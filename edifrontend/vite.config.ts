/**
 * [NEW] - Created for Phase 2: Fresh Frontend
 * Date: 2026-01-08
 * Purpose: Vite configuration with proxy for edibackend
 */
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})
