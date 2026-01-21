/**
 * [TREO] - Treo Enrollment Analytics View
 * Date: 2026-01-21
 * Purpose: Display comprehensive analytics for processed EDI 834 files
 */
import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import {
  Typography,
  Box,
  Container,
  Paper,
  Grid,
  Card,
  CardContent,
  Chip,
  CircularProgress,
  Alert,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Button,
} from '@mui/material'
import {
  ArrowBack,
  People,
  FileUpload,
  Warning as WarningIcon,
  CheckCircle,
  Error as ErrorIcon,
  Assessment,
} from '@mui/icons-material'
import { getTreoEnrollmentAnalytics, type TreoAnalytics } from '../services/treoService'

const TreoAnalytics = () => {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [analytics, setAnalytics] = useState<TreoAnalytics | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchAnalytics = async () => {
      if (!id) return
      
      try {
        setLoading(true)
        const data = await getTreoEnrollmentAnalytics(parseInt(id))
        setAnalytics(data)
      } catch (err: any) {
        setError(err.response?.data?.detail || err.message || 'Failed to load analytics')
      } finally {
        setLoading(false)
      }
    }

    fetchAnalytics()
  }, [id])

  if (loading) {
    return (
      <Container maxWidth="lg">
        <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '400px' }}>
          <CircularProgress />
        </Box>
      </Container>
    )
  }

  if (error || !analytics) {
    return (
      <Container maxWidth="lg">
        <Alert severity="error" sx={{ mt: 4 }}>
          {error || 'Analytics not found'}
        </Alert>
      </Container>
    )
  }

  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 4, mb: 4 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
          <Button
            startIcon={<ArrowBack />}
            onClick={() => navigate('/treo')}
            sx={{ mr: 2 }}
          >
            Back to Upload
          </Button>
          <Typography variant="h4" component="h1">
            <Assessment sx={{ mr: 1, verticalAlign: 'middle' }} />
            File Analytics
          </Typography>
        </Box>

        {/* File Information */}
        <Paper sx={{ p: 3, mb: 3 }}>
          <Typography variant="h6" gutterBottom>
            File Information
          </Typography>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={6}>
              <Typography variant="body2" color="text.secondary">
                File Name
              </Typography>
              <Typography variant="body1" fontWeight="bold">
                {analytics.file_info.file_name}
              </Typography>
            </Grid>
            <Grid item xs={12} sm={6}>
              <Typography variant="body2" color="text.secondary">
                File Size
              </Typography>
              <Typography variant="body1" fontWeight="bold">
                {analytics.file_info.file_size_mb} MB ({analytics.file_info.file_size_bytes.toLocaleString()} bytes)
              </Typography>
            </Grid>
            <Grid item xs={12} sm={4}>
              <Typography variant="body2" color="text.secondary">
                Enrollment File ID
              </Typography>
              <Typography variant="body1" fontWeight="bold">
                {analytics.file_info.enrollment_file_id}
              </Typography>
            </Grid>
            <Grid item xs={12} sm={4}>
              <Typography variant="body2" color="text.secondary">
                Client ID
              </Typography>
              <Typography variant="body1" fontWeight="bold">
                {analytics.file_info.client_id}
              </Typography>
            </Grid>
            <Grid item xs={12} sm={4}>
              <Typography variant="body2" color="text.secondary">
                LOB ID
              </Typography>
              <Typography variant="body1" fontWeight="bold">
                {analytics.file_info.lob_id}
              </Typography>
            </Grid>
            <Grid item xs={12} sm={6}>
              <Typography variant="body2" color="text.secondary">
                Processing Status
              </Typography>
              <Chip
                label={analytics.file_info.processing_status}
                color={analytics.file_info.processing_status === 'completed' ? 'success' : 'default'}
                sx={{ mt: 0.5 }}
              />
            </Grid>
          </Grid>
        </Paper>

        {/* Key Statistics Cards */}
        <Grid container spacing={3} sx={{ mb: 3 }}>
          <Grid item xs={12} sm={6} md={3}>
            <Card>
              <CardContent>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                  <People color="primary" sx={{ mr: 1 }} />
                  <Typography variant="h6">
                    {analytics.member_statistics.total_members_processed.toLocaleString()}
                  </Typography>
                </Box>
                <Typography variant="body2" color="text.secondary">
                  Total Members Processed
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Card>
              <CardContent>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                  <People color="success" sx={{ mr: 1 }} />
                  <Typography variant="h6">
                    {analytics.member_statistics.unique_members.toLocaleString()}
                  </Typography>
                </Box>
                <Typography variant="body2" color="text.secondary">
                  Unique Members
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Card>
              <CardContent>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                  <WarningIcon color="warning" sx={{ mr: 1 }} />
                  <Typography variant="h6">
                    {analytics.member_statistics.duplicate_members.toLocaleString()}
                  </Typography>
                </Box>
                <Typography variant="body2" color="text.secondary">
                  Duplicate Members ({analytics.member_statistics.duplicate_percentage}%)
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Card>
              <CardContent>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                  <FileUpload color="info" sx={{ mr: 1 }} />
                  <Typography variant="h6">
                    {analytics.transaction_statistics.total_transaction_sets}
                  </Typography>
                </Box>
                <Typography variant="body2" color="text.secondary">
                  Transaction Sets
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        </Grid>

        {/* Member Statistics */}
        <Paper sx={{ p: 3, mb: 3 }}>
          <Typography variant="h6" gutterBottom>
            Member Statistics
          </Typography>
          <Grid container spacing={2}>
            <Grid item xs={12} md={6}>
              <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                <Typography variant="body2" color="text.secondary">
                  Total Members Processed
                </Typography>
                <Typography variant="h5" fontWeight="bold">
                  {analytics.member_statistics.total_members_processed.toLocaleString()}
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} md={6}>
              <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                <Typography variant="body2" color="text.secondary">
                  Unique Members
                </Typography>
                <Typography variant="h5" fontWeight="bold" color="success.main">
                  {analytics.member_statistics.unique_members.toLocaleString()}
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} md={6}>
              <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                <Typography variant="body2" color="text.secondary">
                  Duplicate Members
                </Typography>
                <Typography variant="h5" fontWeight="bold" color="warning.main">
                  {analytics.member_statistics.duplicate_members.toLocaleString()}
                </Typography>
                <Typography variant="body2" color="text.secondary" sx={{ mt: 0.5 }}>
                  {analytics.member_statistics.duplicate_percentage}% of total
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} md={6}>
              <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                <Typography variant="body2" color="text.secondary">
                  Max Occurrences
                </Typography>
                <Typography variant="h5" fontWeight="bold">
                  {analytics.duplicate_analysis.max_occurrences}
                </Typography>
                <Typography variant="body2" color="text.secondary" sx={{ mt: 0.5 }}>
                  {analytics.duplicate_analysis.total_duplicate_members} members appear multiple times
                </Typography>
              </Box>
            </Grid>
          </Grid>
        </Paper>

        {/* Duplicate Analysis */}
        {analytics.duplicate_analysis.duplicate_members.length > 0 && (
          <Paper sx={{ p: 3, mb: 3 }}>
            <Typography variant="h6" gutterBottom>
              Duplicate Members Analysis (Top 20)
            </Typography>
            <TableContainer>
              <Table size="small">
                <TableHead>
                  <TableRow>
                    <TableCell>Member ID (ref02_1)</TableCell>
                    <TableCell align="right">Occurrences</TableCell>
                    <TableCell align="right">First Occurrence</TableCell>
                    <TableCell align="right">Last Occurrence</TableCell>
                    <TableCell align="right">Span</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {analytics.duplicate_analysis.duplicate_members.map((member) => (
                    <TableRow key={member.ref02_1}>
                      <TableCell>{member.ref02_1}</TableCell>
                      <TableCell align="right">{member.occurrence_count}</TableCell>
                      <TableCell align="right">{member.first_occurrence_index}</TableCell>
                      <TableCell align="right">{member.last_occurrence_index}</TableCell>
                      <TableCell align="right">{member.occurrence_span}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          </Paper>
        )}

        {/* Segment Statistics */}
        <Paper sx={{ p: 3, mb: 3 }}>
          <Typography variant="h6" gutterBottom>
            Segment Statistics
          </Typography>
          <Grid container spacing={2}>
            <Grid item xs={6} sm={4} md={2}>
              <Box sx={{ textAlign: 'center', p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                <Typography variant="h6">
                  {analytics.segment_statistics.ins_segments.toLocaleString()}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  INS Segments
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={6} sm={4} md={2}>
              <Box sx={{ textAlign: 'center', p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                <Typography variant="h6">
                  {analytics.segment_statistics.nm1_segments.toLocaleString()}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  NM1 Segments
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={6} sm={4} md={2}>
              <Box sx={{ textAlign: 'center', p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                <Typography variant="h6">
                  {analytics.segment_statistics.dmg_segments.toLocaleString()}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  DMG Segments
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={6} sm={4} md={2}>
              <Box sx={{ textAlign: 'center', p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                <Typography variant="h6">
                  {analytics.segment_statistics.hd_segments.toLocaleString()}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  HD Segments
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={6} sm={4} md={2}>
              <Box sx={{ textAlign: 'center', p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                <Typography variant="h6">
                  {analytics.segment_statistics.amt_segments.toLocaleString()}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  AMT Segments
                </Typography>
              </Box>
            </Grid>
          </Grid>
        </Paper>

        {/* Processing Summary */}
        <Paper sx={{ p: 3, mb: 3 }}>
          <Typography variant="h6" gutterBottom>
            Processing Summary
          </Typography>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={6} md={3}>
              <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1, textAlign: 'center' }}>
                <ErrorIcon color="error" sx={{ fontSize: 40, mb: 1 }} />
                <Typography variant="h5" fontWeight="bold" color="error.main">
                  {analytics.processing_summary.error_count}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Errors
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} sm={6} md={3}>
              <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1, textAlign: 'center' }}>
                <WarningIcon color="warning" sx={{ fontSize: 40, mb: 1 }} />
                <Typography variant="h5" fontWeight="bold" color="warning.main">
                  {analytics.processing_summary.warning_count}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Warnings
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} sm={6} md={3}>
              <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1, textAlign: 'center' }}>
                <CheckCircle color="info" sx={{ fontSize: 40, mb: 1 }} />
                <Typography variant="h5" fontWeight="bold" color="info.main">
                  {analytics.processing_summary.info_count}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Info Logs
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} sm={6} md={3}>
              <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1, textAlign: 'center' }}>
                <Assessment color="primary" sx={{ fontSize: 40, mb: 1 }} />
                <Typography variant="h5" fontWeight="bold">
                  {analytics.processing_summary.total_logs}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Total Logs
                </Typography>
              </Box>
            </Grid>
          </Grid>
        </Paper>

        {/* Additional Data Statistics */}
        {analytics.additional_data_statistics.total_ls_le_loops > 0 && (
          <Paper sx={{ p: 3, mb: 3 }}>
            <Typography variant="h6" gutterBottom>
              Additional Reporting Data (LS/LE Loops)
            </Typography>
            <Grid container spacing={2}>
              <Grid item xs={12} md={4}>
                <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                  <Typography variant="body2" color="text.secondary">
                    Total LS/LE Loops
                  </Typography>
                  <Typography variant="h5" fontWeight="bold">
                    {analytics.additional_data_statistics.total_ls_le_loops.toLocaleString()}
                  </Typography>
                </Box>
              </Grid>
              <Grid item xs={12} md={4}>
                <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                  <Typography variant="body2" color="text.secondary">
                    Members with LS/LE
                  </Typography>
                  <Typography variant="h5" fontWeight="bold">
                    {analytics.additional_data_statistics.members_with_ls_le.toLocaleString()}
                  </Typography>
                </Box>
              </Grid>
              <Grid item xs={12} md={4}>
                <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 1 }}>
                  <Typography variant="body2" color="text.secondary">
                    Max LS/LE Index per Member
                  </Typography>
                  <Typography variant="h5" fontWeight="bold">
                    {analytics.additional_data_statistics.max_ls_le_index_per_member}
                  </Typography>
                </Box>
              </Grid>
            </Grid>
          </Paper>
        )}
      </Box>
    </Container>
  )
}

export default TreoAnalytics
