import React, { useState, useEffect } from 'react';
import api from '../utils/api';

const VendorDashboard = () => {
  const [deals, setDeals] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    price: '',
    originalPrice: '',
    quantity: '',
    pickupTimeStart: '',
    pickupTimeEnd: '',
    foodType: 'South Indian',
    isJain: false,
    image: ''
  });

  useEffect(() => {
    fetchVendorDeals();
  }, []);

  const fetchVendorDeals = async () => {
    try {
      // In real app, filter by vendor ID from JWT token
      const response = await api.get('/api/deals');
      setDeals(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching deals:', error);
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const dealData = {
        ...formData,
        price: Number(formData.price),
        originalPrice: Number(formData.originalPrice),
        quantity: Number(formData.quantity),
        pickupTimeStart: new Date(formData.pickupTimeStart),
        pickupTimeEnd: new Date(formData.pickupTimeEnd),
        vendor: {
          businessName: 'Sample Restaurant', // Get from logged in vendor
          address: 'Sample Address, Bengaluru',
          location: 'Jayanagar',
          rating: 4.5
        }
      };

      await api.post('/api/deals', dealData);
      alert('Deal created successfully!');
      setShowForm(false);
      setFormData({
        title: '',
        description: '',
        price: '',
        originalPrice: '',
        quantity: '',
        pickupTimeStart: '',
        pickupTimeEnd: '',
        foodType: 'South Indian',
        isJain: false,
        image: ''
      });
      fetchVendorDeals();
    } catch (error) {
      alert('Error creating deal: ' + (error.response?.data?.message || 'Unknown error'));
    }
  };

  if (loading) {
    return <div className="loading">Loading vendor dashboard...</div>;
  }

  return (
    <div className="container">
      <div className="vendor-dashboard">
        <div className="dashboard-header">
          <h1>🏪 Vendor Dashboard</h1>
          <button 
            className="btn btn-primary"
            onClick={() => setShowForm(!showForm)}
          >
            {showForm ? '❌ Cancel' : '➕ Add New Deal'}
          </button>
        </div>

        {showForm && (
          <div className="deal-form-container">
            <h2>Create New Deal</h2>
            <form onSubmit={handleSubmit} className="deal-form">
              <div className="form-row">
                <div className="form-group">
                  <label>Deal Title</label>
                  <input
                    type="text"
                    name="title"
                    value={formData.title}
                    onChange={handleInputChange}
                    required
                    placeholder="e.g., Benne Masala Dosa"
                  />
                </div>
                <div className="form-group">
                  <label>Food Type</label>
                  <select
                    name="foodType"
                    value={formData.foodType}
                    onChange={handleInputChange}
                    required
                  >
                    <option value="South Indian">South Indian</option>
                    <option value="North Indian">North Indian</option>
                    <option value="Italian">Italian</option>
                    <option value="Chinese">Chinese</option>
                    <option value="Continental">Continental</option>
                  </select>
                </div>
              </div>

              <div className="form-group">
                <label>Description</label>
                <textarea
                  name="description"
                  value={formData.description}
                  onChange={handleInputChange}
                  required
                  placeholder="Describe your delicious food item..."
                  rows="3"
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Original Price (₹)</label>
                  <input
                    type="number"
                    name="originalPrice"
                    value={formData.originalPrice}
                    onChange={handleInputChange}
                    required
                    min="0"
                  />
                </div>
                <div className="form-group">
                  <label>Discounted Price (₹)</label>
                  <input
                    type="number"
                    name="price"
                    value={formData.price}
                    onChange={handleInputChange}
                    required
                    min="0"
                  />
                </div>
                <div className="form-group">
                  <label>Quantity Available</label>
                  <input
                    type="number"
                    name="quantity"
                    value={formData.quantity}
                    onChange={handleInputChange}
                    required
                    min="1"
                  />
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Pickup Start Time</label>
                  <input
                    type="datetime-local"
                    name="pickupTimeStart"
                    value={formData.pickupTimeStart}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div className="form-group">
                  <label>Pickup End Time</label>
                  <input
                    type="datetime-local"
                    name="pickupTimeEnd"
                    value={formData.pickupTimeEnd}
                    onChange={handleInputChange}
                    required
                  />
                </div>
              </div>

              <div className="form-group">
                <label>Image URL (optional)</label>
                <input
                  type="url"
                  name="image"
                  value={formData.image}
                  onChange={handleInputChange}
                  placeholder="https://example.com/food-image.jpg"
                />
              </div>

              <div className="checkbox-group">
                <label className="checkbox-label">
                  <input
                    type="checkbox"
                    name="isJain"
                    checked={formData.isJain}
                    onChange={handleInputChange}
                  />
                  <span>🟢 Jain Food (No onion, garlic, root vegetables)</span>
                </label>
              </div>

              <button type="submit" className="btn btn-primary btn-full">
                Create Deal
              </button>
            </form>
          </div>
        )}

        <div className="deals-section">
          <h2>Your Active Deals ({deals.length})</h2>
          {deals.length === 0 ? (
            <div className="no-deals">
              <p>No deals created yet. Create your first deal to start selling!</p>
            </div>
          ) : (
            <div className="vendor-deals-grid">
              {deals.map((deal) => (
                <div key={deal._id} className="vendor-deal-card">
                  <div className="deal-image-small">
                    {deal.image && deal.image.startsWith('http') ? (
                      <img src={deal.image} alt={deal.title} />
                    ) : (
                      <div className="placeholder-icon">🍽️</div>
                    )}
                  </div>
                  <div className="deal-details">
                    <h3>{deal.title}</h3>
                    <p className="deal-type">{deal.foodType} {deal.isJain && '• 🟢 Jain'}</p>
                    <div className="deal-pricing">
                      <span className="current">₹{deal.price}</span>
                      <span className="original">₹{deal.originalPrice}</span>
                    </div>
                    <div className="deal-stats">
                      <span className="claimed">{deal.claimed}/{deal.quantity} claimed</span>
                      <span className={`status ${deal.claimed >= deal.quantity ? 'sold-out' : 'available'}`}>
                        {deal.claimed >= deal.quantity ? 'Sold Out' : 'Available'}
                      </span>
                    </div>
                  </div>
                  <div className="deal-actions">
                    <button className="btn-icon" title="Edit">✏️</button>
                    <button className="btn-icon delete" title="Delete">🗑️</button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default VendorDashboard;