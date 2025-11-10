import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import ErrorBoundary from './components/ErrorBoundary';
import ProtectedRoute from './components/ProtectedRoute';
import Header from './components/Header';
import HomePage from './pages/HomePage';
import DealsPage from './pages/DealsPage';
import DealDetailsPage from './pages/DealDetailsPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import VendorDashboard from './pages/VendorDashboard';
import VendorProfile from './pages/VendorProfile';
import AddDeal from './pages/AddDeal';
import ManageDeals from './pages/ManageDeals';
import './styles/theme.css';

function App() {
  return (
    <AuthProvider>
      <ErrorBoundary>
        <Router>
          <div className="App">
            <Header />
            <main>
              <ErrorBoundary>
                <Routes>
                  <Route path="/" element={<HomePage />} />
                  <Route path="/deals" element={<DealsPage />} />
                  <Route path="/deals/:id" element={<DealDetailsPage />} />
                  <Route path="/login" element={<LoginPage />} />
                  <Route path="/register" element={<RegisterPage />} />
                  <Route 
                    path="/vendor/dashboard" 
                    element={
                      <ProtectedRoute requireVendor={true} requireCompleteProfile={true}>
                        <VendorDashboard />
                      </ProtectedRoute>
                    } 
                  />
                  <Route 
                    path="/vendor/profile" 
                    element={
                      <ProtectedRoute requireVendor={true}>
                        <VendorProfile />
                      </ProtectedRoute>
                    } 
                  />
                  <Route 
                    path="/vendor/add-deal" 
                    element={
                      <ProtectedRoute requireVendor={true} requireCompleteProfile={true}>
                        <AddDeal />
                      </ProtectedRoute>
                    } 
                  />
                  <Route 
                    path="/vendor/manage-deals" 
                    element={
                      <ProtectedRoute requireVendor={true} requireCompleteProfile={true}>
                        <ManageDeals />
                      </ProtectedRoute>
                    } 
                  />
                </Routes>
              </ErrorBoundary>
            </main>
          </div>
        </Router>
      </ErrorBoundary>
    </AuthProvider>
  );
}

export default App;