import React, { useEffect } from 'react';

const DealModal = ({ deal, isOpen, onClose }) => {
  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };

    if (isOpen) {
      document.addEventListener('keydown', handleEscape);
      document.body.style.overflow = 'hidden';
    }

    return () => {
      document.removeEventListener('keydown', handleEscape);
      document.body.style.overflow = 'unset';
    };
  }, [isOpen, onClose]);

  if (!isOpen || !deal) return null;

  const formatTime = (date) => {
    return new Date(date).toLocaleTimeString('en-US', {
      hour: 'numeric',
      minute: '2-digit',
      hour12: true
    });
  };

  const calculateDiscount = () => {
    const original = deal.originalPrice || 0;
    const newP = deal.newPrice || 0;
    if (!original || !newP) return 0;
    return Math.round(((original - newP) / original) * 100);
  };

  const getRemainingQuantity = () => {
    return (deal.stockAvailable || 0) - (deal.claimed || 0);
  };

  const openGoogleMaps = () => {
    if (deal.vendor?.googleMapsLocation) {
      window.open(deal.vendor.googleMapsLocation, '_blank');
    } else {
      const location = `${deal.vendor?.restaurantName}, ${deal.vendor?.address}, ${deal.vendor?.location}, Bangalore`;
      const mapsUrl = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(location)}`;
      window.open(mapsUrl, '_blank');
    }
  };

  const discountPercentage = calculateDiscount();
  const remainingQuantity = getRemainingQuantity();

  return (
    <div 
      className="modal-overlay" 
      onClick={onClose}
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        background: 'rgba(0, 0, 0, 0.7)',
        backdropFilter: 'blur(5px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 9999,
        padding: '1rem',
        overflowY: 'auto'
      }}
    >
      <div 
        className="modal-content" 
        onClick={(e) => e.stopPropagation()}
        style={{
          position: 'relative',
          background: 'white',
          borderRadius: '16px',
          maxWidth: '700px',
          width: '100%',
          margin: 'auto',
          boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
          animation: 'slideUp 0.3s ease'
        }}
      >
        {/* Close Button */}
        <button 
          className="modal-close" 
          onClick={onClose} 
          aria-label="Close modal"
          style={{
            position: 'absolute',
            top: '1rem',
            right: '1rem',
            background: 'white',
            border: 'none',
            borderRadius: '50%',
            width: '40px',
            height: '40px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            cursor: 'pointer',
            fontSize: '1.5rem',
            color: '#6b7280',
            boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
            zIndex: 10,
            transition: 'all 0.3s ease'
          }}
          onMouseEnter={(e) => {
            e.target.style.background = '#f3f4f6';
            e.target.style.transform = 'scale(1.1)';
          }}
          onMouseLeave={(e) => {
            e.target.style.background = 'white';
            e.target.style.transform = 'scale(1)';
          }}
        >
          ✕
        </button>

        {/* Modal Header with Image */}
        <div className="modal-header" style={{ position: 'relative' }}>
          <div className="modal-image-container" style={{ width: '100%', height: '300px', overflow: 'hidden', borderRadius: '16px 16px 0 0' }}>
            {deal.image && deal.image.startsWith('http') ? (
              <img 
                src={deal.image} 
                alt={deal.itemName || 'Deal'}
                className="modal-image"
                style={{ width: '100%', height: '100%', objectFit: 'cover' }}
              />
            ) : (
              <div className="modal-image-placeholder" style={{ width: '100%', height: '100%', background: '#f3f4f6', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <span className="food-emoji-large" style={{ fontSize: '6rem' }}>🍽️</span>
              </div>
            )}
            
            {/* Badges */}
            {discountPercentage > 0 && (
              <div className="modal-discount-badge" style={{ position: 'absolute', top: '1rem', left: '1rem', background: '#dc2626', color: 'white', padding: '0.75rem 1.25rem', borderRadius: '25px', fontWeight: '700', fontSize: '1.125rem' }}>
                {discountPercentage}% OFF
              </div>
            )}
          </div>
        </div>

        {/* Modal Body */}
        <div className="modal-body" style={{ padding: '2rem' }}>
          {/* Title and Description */}
          <div className="modal-title-section" style={{ marginBottom: '1.5rem' }}>
            <h2 className="modal-title" style={{ fontSize: '2rem', fontWeight: '800', color: '#064e3b', marginBottom: '0.75rem' }}>{deal.itemName || 'Delicious Food'}</h2>
            <p className="modal-description" style={{ fontSize: '1rem', color: '#6b7280', lineHeight: '1.6' }}>{deal.description || 'Fresh and delicious food available at great prices!'}</p>
          </div>

          {/* Price Section */}
          <div className="modal-price-section" style={{ padding: '1.5rem', background: '#f0fdf4', borderRadius: '12px', marginBottom: '1.5rem' }}>
            <div className="price-display" style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '0.5rem' }}>
              <span className="modal-current-price" style={{ fontSize: '2.5rem', fontWeight: '800', color: '#10b981' }}>₹{deal.newPrice}</span>
              {deal.originalPrice && deal.originalPrice > deal.newPrice && (
                <span className="modal-original-price" style={{ fontSize: '1.5rem', color: '#9ca3af', textDecoration: 'line-through' }}>₹{deal.originalPrice}</span>
              )}
            </div>
            <div className="savings-info">
              {discountPercentage > 0 && (
                <span className="savings-text" style={{ color: '#059669', fontWeight: '600', fontSize: '1rem' }}>You save ₹{(deal.originalPrice - deal.newPrice).toFixed(0)}!</span>
              )}
            </div>
          </div>

          {/* Deal Info Grid */}
          <div className="modal-info-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '1.5rem' }}>
            <div className="info-item" style={{ display: 'flex', gap: '0.75rem', padding: '1rem', background: '#f9fafb', borderRadius: '8px' }}>
              <span className="info-icon" style={{ fontSize: '1.5rem' }}>⏰</span>
              <div className="info-content">
                <h4 style={{ fontSize: '0.875rem', fontWeight: '600', color: '#6b7280', marginBottom: '0.25rem' }}>Pickup Time</h4>
                <p style={{ fontSize: '1rem', fontWeight: '600', color: '#064e3b' }}>{formatTime(deal.dealStartTime)} - {formatTime(deal.dealEndTime)}</p>
              </div>
            </div>

            <div className="info-item" style={{ display: 'flex', gap: '0.75rem', padding: '1rem', background: '#f9fafb', borderRadius: '8px' }}>
              <span className="info-icon" style={{ fontSize: '1.5rem' }}>📦</span>
              <div className="info-content">
                <h4 style={{ fontSize: '0.875rem', fontWeight: '600', color: '#6b7280', marginBottom: '0.25rem' }}>Available</h4>
                <p style={{ fontSize: '1rem', fontWeight: '600', color: '#064e3b' }}>{remainingQuantity} items left</p>
              </div>
            </div>

            <div className="info-item" style={{ display: 'flex', gap: '0.75rem', padding: '1rem', background: '#f9fafb', borderRadius: '8px' }}>
              <span className="info-icon" style={{ fontSize: '1.5rem' }}>🍽️</span>
              <div className="info-content">
                <h4 style={{ fontSize: '0.875rem', fontWeight: '600', color: '#6b7280', marginBottom: '0.25rem' }}>Food Type</h4>
                <p style={{ fontSize: '1rem', fontWeight: '600', color: '#064e3b' }}>{deal.foodType}</p>
              </div>
            </div>

            {deal.vendor?.rating > 0 && (
              <div className="info-item" style={{ display: 'flex', gap: '0.75rem', padding: '1rem', background: '#f9fafb', borderRadius: '8px' }}>
                <span className="info-icon" style={{ fontSize: '1.5rem' }}>⭐</span>
                <div className="info-content">
                  <h4 style={{ fontSize: '0.875rem', fontWeight: '600', color: '#6b7280', marginBottom: '0.25rem' }}>Rating</h4>
                  <p style={{ fontSize: '1rem', fontWeight: '600', color: '#064e3b' }}>{deal.vendor.rating.toFixed(1)}</p>
                </div>
              </div>
            )}
          </div>

          {/* Vendor Information */}
          <div className="modal-vendor-section" style={{ marginBottom: '1.5rem' }}>
            <h3 style={{ fontSize: '1.25rem', fontWeight: '700', color: '#064e3b', marginBottom: '1rem' }}>Restaurant Information</h3>
            <div className="vendor-card" style={{ padding: '1.5rem', background: '#f9fafb', borderRadius: '12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div className="vendor-main-info">
                <h4 style={{ fontSize: '1.125rem', fontWeight: '700', color: '#064e3b', marginBottom: '0.5rem' }}>{deal.vendor?.restaurantName}</h4>
                <p className="vendor-location" style={{ color: '#6b7280', marginBottom: '0.25rem' }}>📍 {deal.vendor?.location}</p>
                <p style={{ color: '#6b7280', fontSize: '0.875rem' }}>{deal.vendor?.address}</p>
              </div>
              <button 
                className="maps-button"
                onClick={openGoogleMaps}
                title="Open in Google Maps"
                style={{
                  padding: '0.75rem 1.5rem',
                  background: '#10b981',
                  color: 'white',
                  border: 'none',
                  borderRadius: '8px',
                  fontWeight: '600',
                  cursor: 'pointer',
                  fontSize: '0.875rem',
                  transition: 'background 0.3s ease'
                }}
                onMouseEnter={(e) => e.target.style.background = '#059669'}
                onMouseLeave={(e) => e.target.style.background = '#10b981'}
              >
                🗺️ Directions
              </button>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="modal-actions" style={{ display: 'flex', gap: '1rem' }}>
            {deal.vendor?.phoneNumber && (
              <a 
                href={`tel:${deal.vendor.phoneNumber}`}
                style={{
                  flex: 1,
                  padding: '1rem',
                  background: '#10b981',
                  color: 'white',
                  border: 'none',
                  borderRadius: '8px',
                  fontWeight: '700',
                  fontSize: '1rem',
                  cursor: 'pointer',
                  textAlign: 'center',
                  textDecoration: 'none',
                  transition: 'background 0.3s ease'
                }}
                onMouseEnter={(e) => e.target.style.background = '#059669'}
                onMouseLeave={(e) => e.target.style.background = '#10b981'}
              >
                📞 Call Restaurant
              </a>
            )}
            <button 
              onClick={onClose}
              style={{
                flex: 1,
                padding: '1rem',
                background: '#f3f4f6',
                color: '#374151',
                border: 'none',
                borderRadius: '8px',
                fontWeight: '600',
                fontSize: '1rem',
                cursor: 'pointer',
                transition: 'background 0.3s ease'
              }}
              onMouseEnter={(e) => e.target.style.background = '#e5e7eb'}
              onMouseLeave={(e) => e.target.style.background = '#f3f4f6'}
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DealModal;