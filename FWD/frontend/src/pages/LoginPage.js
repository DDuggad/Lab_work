import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import api from '../utils/api';
import '../styles/theme.css';

const LoginPage = () => {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [fieldErrors, setFieldErrors] = useState({});

  const validateForm = () => {
    const errors = {};
    
    if (!formData.email.trim()) {
      errors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      errors.email = 'Please enter a valid email address';
    }
    
    if (!formData.password) {
      errors.password = 'Password is required';
    } else if (formData.password.length < 6) {
      errors.password = 'Password must be at least 6 characters';
    }
    
    setFieldErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
    // Clear field error when user starts typing
    if (fieldErrors[name]) {
      setFieldErrors({
        ...fieldErrors,
        [name]: ''
      });
    }
    // Clear general error
    if (error) setError('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }
    
    setLoading(true);
    setError('');

    try {
      const response = await api.post('/api/auth/login', formData);
      
      if (!response.data || !response.data.user || !response.data.token) {
        throw new Error('Invalid response from server');
      }
      
      // Use AuthContext login method to update state
      login(response.data.user, response.data.token);
      
      // Redirect based on role and profile completion
      const userRole = (response.data.user.role || '').toLowerCase();
      if (userRole === 'vendor') {
        if (response.data.user.profileCompleted) {
          navigate('/vendor/manage-deals');
        } else {
          navigate('/vendor/profile');
        }
      } else {
        navigate('/deals'); // Regular users go to deals page
      }
    } catch (err) {
      console.error('Login error:', err);
      const errorMessage = err.response?.data?.message || 
                          err.message || 
                          'Unable to login. Please check your credentials and try again.';
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div style={{ 
        maxWidth: '440px', 
        margin: '3rem auto', 
        background: 'white', 
        padding: '2.5rem', 
        borderRadius: '16px', 
        boxShadow: '0 10px 40px rgba(0,0,0,0.1)',
        border: '1px solid #e5e7eb'
      }} className="animate-fade-in">
        <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
          <h2 style={{ 
            color: 'var(--primary-green)', 
            fontSize: '2rem',
            marginBottom: '0.5rem',
            fontWeight: '700'
          }}>Welcome Back</h2>
          <p style={{ color: '#6b7280', fontSize: '0.95rem' }}>
            Sign in to access your vendor dashboard
          </p>
        </div>
        
        {error && (
          <div className="alert alert-error animate-slide-down" style={{
            background: '#fee2e2',
            border: '1px solid #fca5a5',
            color: '#991b1b',
            padding: '0.875rem 1rem',
            borderRadius: '8px',
            marginBottom: '1.5rem',
            fontSize: '0.9rem'
          }}>
            <strong>Error:</strong> {error}
          </div>
        )}
        
        <form onSubmit={handleSubmit}>
          <div className="form-group" style={{ marginBottom: '1.25rem' }}>
            <label style={{ 
              display: 'block',
              marginBottom: '0.5rem',
              color: '#374151',
              fontWeight: '600',
              fontSize: '0.9rem'
            }}>Email Address</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              disabled={loading}
              className="form-input"
              placeholder="your@email.com"
              style={{
                width: '100%',
                padding: '0.75rem 1rem',
                border: fieldErrors.email ? '2px solid #ef4444' : '2px solid #e5e7eb',
                borderRadius: '8px',
                fontSize: '1rem',
                transition: 'all 0.2s',
                outline: 'none'
              }}
              onFocus={(e) => {
                if (!fieldErrors.email) {
                  e.target.style.borderColor = 'var(--primary-green)';
                }
              }}
              onBlur={(e) => {
                if (!fieldErrors.email) {
                  e.target.style.borderColor = '#e5e7eb';
                }
              }}
            />
            {fieldErrors.email && (
              <span style={{ 
                color: '#ef4444', 
                fontSize: '0.85rem',
                marginTop: '0.25rem',
                display: 'block'
              }}>{fieldErrors.email}</span>
            )}
          </div>
          
          <div className="form-group" style={{ marginBottom: '1.5rem' }}>
            <label style={{ 
              display: 'block',
              marginBottom: '0.5rem',
              color: '#374151',
              fontWeight: '600',
              fontSize: '0.9rem'
            }}>Password</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              disabled={loading}
              className="form-input"
              placeholder="Enter your password"
              style={{
                width: '100%',
                padding: '0.75rem 1rem',
                border: fieldErrors.password ? '2px solid #ef4444' : '2px solid #e5e7eb',
                borderRadius: '8px',
                fontSize: '1rem',
                transition: 'all 0.2s',
                outline: 'none'
              }}
              onFocus={(e) => {
                if (!fieldErrors.password) {
                  e.target.style.borderColor = 'var(--primary-green)';
                }
              }}
              onBlur={(e) => {
                if (!fieldErrors.password) {
                  e.target.style.borderColor = '#e5e7eb';
                }
              }}
            />
            {fieldErrors.password && (
              <span style={{ 
                color: '#ef4444', 
                fontSize: '0.85rem',
                marginTop: '0.25rem',
                display: 'block'
              }}>{fieldErrors.password}</span>
            )}
          </div>
          
          <button 
            type="submit" 
            className="btn btn-primary btn-large"
            disabled={loading}
            style={{ 
              width: '100%',
              padding: '0.875rem',
              fontSize: '1rem',
              fontWeight: '600',
              borderRadius: '8px',
              border: 'none',
              background: loading ? '#9ca3af' : 'var(--primary-green)',
              color: 'white',
              cursor: loading ? 'not-allowed' : 'pointer',
              transition: 'all 0.2s',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '0.5rem'
            }}
          >
            {loading ? (
              <>
                <span className="spinner" style={{
                  width: '16px',
                  height: '16px',
                  border: '2px solid rgba(255,255,255,0.3)',
                  borderTopColor: 'white',
                  borderRadius: '50%',
                  animation: 'spin 0.6s linear infinite'
                }}></span>
                Signing In...
              </>
            ) : (
              'Sign In'
            )}
          </button>
          
          <div style={{ 
            marginTop: '1.5rem',
            paddingTop: '1.5rem',
            borderTop: '1px solid #e5e7eb',
            textAlign: 'center'
          }}>
            <p style={{ color: '#6b7280', fontSize: '0.9rem' }}>
              Don't have an account?{' '}
              <Link 
                to="/register" 
                style={{ 
                  color: 'var(--primary-green)', 
                  textDecoration: 'none', 
                  fontWeight: '600',
                  transition: 'all 0.2s'
                }}
                onMouseEnter={(e) => e.target.style.textDecoration = 'underline'}
                onMouseLeave={(e) => e.target.style.textDecoration = 'none'}
              >
                Register here
              </Link>
            </p>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;