import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import axios from 'axios';
import '../styles/theme.css';

const LoginPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await axios.post('/api/auth/login', formData);
      
      // Store token and user info
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
      
      // Redirect based on profile completion
      if (response.data.user.profileCompleted) {
        navigate('/vendor/manage-deals');
      } else {
        navigate('/vendor/profile');
      }
    } catch (err) {
      setError(err.response?.data?.message || 'Login failed');
    }
    
    setLoading(false);
  };

  return (
    <div className="container">
      <div style={{ maxWidth: '400px', margin: '2rem auto', background: 'white', padding: '2rem', borderRadius: '12px', boxShadow: 'var(--shadow-md)' }} className="animate-fade-in">
        <h2 style={{ textAlign: 'center', marginBottom: '0.5rem', color: 'var(--primary-green)', fontSize: '2rem' }}>🔑 Vendor Login</h2>
        <p style={{ textAlign: 'center', marginBottom: '2rem', color: '#666' }}>Access your vendor dashboard</p>
        
        {error && (
          <div className="alert alert-error animate-slide-down">
            {error}
          </div>
        )}
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Email:</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              className="form-input"
              placeholder="your@email.com"
            />
          </div>
          
          <div className="form-group">
            <label>Password:</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              className="form-input"
              placeholder="Enter your password"
            />
          </div>
          
          <button 
            type="submit" 
            className="btn btn-primary btn-large"
            disabled={loading}
            style={{ width: '100%' }}
          >
            {loading ? <><span className="spinner"></span> Logging in...</> : 'Login'}
          </button>
          
          <p style={{ textAlign: 'center', marginTop: '1.5rem', color: '#666' }}>
            Don't have an account? <Link to="/register" style={{ color: 'var(--primary-green)', textDecoration: 'none', fontWeight: '600' }}>Register here</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;