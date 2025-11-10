import React, { useState, useEffect } from 'react';
import axios from 'axios';
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
      const filtered = deals.filter(deal =>
        deal.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        deal.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
        deal.vendor?.businessName.toLowerCase().includes(searchTerm.toLowerCase())
      );
      setFilteredDeals(filtered);
    }
  }, [deals, searchTerm]);

  const fetchDeals = async () => {
    try {
      const response = await axios.get('/api/deals');
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
        <div className="deals-filters">
          <div className="search-container">
            <div className="search-box">
              <span className="search-icon">⌕</span>
              <input
                type="text"
                placeholder="Search for restaurants, dishes, or locations..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="search-input"
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