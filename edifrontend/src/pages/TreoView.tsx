/**
 * [TREO] - Treo Enrollment View Page
 * Date: 2026-01-20
 * Purpose: Display parsed EDI 834 JSON data for review in the browser
 */
import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import {
  Typography,
  Box,
  CircularProgress,
  Container,
  Button,
  Alert,
  Paper,
  Chip,
  Accordion,
  AccordionSummary,
  AccordionDetails,
} from '@mui/material'
import ExpandMoreIcon from '@mui/icons-material/ExpandMore'
import { getTreoEnrollment, type TreoEnrollment } from '../services/treoService'

export default function TreoView() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [data, setData] = useState<TreoEnrollment | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [expandedSection, setExpandedSection] = useState<string | false>('interchange')

  useEffect(() => {
    if (!id) {
      setError('No enrollment ID provided')
      setLoading(false)
      return
    }

    const enrollmentId = parseInt(id)
    if (isNaN(enrollmentId)) {
      setError('Invalid enrollment ID')
      setLoading(false)
      return
    }

    console.log('Fetching enrollment:', enrollmentId)
    setLoading(true)
    setError(null)
    setData(null)
    
    // Add timeout to prevent infinite loading
    let timeoutId: NodeJS.Timeout | null = null
    let isMounted = true
    
    timeoutId = setTimeout(() => {
      if (isMounted) {
        console.error('Request timeout - no response after 30 seconds')
        setError('Request timeout - please check your network connection and try again')
        setLoading(false)
      }
    }, 30000)
    
    getTreoEnrollment(enrollmentId)
      .then((result) => {
        if (timeoutId) clearTimeout(timeoutId)
        if (!isMounted) return
        
        console.log('Enrollment data received:', result)
        if (result && result.edi_data) {
          console.log('EDI data exists:', Object.keys(result.edi_data))
        } else {
          console.warn('No edi_data in response:', result)
        }
        setData(result)
        setLoading(false)
      })
      .catch((err: any) => {
        if (timeoutId) clearTimeout(timeoutId)
        if (!isMounted) return
        
        console.error('Error fetching enrollment:', err)
        console.error('Error details:', {
          message: err.message,
          status: err.status,
          data: err.data,
          response: err.response,
          fullError: err,
        })
        // Handle both axios interceptor format and direct axios errors
        const errorMessage = err.data?.detail || err.message || err.response?.data?.detail || 'Failed to fetch enrollment data'
        setError(errorMessage)
        setLoading(false)
      })
    
    // Cleanup on unmount
    return () => {
      isMounted = false
      if (timeoutId) clearTimeout(timeoutId)
    }
  }, [id])

  const handleSectionChange = (section: string) => (event: React.SyntheticEvent, isExpanded: boolean) => {
    setExpandedSection(isExpanded ? section : false)
  }

  const renderJSON = (obj: any, depth: number = 0): JSX.Element => {
    if (obj === null || obj === undefined) {
      return <Typography component="span" sx={{ color: 'text.secondary', fontStyle: 'italic' }}>null</Typography>
    }

    if (typeof obj === 'string' || typeof obj === 'number' || typeof obj === 'boolean') {
      return (
        <Typography
          component="span"
          sx={{
            color: typeof obj === 'string' ? '#2e7d32' : typeof obj === 'number' ? '#1976d2' : '#9c27b0',
            fontFamily: 'monospace',
          }}
        >
          {typeof obj === 'string' ? `"${obj}"` : String(obj)}
        </Typography>
      )
    }

    if (Array.isArray(obj)) {
      if (obj.length === 0) {
        return <Typography component="span" sx={{ color: 'text.secondary', fontStyle: 'italic' }}>[]</Typography>
      }
      return (
        <Box sx={{ pl: 2, borderLeft: '1px solid #e0e0e0' }}>
          {obj.map((item, idx) => (
            <Box key={idx} sx={{ mb: 1 }}>
              <Typography component="span" sx={{ color: 'text.secondary', fontFamily: 'monospace' }}>
                [{idx}]:
              </Typography>
              <Box sx={{ pl: 2, mt: 0.5 }}>{renderJSON(item, depth + 1)}</Box>
            </Box>
          ))}
        </Box>
      )
    }

    if (typeof obj === 'object') {
      const keys = Object.keys(obj)
      if (keys.length === 0) {
        return <Typography component="span" sx={{ color: 'text.secondary', fontStyle: 'italic' }}>{'{}'}</Typography>
      }
      return (
        <Box sx={{ pl: depth > 0 ? 2 : 0, borderLeft: depth > 0 ? '1px solid #e0e0e0' : 'none' }}>
          {keys.map((key) => (
            <Box key={key} sx={{ mb: 1 }}>
              <Typography
                component="span"
                sx={{
                  color: '#d32f2f',
                  fontFamily: 'monospace',
                  fontWeight: 'bold',
                  mr: 1,
                }}
              >
                {key}:
              </Typography>
              <Box sx={{ display: 'inline-block', pl: 1 }}>{renderJSON(obj[key], depth + 1)}</Box>
            </Box>
          ))}
        </Box>
      )
    }

    return <Typography component="span">{String(obj)}</Typography>
  }

  if (loading) {
    return (
      <Container maxWidth="lg">
        <Box display="flex" justifyContent="center" alignItems="center" minHeight="80vh">
          <CircularProgress />
        </Box>
      </Container>
    )
  }

  if (error) {
    return (
      <Container maxWidth="lg">
        <Box p={3}>
          <Alert severity="error" sx={{ mb: 2 }}>
            <Typography variant="h6" gutterBottom>
              Error Loading Enrollment Data
            </Typography>
            <Typography variant="body2">{error}</Typography>
            <Typography variant="body2" sx={{ mt: 1, fontFamily: 'monospace', fontSize: '0.75rem' }}>
              Check browser console for details
            </Typography>
          </Alert>
          <Button variant="contained" onClick={() => navigate('/treo')}>
            Back to Upload
          </Button>
        </Box>
      </Container>
    )
  }

  if (!data) {
    return (
      <Container maxWidth="lg">
        <Box p={3}>
          <Alert severity="warning" sx={{ mb: 2 }}>
            <Typography variant="h6" gutterBottom>
              No Data Available
            </Typography>
            <Typography variant="body2">No enrollment data found for ID: {id}</Typography>
          </Alert>
          <Button variant="contained" onClick={() => navigate('/treo')}>
            Back to Upload
          </Button>
        </Box>
      </Container>
    )
  }

  const jsonData = data.edi_data || {}

  return (
    <Container maxWidth="xl">
      <Box p={3}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
          <Box>
            <Typography variant="h4" gutterBottom>
              EDI 834 Parsed JSON Data
            </Typography>
            <Typography variant="body1" color="text.secondary">
              File: {data.file_name} | Enrollment ID: {data.enrollment_file_id}
            </Typography>
          </Box>
          <Box sx={{ display: 'flex', gap: 1 }}>
            <Chip 
              label={`Processing: ${data.processing_status}`} 
              color={data.processing_status === 'completed' ? 'success' : data.processing_status === 'failed' ? 'error' : 'primary'} 
            />
          </Box>
        </Box>

        <Box sx={{ mb: 2, display: 'flex', gap: 2 }}>
          <Button variant="outlined" onClick={() => navigate('/treo')}>
            Back to Upload
          </Button>
          <Button
            variant="outlined"
            onClick={() => {
              const jsonString = JSON.stringify(jsonData, null, 2)
              const blob = new Blob([jsonString], { type: 'application/json' })
              const url = URL.createObjectURL(blob)
              const a = document.createElement('a')
              a.href = url
              a.download = `${data.file_name}_parsed.json`
              a.click()
              URL.revokeObjectURL(url)
            }}
          >
            Download JSON
          </Button>
        </Box>

        {!jsonData || Object.keys(jsonData).length === 0 ? (
          <Alert severity="warning">
            No JSON data available for this enrollment file.
          </Alert>
        ) : (
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom sx={{ mb: 2 }}>
              JSON Structure
            </Typography>

            {/* Interchange Section */}
            {jsonData.interchange && (
              <Accordion
                expanded={expandedSection === 'interchange'}
                onChange={handleSectionChange('interchange')}
                sx={{ mb: 1 }}
              >
                <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                  <Typography variant="subtitle1" sx={{ fontWeight: 'bold' }}>
                    Interchange (ISA/IEA)
                  </Typography>
                </AccordionSummary>
                <AccordionDetails>
                  <Box
                    sx={{
                      p: 2,
                      bgcolor: '#f5f5f5',
                      borderRadius: 1,
                      overflow: 'auto',
                      maxHeight: '500px',
                    }}
                  >
                    {renderJSON(jsonData.interchange)}
                  </Box>
                </AccordionDetails>
              </Accordion>
            )}

            {/* Functional Group Section */}
            {jsonData.functional_group && (
              <Accordion
                expanded={expandedSection === 'functional_group'}
                onChange={handleSectionChange('functional_group')}
                sx={{ mb: 1 }}
              >
                <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                  <Typography variant="subtitle1" sx={{ fontWeight: 'bold' }}>
                    Functional Group (GS/GE)
                  </Typography>
                </AccordionSummary>
                <AccordionDetails>
                  <Box
                    sx={{
                      p: 2,
                      bgcolor: '#f5f5f5',
                      borderRadius: 1,
                      overflow: 'auto',
                      maxHeight: '500px',
                    }}
                  >
                    {renderJSON(jsonData.functional_group)}
                  </Box>
                </AccordionDetails>
              </Accordion>
            )}

            {/* Transaction Set Section */}
            {jsonData.transaction_set && (
              <Accordion
                expanded={expandedSection === 'transaction_set'}
                onChange={handleSectionChange('transaction_set')}
                sx={{ mb: 1 }}
              >
                <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                  <Typography variant="subtitle1" sx={{ fontWeight: 'bold' }}>
                    Transaction Set (ST/BGN/Loops/SE)
                  </Typography>
                </AccordionSummary>
                <AccordionDetails>
                  <Box
                    sx={{
                      p: 2,
                      bgcolor: '#f5f5f5',
                      borderRadius: 1,
                      overflow: 'auto',
                      maxHeight: '600px',
                    }}
                  >
                    {renderJSON(jsonData.transaction_set)}
                  </Box>
                </AccordionDetails>
              </Accordion>
            )}

            {/* Metadata Section */}
            {jsonData.metadata && (
              <Accordion
                expanded={expandedSection === 'metadata'}
                onChange={handleSectionChange('metadata')}
                sx={{ mb: 1 }}
              >
                <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                  <Typography variant="subtitle1" sx={{ fontWeight: 'bold' }}>
                    Metadata
                  </Typography>
                </AccordionSummary>
                <AccordionDetails>
                  <Box
                    sx={{
                      p: 2,
                      bgcolor: '#f5f5f5',
                      borderRadius: 1,
                      overflow: 'auto',
                      maxHeight: '300px',
                    }}
                  >
                    {renderJSON(jsonData.metadata)}
                  </Box>
                </AccordionDetails>
              </Accordion>
            )}

            {/* Full JSON View */}
            <Accordion
              expanded={expandedSection === 'full_json'}
              onChange={handleSectionChange('full_json')}
            >
              <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                <Typography variant="subtitle1" sx={{ fontWeight: 'bold' }}>
                  Full JSON (Raw)
                </Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Box
                  sx={{
                    p: 2,
                    bgcolor: '#f5f5f5',
                    borderRadius: 1,
                    overflow: 'auto',
                    maxHeight: '800px',
                  }}
                >
                  <pre style={{ margin: 0, fontFamily: 'monospace', fontSize: '0.875rem', whiteSpace: 'pre-wrap' }}>
                    {JSON.stringify(jsonData, null, 2)}
                  </pre>
                </Box>
              </AccordionDetails>
            </Accordion>
          </Paper>
        )}
      </Box>
    </Container>
  )
}
