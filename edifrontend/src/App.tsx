/**
 * [TREO] - Main App Component
 * Purpose: Main application routing for TREO EDI 834 enrollment system
 */
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { CssBaseline, ThemeProvider, createTheme } from '@mui/material'
import TreoUpload from './pages/TreoUpload'
import TreoView from './pages/TreoView'
import TreoAnalytics from './pages/TreoAnalytics'

const theme = createTheme({
  palette: {
    mode: 'light',
  },
})

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Routes>
          <Route path="/" element={<TreoUpload />} />
          <Route path="/treo" element={<TreoUpload />} />
          <Route path="/treo/view/:id" element={<TreoView />} />
          <Route path="/treo/analytics/:id" element={<TreoAnalytics />} />
        </Routes>
      </Router>
    </ThemeProvider>
  )
}

export default App
