import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import api from '../utils/api';
import '../styles/ManageDeals.css';

const ManageDeals = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [deals, setDeals] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [editingDeal, setEditingDeal] = useState(null);

  useEffect(() => {
    if (user && user.id) {
      fetchDeals();
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [user]);

  const fetchDeals = async () => {
    if (!user || !user.id) {
      setError('User not authenticated');
      setLoading(false);
      return;
    }

    try {
      const token = localStorage.getItem('token');
      console.log('Fetching deals for user ID:', user.id);
      console.log('Token:', token ? 'Present' : 'Missing');
      
      const response = await api.get(`/api/deals/vendor/${user.id}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      
      console.log('API Response:', response.data);
      setDeals(response.data.deals || []);
    } catch (err) {
      console.error('Error fetching deals:', err);
      setError(`Failed to load deals: ${err.response?.data?.message || err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (dealId) => {
    if (!window.confirm('Are you sure you want to delete this deal?')) return;

    try {
      const token = localStorage.getItem('token');
      await api.delete(`/api/deals/${dealId}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setDeals(deals.filter(deal => deal._id !== dealId));
    } catch (err) {
      alert('Failed to delete deal');
    }
  };

  const handleUpdateStock = async (dealId, newStock) => {
    try {
      const token = localStorage.getItem('token');
      const response = await api.put(
        `/api/deals/${dealId}`,
        { stockAvailable: parseInt(newStock) },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      const updatedDeal = response.data.deal || response.data;
      setDeals(deals.map(deal => deal._id === dealId ? updatedDeal : deal));
      setEditingDeal(null);
    } catch (err) {
      console.error('Failed to update stock:', err);
      alert('Failed to update stock: ' + (err.response?.data?.message || err.message));
    }
  };

  const toggleDealStatus = async (dealId, currentStatus) => {
    try {
      const token = localStorage.getItem('token');
      const response = await api.put(
        `/api/deals/${dealId}`,
        { isActive: !currentStatus },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      const updatedDeal = response.data.deal || response.data;
      setDeals(deals.map(deal => deal._id === dealId ? updatedDeal : deal));
    } catch (err) {
      console.error('Failed to update deal status:', err);
      alert('Failed to update deal status: ' + (err.response?.data?.message || err.message));
    }
  };

  const formatDate = (date) => {
    return new Date(date).toLocaleString('en-IN', {
      day: '2-digit',
      month: 'short',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getStockStatus = (deal) => {
    const available = deal.stockAvailable - deal.claimed;
    const percentage = (available / deal.stockAvailable) * 100;
    if (percentage > 50) return 'stock-good';
    if (percentage > 20) return 'stock-medium';
    return 'stock-low';
  };

  if (loading) {
    return <div className="loading-spinner"><div className="spinner large"></div></div>;
  }

  return (
    <div className="manage-deals-container">
      <div className="manage-header">
        <div>
          <h1>Manage Deals</h1>
          <p>Track and update your active deals</p>
        </div>
        <button className="btn btn-primary" onClick={() => navigate('/vendor/add-deal')}>
          Add New Deal
        </button>
      </div>

      {error && <div className="alert alert-error">{error}</div>}

      {deals.length === 0 ? (
        <div className="empty-state">
          <div className="empty-icon">�</div>
          <h2>No Deals Yet</h2>
          <p>Create your first deal to start selling!</p>
          <button className="btn btn-primary" onClick={() => navigate('/vendor/add-deal')}>
            Create First Deal
          </button>
        </div>
      ) : (
        <div className="deals-grid">
          {deals.map((deal) => {
            const availableStock = deal.stockAvailable - deal.claimed;
            const isExpired = new Date(deal.dealEndTime) < new Date();
            
            return (
              <div key={deal._id} className={`deal-card ${!deal.isActive ? 'inactive' : ''} ${isExpired ? 'expired' : ''}`}>
                <div className="deal-image">
                  {deal.image ? (
                    <img src={deal.image} alt={deal.itemName} />
                  ) : (
                    <div className="placeholder-image">🍽</div>
                  )}
                  <div className="deal-badges">
                    {deal.isActive && !isExpired ? (
                      <span className="badge badge-success">Active</span>
                    ) : isExpired ? (
                      <span className="badge badge-expired">Expired</span>
                    ) : (
                      <span className="badge badge-inactive">Inactive</span>
                    )}
                    <span className="badge badge-discount">{deal.discountPercentage}% OFF</span>
                  </div>
                </div>

                <div className="deal-content">
                  <h3>{deal.itemName}</h3>
                  <p className="deal-description">{deal.description || 'No description'}</p>

                  <div className="price-row">
                    <div className="prices">
                      <span className="original-price">₹{deal.originalPrice}</span>
                      <span className="new-price">₹{deal.newPrice}</span>
                    </div>
                    <span className="food-type">{deal.foodType}</span>
                  </div>

                  <div className="deal-stats">
                    <div className={`stock-info ${getStockStatus(deal)}`}>
                      <span className="stock-label">Stock:</span>
                      {editingDeal === deal._id ? (
                        <input
                          type="number"
                          className="stock-input"
                          defaultValue={deal.stockAvailable}
                          onBlur={(e) => handleUpdateStock(deal._id, e.target.value)}
                          onKeyPress={(e) => e.key === 'Enter' && e.target.blur()}
                          autoFocus
                          min="0"
                        />
                      ) : (
                        <span 
                          className="stock-value"
                          onClick={() => setEditingDeal(deal._id)}
                          title="Click to edit"
                        >
                          {availableStock} / {deal.stockAvailable}
                        </span>
                      )}
                    </div>
                    <div className="claimed-info">
                      <span className="claimed-label">Claimed:</span>
                      <span className="claimed-value">{deal.claimed}</span>
                    </div>
                  </div>

                  <div className="deal-time">
                    <div>
                      <small>Starts:</small> {formatDate(deal.dealStartTime)}
                    </div>
                    <div>
                      <small>Ends:</small> {formatDate(deal.dealEndTime)}
                    </div>
                  </div>

                  <div className="deal-actions">
                    <button
                      className={`btn btn-sm ${deal.isActive ? 'btn-warning' : 'btn-success'}`}
                      onClick={() => toggleDealStatus(deal._id, deal.isActive)}
                      disabled={isExpired}
                    >
                      {deal.isActive ? 'Pause' : 'Activate'}
                    </button>
                    <button
                      className="btn btn-sm btn-secondary"
                      onClick={() => setEditingDeal(deal._id === editingDeal ? null : deal._id)}
                    >
                      Edit Stock
                    </button>
                    <button
                      className="btn btn-sm btn-danger"
                      onClick={() => handleDelete(deal._id)}
                    >
                      Delete
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default ManageDeals;
