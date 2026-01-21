/**
 * [TREO] - Treo Enrollment API Service
 * Date: 2026-01-16
 * Purpose: API service calls for Treo enrollment workflow
 */
import api from '../api/client'

export interface TreoUploadResponse {
  success: boolean
  enrollment_file_id: number
  message: string
  json_data?: any // Parsed JSON structure (available immediately after upload)
  validation_results: {
    validation_status: string
    errors_count: number
    warnings_count: number
    schema_validation: {
      is_valid: boolean
      schema_version: string
    }
  }
  duplicate_detected: boolean
  warnings: number
  errors?: number
}

export interface TreoEnrollment {
  enrollment_file_id: number
  client_id: number
  lob_id: number
  file_name: string
  file_size_bytes: number
  processing_status: string
  processed_at: string | null
  created_at: string
  edi_data: any // JSON structure
}

export interface TreoProcessLog {
  process_log_id: number
  log_type: 'error' | 'warning' | 'info' | 'debug'
  log_level: 'ERROR' | 'WARN' | 'INFO' | 'DEBUG'
  message: string
  error_code?: string
  segment_code?: string
  element_ref?: string
  line_number?: number
  metadata?: any
  created_at: string
}

export interface TreoLogsResponse {
  enrollment_file_id: number
  file_name: string
  logs: TreoProcessLog[]
  total_logs: number
}

export interface TreoEnrollmentListResponse {
  total: number
  limit: number
  offset: number
  enrollments: Array<{
    enrollment_file_id: number
    client_id: number
    lob_id: number
    file_name: string
    file_size_bytes: number
    processing_status: string
    processed_at: string | null
    created_at: string
  }>
}

export interface TreoAnalytics {
  enrollment_file_id: number
  file_info: {
    enrollment_file_id: number
    file_name: string
    file_size_bytes: number
    file_size_mb: number
    client_id: number
    lob_id: number
    processing_status: string
    processed_at: string | null
    created_at: string
  }
  member_statistics: {
    total_members_processed: number
    unique_members: number
    duplicate_members: number
    duplicate_percentage: number
  }
  duplicate_analysis: {
    total_duplicate_members: number
    max_occurrences: number
    duplicate_members: Array<{
      ref02_1: string
      occurrence_count: number
      first_occurrence_index: number
      last_occurrence_index: number
      occurrence_span: number
    }>
  }
  segment_statistics: {
    total_member_records: number
    ins_segments: number
    nm1_segments: number
    dmg_segments: number
    hd_segments: number
    amt_segments: number
  }
  transaction_statistics: {
    total_transaction_sets: number
    first_transaction_index: number | null
    last_transaction_index: number | null
  }
  additional_data_statistics: {
    total_ls_le_loops: number
    members_with_ls_le: number
    max_ls_le_index_per_member: number
  }
  processing_summary: {
    total_logs: number
    error_count: number
    warning_count: number
    info_count: number
    debug_count: number
    processing_status: string
  }
}

/**
 * Upload and process EDI 834 file using Treo workflow
 */
export const uploadTreoEnrollment = async (
  file: File,
  clientId: number,
  lobId: number,
  duplicateMode: 'reject' | 'warn' | 'allow' = 'warn',
  createdBy?: string
): Promise<TreoUploadResponse> => {
  const formData = new FormData()
  formData.append('file', file)
  formData.append('client_id', clientId.toString())
  formData.append('lob_id', lobId.toString())
  formData.append('duplicate_mode', duplicateMode)
  if (createdBy) {
    formData.append('created_by', createdBy)
  }
  
  const response = await api.post<TreoUploadResponse>(
    '/api/v1/treo/enrollments/upload',
    formData,
    {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    }
  )
  
  return response.data
}

/**
 * Get enrollment file JSON by ID
 */
export const getTreoEnrollment = async (enrollmentFileId: number): Promise<TreoEnrollment> => {
  try {
    console.log('Calling API:', `/api/v1/treo/enrollments/${enrollmentFileId}`)
    const response = await api.get<TreoEnrollment>(`/api/v1/treo/enrollments/${enrollmentFileId}`)
    console.log('API response received:', response)
    return response.data
  } catch (error: any) {
    console.error('API call failed:', error)
    throw error
  }
}

/**
 * Get process logs for an enrollment file
 */
export const getTreoEnrollmentLogs = async (
  enrollmentFileId: number,
  logType?: 'error' | 'warning' | 'info' | 'debug'
): Promise<TreoLogsResponse> => {
  const params = new URLSearchParams()
  if (logType) {
    params.append('log_type', logType)
  }
  
  const response = await api.get<TreoLogsResponse>(
    `/api/v1/treo/enrollments/${enrollmentFileId}/logs${params.toString() ? '?' + params.toString() : ''}`
  )
  return response.data
}

/**
 * List enrollment files with filters
 */
export const listTreoEnrollments = async (
  clientId?: number,
  lobId?: number,
  processingStatus?: string,
  limit: number = 100,
  offset: number = 0
): Promise<TreoEnrollmentListResponse> => {
  const params = new URLSearchParams()
  if (clientId) params.append('client_id', clientId.toString())
  if (lobId) params.append('lob_id', lobId.toString())
  if (processingStatus) params.append('processing_status', processingStatus)
  params.append('limit', limit.toString())
  params.append('offset', offset.toString())
  
  const response = await api.get<TreoEnrollmentListResponse>(
    `/api/v1/treo/enrollments?${params.toString()}`
  )
  return response.data
}

/**
 * Get analytics for an enrollment file
 */
export const getTreoEnrollmentAnalytics = async (
  enrollmentFileId: number
): Promise<TreoAnalytics> => {
  const response = await api.get<TreoAnalytics>(
    `/api/v1/treo/enrollments/${enrollmentFileId}/analytics`
  )
  return response.data
}
