/**
 * [TREO] - Treo Enrollment Upload Page
 * Date: 2026-01-21
 * Purpose: Upload EDI 834 file with stepper progress and analytics
 */
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  Typography,
  Box,
  Button,
  LinearProgress,
  Alert,
  Container,
  TextField,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  FormHelperText,
  Paper,
  Chip,
  Stepper,
  Step,
  StepLabel,
  StepContent,
  Collapse,
  List,
  ListItem,
  ListItemText,
  IconButton,
  Divider,
} from '@mui/material'
import {
  ExpandMore,
  ExpandLess,
  CheckCircle,
  Error as ErrorIcon,
  Warning as WarningIcon,
  Info as InfoIcon,
} from '@mui/icons-material'
import { uploadTreoEnrollment, getTreoEnrollmentLogs, type TreoUploadResponse, type TreoProcessLog } from '../services/treoService'

type ProcessingStep = 'idle' | 'uploading' | 'parsing' | 'validating' | 'storing' | 'complete' | 'error'

const TreoUpload = () => {
  const navigate = useNavigate()
  const [file, setFile] = useState<File | null>(null)
  const [uploading, setUploading] = useState(false)
  const [currentStep, setCurrentStep] = useState<ProcessingStep>('idle')
  const [progress, setProgress] = useState(0)
  const [error, setError] = useState<string | null>(null)
  const [clientId, setClientId] = useState<string>('1')
  const [lobId, setLobId] = useState<string>('1')
  const [duplicateMode, setDuplicateMode] = useState<'reject' | 'warn' | 'allow'>('warn')
  const [createdBy, setCreatedBy] = useState<string>('')
  const [uploadResult, setUploadResult] = useState<TreoUploadResponse | null>(null)
  const [errorLogs, setErrorLogs] = useState<TreoProcessLog[]>([])
  const [warningLogs, setWarningLogs] = useState<TreoProcessLog[]>([])
  const [showErrors, setShowErrors] = useState(false)
  const [showWarnings, setShowWarnings] = useState(false)

  const steps = [
    { label: 'Upload File', step: 'uploading' as ProcessingStep },
    { label: 'Parse EDI', step: 'parsing' as ProcessingStep },
    { label: 'Validate Data', step: 'validating' as ProcessingStep },
    { label: 'Store Results', step: 'storing' as ProcessingStep },
    { label: 'Complete', step: 'complete' as ProcessingStep },
  ]

  const getActiveStep = () => {
    const stepIndex = steps.findIndex(s => s.step === currentStep)
    return stepIndex >= 0 ? stepIndex : 0
  }

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0])
      setError(null)
      setUploadResult(null)
      setCurrentStep('idle')
      setErrorLogs([])
      setWarningLogs([])
    }
  }

  const handleUpload = async () => {
    if (!file) return

    setUploading(true)
    setError(null)
    setUploadResult(null)
    setProgress(0)
    setCurrentStep('uploading')
    setErrorLogs([])
    setWarningLogs([])

    try {
      // Step 1: Uploading
      setProgress(10)
      setCurrentStep('uploading')
      
      const clientIdNum = parseInt(clientId) || 1
      const lobIdNum = parseInt(lobId) || 1
      
      // Step 2: Parsing
      setProgress(30)
      setCurrentStep('parsing')
      
      const response = await uploadTreoEnrollment(
        file,
        clientIdNum,
        lobIdNum,
        duplicateMode,
        createdBy || undefined
      )
      
      // Step 3: Validating
      setProgress(60)
      setCurrentStep('validating')
      
      // Step 4: Storing
      setProgress(80)
      setCurrentStep('storing')
      
      // Fetch error and warning logs
      if (response.enrollment_file_id) {
        try {
          const [errorLogsResponse, warningLogsResponse] = await Promise.all([
            getTreoEnrollmentLogs(response.enrollment_file_id, 'error'),
            getTreoEnrollmentLogs(response.enrollment_file_id, 'warning')
          ])
          setErrorLogs(errorLogsResponse.logs || [])
          setWarningLogs(warningLogsResponse.logs || [])
        } catch (logError) {
          console.error('Failed to fetch logs:', logError)
        }
      }
      
      // Step 5: Complete
      setProgress(100)
      setCurrentStep('complete')
      setUploadResult(response)
      setUploading(false)

      // Redirect to analytics view after successful upload
      if (response.success) {
        setTimeout(() => {
          navigate(`/treo/analytics/${response.enrollment_file_id}`)
        }, 3000)
      }
    } catch (err: any) {
      console.error('Upload error:', err)
      setUploading(false)
      setProgress(0)
      setCurrentStep('error')
      
      const errorMessage = err.response?.data?.detail || err.message || 'Upload failed'
      setError(errorMessage)
    }
  }

  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Treo Enrollment - Upload EDI 834 File
        </Typography>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
          Upload and process EDI 834 file using Treo architecture
        </Typography>

        <Box sx={{ mt: 4, maxWidth: 800 }}>
          <TextField
            fullWidth
            label="Client ID"
            type="number"
            value={clientId}
            onChange={(e) => setClientId(e.target.value)}
            margin="normal"
            required
            disabled={uploading}
          />
          <TextField
            fullWidth
            label="LOB ID"
            type="number"
            value={lobId}
            onChange={(e) => setLobId(e.target.value)}
            margin="normal"
            required
            disabled={uploading}
          />
          <TextField
            fullWidth
            label="Created By (optional)"
            value={createdBy}
            onChange={(e) => setCreatedBy(e.target.value)}
            margin="normal"
            placeholder="User name or ID"
            disabled={uploading}
          />

          {/* Duplicate Detection Settings */}
          <Paper sx={{ p: 2, mt: 2, mb: 2, bgcolor: 'background.default' }}>
            <Typography variant="h6" gutterBottom>
              Duplicate Detection Settings
            </Typography>
            <FormControl fullWidth sx={{ mt: 2 }}>
              <InputLabel>Duplicate Detection Mode</InputLabel>
              <Select
                value={duplicateMode}
                onChange={(e) => setDuplicateMode(e.target.value as 'reject' | 'warn' | 'allow')}
                label="Duplicate Detection Mode"
                disabled={uploading}
              >
                <MenuItem value="reject">
                  Reject - Block duplicate files (HTTP 400)
                </MenuItem>
                <MenuItem value="warn">
                  Warn - Process but flag in response
                </MenuItem>
                <MenuItem value="allow">
                  Allow - Process normally, log only
                </MenuItem>
              </Select>
              <FormHelperText>
                {duplicateMode === 'reject' && 'Duplicate files will be rejected immediately'}
                {duplicateMode === 'warn' && 'Duplicate files will be processed with a warning'}
                {duplicateMode === 'allow' && 'Duplicate files will be processed normally (logged only)'}
              </FormHelperText>
            </FormControl>
          </Paper>

          <Box sx={{ mt: 2, mb: 2 }}>
            <input
              type="file"
              accept=".edi,.x12,.txt"
              onChange={handleFileChange}
              disabled={uploading}
              style={{ marginBottom: '1rem', display: 'block' }}
            />
          </Box>

          <Button
            variant="contained"
            onClick={handleUpload}
            disabled={!file || uploading || !clientId || !lobId}
            sx={{ mb: 2 }}
            fullWidth
            size="large"
          >
            {uploading ? 'Processing...' : 'Upload & Process'}
          </Button>

          {/* Processing Stepper */}
          {uploading && (
            <Paper sx={{ p: 3, mb: 2 }}>
              <Typography variant="h6" gutterBottom>
                Processing Progress
              </Typography>
              <Stepper activeStep={getActiveStep()} orientation="vertical">
                {steps.map((step, index) => (
                  <Step key={step.label}>
                    <StepLabel
                      StepIconComponent={
                        currentStep === step.step
                          ? undefined
                          : currentStep === 'error' && index < getActiveStep()
                          ? undefined
                          : index < getActiveStep()
                          ? CheckCircle
                          : undefined
                      }
                    >
                      {step.label}
                    </StepLabel>
                    <StepContent>
                      {currentStep === step.step && (
                        <Box sx={{ mb: 2 }}>
                          <LinearProgress variant="determinate" value={progress} />
                          <Typography variant="body2" sx={{ mt: 1 }}>
                            {progress}%
                          </Typography>
                        </Box>
                      )}
                    </StepContent>
                  </Step>
                ))}
              </Stepper>
            </Paper>
          )}

          {/* Error Display */}
          {error && (
            <Alert severity="error" sx={{ mb: 2 }}>
              <Typography variant="h6" gutterBottom>
                <ErrorIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                File Processing Failed
              </Typography>
              <Typography variant="body2" style={{ whiteSpace: 'pre-line' }}>
                {error}
              </Typography>
            </Alert>
          )}

          {/* Success/Result Display */}
          {uploadResult && (
            <Box sx={{ mt: 2 }}>
              <Alert 
                severity={uploadResult.success ? "success" : "warning"} 
                sx={{ mb: 2 }}
              >
                <Typography variant="h6" gutterBottom>
                  {uploadResult.success ? (
                    <>
                      <CheckCircle sx={{ mr: 1, verticalAlign: 'middle' }} />
                      File Processed Successfully!
                    </>
                  ) : (
                    <>
                      <WarningIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                      Processing Completed with Issues
                    </>
                  )}
                </Typography>
                <Box sx={{ mt: 1 }}>
                  <Chip 
                    label={`Enrollment ID: ${uploadResult.enrollment_file_id}`} 
                    color="primary" 
                    sx={{ mr: 1, mb: 1 }} 
                  />
                  <Chip 
                    label={`Validation: ${uploadResult.validation_results.validation_status}`} 
                    color={uploadResult.validation_results.validation_status === 'valid' ? 'success' : 'warning'} 
                    sx={{ mr: 1, mb: 1 }} 
                  />
                  <Chip 
                    label={`Errors: ${uploadResult.validation_results.errors_count || uploadResult.errors || 0}`} 
                    color={(uploadResult.validation_results.errors_count || uploadResult.errors || 0) > 0 ? 'error' : 'default'} 
                    sx={{ mr: 1, mb: 1 }} 
                  />
                  <Chip 
                    label={`Warnings: ${uploadResult.validation_results.warnings_count || uploadResult.warnings || 0}`} 
                    color={(uploadResult.validation_results.warnings_count || uploadResult.warnings || 0) > 0 ? 'warning' : 'default'} 
                    sx={{ mb: 1 }} 
                  />
                </Box>
                {uploadResult.duplicate_detected && (
                  <Typography variant="body2" sx={{ mt: 1 }}>
                    ⚠️ Duplicate file detected (processed with warning)
                  </Typography>
                )}
                {uploadResult.success && (
                  <Typography variant="body2" sx={{ mt: 1 }}>
                    Redirecting to analytics view...
                  </Typography>
                )}
              </Alert>

              {/* Error Logs */}
              {errorLogs.length > 0 && (
                <Paper sx={{ mb: 2 }}>
                  <Box sx={{ p: 2, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <Typography variant="h6" color="error">
                      <ErrorIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                      Errors ({errorLogs.length})
                    </Typography>
                    <IconButton onClick={() => setShowErrors(!showErrors)}>
                      {showErrors ? <ExpandLess /> : <ExpandMore />}
                    </IconButton>
                  </Box>
                  <Collapse in={showErrors}>
                    <Divider />
                    <List>
                      {errorLogs.slice(0, 10).map((log) => (
                        <ListItem key={log.process_log_id}>
                          <ListItemText
                            primary={log.message}
                            secondary={
                              <>
                                {log.error_code && `Code: ${log.error_code} | `}
                                {log.segment_code && `Segment: ${log.segment_code} | `}
                                {log.line_number && `Line: ${log.line_number} | `}
                                {new Date(log.created_at).toLocaleString()}
                              </>
                            }
                          />
                        </ListItem>
                      ))}
                      {errorLogs.length > 10 && (
                        <ListItem>
                          <ListItemText
                            primary={`... and ${errorLogs.length - 10} more errors`}
                            primaryTypographyProps={{ variant: 'body2', color: 'text.secondary' }}
                          />
                        </ListItem>
                      )}
                    </List>
                  </Collapse>
                </Paper>
              )}

              {/* Warning Logs */}
              {warningLogs.length > 0 && (
                <Paper sx={{ mb: 2 }}>
                  <Box sx={{ p: 2, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <Typography variant="h6" color="warning.main">
                      <WarningIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                      Warnings ({warningLogs.length})
                    </Typography>
                    <IconButton onClick={() => setShowWarnings(!showWarnings)}>
                      {showWarnings ? <ExpandLess /> : <ExpandMore />}
                    </IconButton>
                  </Box>
                  <Collapse in={showWarnings}>
                    <Divider />
                    <List>
                      {warningLogs.slice(0, 10).map((log) => (
                        <ListItem key={log.process_log_id}>
                          <ListItemText
                            primary={log.message}
                            secondary={
                              <>
                                {log.error_code && `Code: ${log.error_code} | `}
                                {log.segment_code && `Segment: ${log.segment_code} | `}
                                {log.line_number && `Line: ${log.line_number} | `}
                                {new Date(log.created_at).toLocaleString()}
                              </>
                            }
                          />
                        </ListItem>
                      ))}
                      {warningLogs.length > 10 && (
                        <ListItem>
                          <ListItemText
                            primary={`... and ${warningLogs.length - 10} more warnings`}
                            primaryTypographyProps={{ variant: 'body2', color: 'text.secondary' }}
                          />
                        </ListItem>
                      )}
                    </List>
                  </Collapse>
                </Paper>
              )}
            </Box>
          )}
        </Box>
      </Box>
    </Container>
  )
}

export default TreoUpload
