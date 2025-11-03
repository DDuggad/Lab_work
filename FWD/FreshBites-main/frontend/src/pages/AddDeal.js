import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';
import '../styles/AddDeal.css';

const AddDeal = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const [formData, setFormData] = useState({
    itemName: '',
    description: '',
    originalPrice: '',
    newPrice: '',
    stockAvailable: '',
    dealStartTime: '',
    dealEndTime: '',
    image: '',
    foodType: 'Pure Veg'
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setSuccess('');

    try {
      const token = localStorage.getItem('token');
      
      const dealData = {
        ...formData,
        originalPrice: parseFloat(formData.originalPrice),
        newPrice: parseFloat(formData.newPrice),
        stockAvailable: parseInt(formData.stockAvailable),
        vendor: {
          restaurantName: user.restaurantName,
          address: user.address,
          location: user.location,
          phoneNumber: user.phoneNumber,
          googleMapsLocation: user.googleMapsLocation || '',
          rating: user.rating || 0
        }
      };

      await axios.post('/api/deals', dealData, {
        headers: { Authorization: `Bearer ${token}` }
      });

      setSuccess('Deal created successfully!');
      setTimeout(() => {
        navigate('/vendor/manage-deals');
      }, 1500);
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to create deal');
    } finally {
      setLoading(false);
    }
  };

  const calculateDiscount = () => {
    const original = parseFloat(formData.originalPrice);
    const newPrice = parseFloat(formData.newPrice);
    if (original && newPrice && original > newPrice) {
      return Math.round(((original - newPrice) / original) * 100);
    }
    return 0;
  };

  return (
    <div className="add-deal-container">
      <div className="add-deal-card animate-fade-in">
        <div className="deal-header">
          <h1>➕ Add New Deal</h1>
          <p>Create an exciting deal for your customers</p>
        </div>

        {error && <div className="alert alert-error animate-slide-down">{error}</div>}
        {success && <div className="alert alert-success animate-slide-down">{success}</div>}

        <form onSubmit={handleSubmit} className="deal-form">
          <div className="form-row">
            <div className="form-group">
              <label htmlFor="itemName">Item Name *</label>
              <input
                type="text"
                id="itemName"
                name="itemName"
                value={formData.itemName}
                onChange={handleChange}
                required
                placeholder="e.g., Masala Dosa Combo"
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label htmlFor="foodType">Food Type *</label>
              <select
                id="foodType"
                name="foodType"
                value={formData.foodType}
                onChange={handleChange}
                required
                className="form-select"
              >
                <option value="Pure Veg">Pure Veg</option>
                <option value="South Indian">South Indian</option>
                <option value="North Indian">North Indian</option>
                <option value="Italian">Italian</option>
                <option value="Chinese">Chinese</option>
                <option value="Continental">Continental</option>
                <option value="Multi-Cuisine">Multi-Cuisine</option>
              </select>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="description">Description</label>
            <textarea
              id="description"
              name="description"
              value={formData.description}
              onChange={handleChange}
              rows="3"
              placeholder="Brief description of the deal..."
              className="form-textarea"
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="originalPrice">Original Price (₹) *</label>
              <input
                type="number"
                id="originalPrice"
                name="originalPrice"
                value={formData.originalPrice}
                onChange={handleChange}
                required
                min="0"
                step="0.01"
                placeholder="100"
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label htmlFor="newPrice">Deal Price (₹) *</label>
              <input
                type="number"
                id="newPrice"
                name="newPrice"
                value={formData.newPrice}
                onChange={handleChange}
                required
                min="0"
                step="0.01"
                placeholder="70"
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label>Discount</label>
              <div className="discount-badge">{calculateDiscount()}% OFF</div>
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="stockAvailable">Stock Available *</label>
              <input
                type="number"
                id="stockAvailable"
                name="stockAvailable"
                value={formData.stockAvailable}
                onChange={handleChange}
                required
                min="1"
                placeholder="50"
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label htmlFor="dealStartTime">Deal Start Time *</label>
              <input
                type="datetime-local"
                id="dealStartTime"
                name="dealStartTime"
                value={formData.dealStartTime}
                onChange={handleChange}
                required
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label htmlFor="dealEndTime">Deal End Time *</label>
              <input
                type="datetime-local"
                id="dealEndTime"
                name="dealEndTime"
                value={formData.dealEndTime}
                onChange={handleChange}
                required
                className="form-input"
              />
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="image">Image URL</label>
            <input
              type="url"
              id="image"
              name="image"
              value={formData.image}
              onChange={handleChange}
              placeholder="https://example.com/food-image.jpg"
              className="form-input"
            />
            {formData.image && (
              <div className="image-preview">
                <img src={formData.image} alt="Deal Preview" onError={(e) => e.target.style.display = 'none'} />
              </div>
            )}
          </div>

          <div className="form-actions">
            <button 
              type="button" 
              className="btn btn-secondary" 
              onClick={() => navigate('/vendor/manage-deals')}
              disabled={loading}
            >
              Cancel
            </button>
            <button type="submit" className="btn btn-primary btn-large" disabled={loading}>
              {loading ? <><span className="spinner"></span> Creating...</> : 'Create Deal'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AddDeal;
