import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';
import '../styles/theme.css';

const RegisterPage = () => {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [formData, setFormData] = useState({
    username: '',
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
      const response = await axios.post('/api/auth/register', formData);
      
      // Use AuthContext login method to set user state
      login(response.data.user, response.data.token);
      
      // Redirect to vendor profile form to complete registration
      navigate('/vendor/profile');
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed');
    }
    
    setLoading(false);
  };

  return (
    <div className="container">
      <div className="animate-fade-in" style={{ maxWidth: '500px', margin: '3rem auto', background: 'white', padding: '3rem', borderRadius: '16px', boxShadow: '0 10px 30px rgba(0,0,0,0.1)' }}>
        <h2 style={{ textAlign: 'center', marginBottom: '0.5rem', color: '#333', fontSize: '2rem' }}>
          Vendor Registration
        </h2>
        <p style={{ textAlign: 'center', color: '#666', marginBottom: '2rem' }}>
          Join FreshBites and start offering deals
        </p>
        
        {error && (
          <div className="alert alert-error animate-slide-down">
            {error}
          </div>
        )}
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Username:</label>
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
              required
              minLength="3"
              className="form-input"
              placeholder="Enter username"
            />
          </div>
          
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
              minLength="6"
              className="form-input"
              placeholder="Minimum 6 characters"
            />
          </div>
          
          <button 
            type="submit" 
            className="btn btn-primary btn-large"
            disabled={loading}
            style={{ width: '100%' }}
          >
            {loading ? <><span className="spinner"></span> Registering...</> : 'Register as Vendor'}
          </button>
          
          <p style={{ textAlign: 'center', marginTop: '1.5rem', color: '#666' }}>
            Already have an account? <Link to="/login" style={{ color: 'var(--primary-green)', textDecoration: 'none', fontWeight: '600' }}>Login here</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default RegisterPage;