/**
 * [NEW] - Created for Phase 2: Fresh Frontend
 * Date: 2026-01-08
 * Purpose: Clean axios API client for edibackend
 */
import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      // Server responded with error
      return Promise.reject({
        message: error.response.data?.detail || error.response.data?.message || 'Request failed',
        status: error.response.status,
        data: error.response.data,
      })
    } else if (error.request) {
      // Request made but no response
      return Promise.reject({
        message: 'Network error - unable to reach server',
        status: 0,
      })
    } else {
      // Something else happened
      return Promise.reject({
        message: error.message || 'Unknown error occurred',
        status: 0,
      })
    }
  }
)

export default api
