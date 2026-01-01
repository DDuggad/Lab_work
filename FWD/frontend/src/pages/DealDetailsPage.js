import React, { useState, useEffect, useCallback } from 'react';
import { useParams } from 'react-router-dom';
import api from '../utils/api';

const DealDetailsPage = () => {
  const { id } = useParams();
  const [deal, setDeal] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [claiming, setClaiming] = useState(false);

  const fetchDeal = useCallback(async () => {
    try {
      const response = await api.get(`/api/deals/${id}`);
      setDeal(response.data);
      setLoading(false);
    } catch (err) {
      setError('Failed to fetch deal details');
      setLoading(false);
    }
  }, [id]);

  useEffect(() => {
    fetchDeal();
  }, [fetchDeal]);

  const claimDeal = async () => {
    if (claiming) return;
    
    setClaiming(true);
    try {
      const response = await api.post(`/api/deals/${id}/claim`);
      setDeal(response.data.deal);
      alert('Deal claimed successfully!');
    } catch (err) {
      alert('Failed to claim deal: ' + (err.response?.data?.message || 'Unknown error'));
    }
    setClaiming(false);
  };

  const formatTime = (date) => {
    return new Date(date).toLocaleTimeString('en-US', {
      hour: 'numeric',
      minute: '2-digit',
      hour12: true
    });
  };

  if (loading) {
    return <div className="loading">Loading deal details...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  if (!deal) {
    return <div className="error">Deal not found</div>;
  }

  const isAvailable = deal.claimed < deal.quantity;

  return (
    <div className="container">
      <div style={{ maxWidth: '800px', margin: '2rem auto', background: 'white', borderRadius: '8px', overflow: 'hidden', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}>
        <div style={{ height: '300px', background: '#e9ecef', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '6rem', overflow: 'hidden' }}>
          {deal.image && deal.image.startsWith('http') ? (
            <img 
              src={deal.image} 
              alt={deal.title}
              style={{ width: '100%', height: '100%', objectFit: 'cover' }}
              onError={(e) => {
                e.target.style.display = 'none';
                e.target.nextSibling.style.display = 'flex';
              }}
            />
          ) : null}
          <div style={{ fontSize: '6rem', display: deal.image && deal.image.startsWith('http') ? 'none' : 'flex' }}>
            🍽️
          </div>
        </div>
        
        <div style={{ padding: '2rem' }}>
          <h1 style={{ marginBottom: '1rem', color: '#333' }}>{deal.title}</h1>
          
          <p style={{ fontSize: '1.1rem', color: '#666', lineHeight: '1.6', marginBottom: '2rem' }}>
            {deal.description}
          </p>
          
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '2rem', marginBottom: '2rem' }}>
            <div>
              <h3 style={{ color: '#333', marginBottom: '0.5rem' }}>Price</h3>
              <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <span style={{ fontSize: '2rem', fontWeight: 'bold', color: '#4CAF50' }}>₹{deal.price}</span>
                <span style={{ fontSize: '1.2rem', color: '#999', textDecoration: 'line-through' }}>₹{deal.originalPrice}</span>
              </div>
            </div>
            
            <div>
              <h3 style={{ color: '#333', marginBottom: '0.5rem' }}>Availability</h3>
              <p style={{ color: isAvailable ? '#4CAF50' : '#d32f2f', fontWeight: 'bold' }}>
                {deal.quantity - deal.claimed} of {deal.quantity} available
              </p>
            </div>
            
            <div>
              <h3 style={{ color: '#333', marginBottom: '0.5rem' }}>Pickup Time</h3>
              <p style={{ color: '#4CAF50', fontWeight: '500' }}>
                {formatTime(deal.pickupTimeStart)} - {formatTime(deal.pickupTimeEnd)}
              </p>
            </div>
            
            <div>
              <h3 style={{ color: '#333', marginBottom: '0.5rem' }}>Food Type</h3>
              <p style={{ color: '#666' }}>{deal.foodType}</p>
              {deal.isJain && <span style={{ background: '#4CAF50', color: 'white', padding: '0.25rem 0.5rem', borderRadius: '4px', fontSize: '0.8rem' }}>Jain</span>}
            </div>
          </div>
          
          <div style={{ background: '#f8f9fa', padding: '1.5rem', borderRadius: '8px', marginBottom: '2rem' }}>
            <h3 style={{ color: '#333', marginBottom: '1rem' }}>Vendor Information</h3>
            <div style={{ display: 'grid', gap: '0.5rem' }}>
              <p><strong>Restaurant:</strong> {deal.vendor?.businessName}</p>
              <p><strong>Location:</strong> {deal.vendor?.location}</p>
              <p><strong>Address:</strong> {deal.vendor?.address}</p>
              <p><strong>Rating:</strong> {deal.vendor?.rating} ⭐</p>
            </div>
          </div>
          
          <button 
            className="btn" 
            onClick={claimDeal}
            disabled={!isAvailable || claiming}
            style={{ 
              fontSize: '1.2rem', 
              padding: '1rem 2rem',
              backgroundColor: !isAvailable ? '#ccc' : '#4CAF50'
            }}
          >
            {claiming ? 'Claiming...' : !isAvailable ? 'Sold Out' : `Claim Deal for ₹${deal.price}`}
          </button>
        </div>
      </div>
    </div>
  );
};

export default DealDetailsPage;