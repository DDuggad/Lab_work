import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

const ProtectedRoute = ({ children, requireVendor = false, requireCompleteProfile = false }) => {
  const { isAuthenticated, isVendor, loading, user } = useAuth();

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner">
          <div className="spinner"></div>
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  if (!isAuthenticated()) {
    return <Navigate to="/login" replace />;
  }

  if (requireVendor && !isVendor()) {
    return <Navigate to="/register" replace />;
  }

  // Check if vendor profile is complete for routes that require it
  if (requireVendor && requireCompleteProfile && isVendor() && user && !user.profileCompleted) {
    return <Navigate to="/vendor/profile" replace />;
  }

  return children;
};

export default ProtectedRoute;