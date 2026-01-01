import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import api from '../utils/api';
import '../styles/VendorProfile.css';
import '../styles/theme.css';

const VendorProfile = () => {
  const { user, updateUser } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  
  const [formData, setFormData] = useState({
    restaurantName: '',
    location: '',
    address: '',
    phoneNumber: '',
    restaurantImage: '',
    googleMapsLocation: ''
  });

  useEffect(() => {
    if (user && user.profileCompleted) {
      setFormData({
        restaurantName: user.restaurantName || '',
        location: user.location || '',
        address: user.address || '',
        phoneNumber: user.phoneNumber || '',
        restaurantImage: user.restaurantImage || '',
        googleMapsLocation: user.googleMapsLocation || ''
      });
    }
  }, [user]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setSuccess('');

    try {
      const token = localStorage.getItem('token');
      const response = await api.put(
        '/api/auth/profile',
        formData,
        { headers: { Authorization: `Bearer ${token}` } }
      );

      updateUser(response.data.user);
      setSuccess('Profile updated successfully!');
      
      setTimeout(() => {
        navigate('/vendor/manage-deals');
      }, 1500);
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to update profile');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="vendor-profile-container">
      <div className="vendor-profile-card">
        <div className="profile-header">
          <h1>Restaurant Profile</h1>
          <p>{user?.profileCompleted ? 'Update your restaurant details' : 'Complete your restaurant profile to start managing deals'}</p>
        </div>

        {error && <div className="alert alert-error">{error}</div>}
        {success && <div className="alert alert-success">{success}</div>}

        <form onSubmit={handleSubmit} className="profile-form">
          <div className="profile-step-indicator">
            <div className="step active"></div>
            <div className="step active"></div>
            <div className="step"></div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="restaurantName">
                Restaurant Name <span className="required-asterisk">*</span>
              </label>
              <input
                type="text"
                id="restaurantName"
                name="restaurantName"
                value={formData.restaurantName}
                onChange={handleChange}
                required
                className="form-input"
                placeholder="Enter your restaurant name"
              />
            </div>

            <div className="form-group">
              <label htmlFor="location">
                Location <span className="required-asterisk">*</span>
              </label>
              <select
                id="location"
                name="location"
                value={formData.location}
                onChange={handleChange}
                required
                className="form-select"
              >
                <option value="">Select location</option>
                <option value="Basavanagudi">Basavanagudi</option>
                <option value="Jayanagar">Jayanagar</option>
                <option value="Rajajinagar">Rajajinagar</option>
                <option value="Hanumanth Nagar">Hanumanth Nagar</option>
                <option value="Malleshwaram">Malleshwaram</option>
                <option value="Indiranagar">Indiranagar</option>
                <option value="Koramangala">Koramangala</option>
                <option value="BTM Layout">BTM Layout</option>
              </select>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="address">
              Full Address <span className="required-asterisk">*</span>
            </label>
            <textarea
              id="address"
              name="address"
              value={formData.address}
              onChange={handleChange}
              required
              rows="3"
              className="form-textarea"
              placeholder="Enter complete address with landmarks"
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="phoneNumber">
                Phone Number <span className="required-asterisk">*</span>
              </label>
              <input
                type="tel"
                id="phoneNumber"
                name="phoneNumber"
                value={formData.phoneNumber}
                onChange={handleChange}
                required
                pattern="[0-9]{10}"
                className="form-input"
                placeholder="10-digit phone number"
              />
            </div>

            <div className="form-group">
              <label htmlFor="restaurantImage">Restaurant Image URL</label>
              <input
                type="url"
                id="restaurantImage"
                name="restaurantImage"
                value={formData.restaurantImage}
                onChange={handleChange}
                className="form-input"
                placeholder="https://example.com/image.jpg"
              />
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="googleMapsLocation">
              Google Maps Location URL
              <small style={{ display: 'block', color: '#6b7280', fontWeight: 'normal', marginTop: '0.25rem' }}>
                Example: https://maps.google.com/?q=Your+Restaurant+Name+Location
              </small>
            </label>
            <input
              type="url"
              id="googleMapsLocation"
              name="googleMapsLocation"
              value={formData.googleMapsLocation}
              onChange={handleChange}
              className="form-input"
              placeholder="https://maps.google.com/?q=Your+Restaurant+Bangalore"
              pattern="https://maps\.google\.com/.*|https://www\.google\.com/maps/.*|https://goo\.gl/maps/.*"
              title="Please enter a valid Google Maps URL (e.g., https://maps.google.com/?q=...)"
            />
          </div>

          <div className="form-actions">
            <button type="submit" className="btn btn-primary btn-profile" disabled={loading}>
              {loading ? (
                <>
                  <span className="spinner"></span> Saving...
                </>
              ) : (
                user?.profileCompleted ? 'Update Profile' : 'Complete Profile & Continue'
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default VendorProfile;