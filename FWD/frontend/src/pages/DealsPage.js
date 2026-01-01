import React, { useState, useEffect } from 'react';
import api from '../utils/api';
import DealCard from '../components/DealCard';
import DealModal from '../components/DealModal';

const DealsPage = () => {
  const [deals, setDeals] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredDeals, setFilteredDeals] = useState([]);
  const [selectedDeal, setSelectedDeal] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    fetchDeals();
  }, []);

  useEffect(() => {
    // Filter deals based on search term
    if (searchTerm.trim() === '') {
      setFilteredDeals(deals);
    } else {
      const filtered = deals.filter(deal => {
        const itemName = deal.itemName || '';
        const description = deal.description || '';
        const restaurantName = deal.vendor?.restaurantName || '';
        const location = deal.vendor?.location || '';
        const searchLower = searchTerm.toLowerCase();
        
        return itemName.toLowerCase().includes(searchLower) ||
               description.toLowerCase().includes(searchLower) ||
               restaurantName.toLowerCase().includes(searchLower) ||
               location.toLowerCase().includes(searchLower);
      });
      setFilteredDeals(filtered);
    }
  }, [deals, searchTerm]);

  const fetchDeals = async () => {
    try {
      const response = await api.get('/api/deals');
      setDeals(response.data);
      setLoading(false);
    } catch (err) {
      setError('Failed to fetch deals');
      setLoading(false);
    }
  };

  const openModal = (deal) => {
    setSelectedDeal(deal);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setSelectedDeal(null);
  };

  if (loading) {
    return (
      <div className="page-container">
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Loading delicious deals...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="page-container">
        <div className="error-container">
          <h2>Oops! Something went wrong</h2>
          <p>{error}</p>
          <button className="btn btn-primary" onClick={fetchDeals}>
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="page-container">
      <div className="container">
        {/* Header Section */}
        <div className="deals-header">
          <h1 className="page-title">
            Today's Surplus Deals
            <span className="text-gradient">Fresh & Affordable</span>
          </h1>
          <p className="page-subtitle">
            Discover amazing food deals from local restaurants in Bangalore. 
            Help reduce food waste while enjoying delicious meals at unbeatable prices.
          </p>
        </div>

        {/* Search and Filter Section */}
        <div style={{ marginBottom: '2rem' }}>
          <div style={{ maxWidth: '600px', margin: '0 auto' }}>
            <div style={{ 
              display: 'flex', 
              alignItems: 'center', 
              gap: '0.75rem',
              padding: '0.875rem 1.25rem',
              background: 'white',
              border: '2px solid #10b981',
              borderRadius: '50px',
              boxShadow: '0 2px 8px rgba(16, 185, 129, 0.1)',
              transition: 'all 0.3s ease'
            }}>
              <span style={{ fontSize: '1.25rem', color: '#10b981' }}>🔍</span>
              <input
                type="text"
                placeholder="Search for restaurants, dishes, or locations..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                style={{
                  flex: 1,
                  border: 'none',
                  outline: 'none',
                  fontSize: '1rem',
                  color: '#374151',
                  background: 'transparent'
                }}
              />
            </div>
          </div>
        </div>

        {/* Results Section */}
        {filteredDeals.length === 0 ? (
          <div className="no-deals-container">
            <div className="no-deals-content">
              <div className="no-deals-icon">📭</div>
              <h2>No Deals Found</h2>
              <p>
                {searchTerm 
                  ? "Try adjusting your search terms or check back later for new deals!"
                  : "No deals available at the moment. Check back later for fresh deals!"
                }
              </p>
              {searchTerm && (
                <button 
                  className="btn btn-outline" 
                  onClick={() => setSearchTerm('')}
                >
                  Clear Search
                </button>
              )}
            </div>
          </div>
        ) : (
          <>
            <div className="deals-count">
              <p>
                {filteredDeals.length === deals.length 
                  ? `${deals.length} deals available`
                  : `${filteredDeals.length} of ${deals.length} deals`
                }
              </p>
            </div>
            
            <div className="deals-grid grid grid-4">
              {filteredDeals.map((deal, index) => (
                <div 
                  key={deal._id || deal.id} 
                  className="deal-item fade-in"
                  style={{ animationDelay: `${index * 100}ms` }}
                >
                  <DealCard deal={deal} onOpenModal={openModal} />
                </div>
              ))}
            </div>
          </>
        )}
      </div>

      {/* Deal Modal */}
      <DealModal 
        deal={selectedDeal}
        isOpen={isModalOpen}
        onClose={closeModal}
      />
    </div>
  );
};

export default DealsPage;