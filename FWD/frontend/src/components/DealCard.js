import React from 'react';

const DealCard = ({ deal, onOpenModal }) => {
  // Safety check for deal object
  if (!deal) return null;

  const formatTime = (date) => {
    if (!date) return 'N/A';
    try {
      return new Date(date).toLocaleTimeString('en-US', {
        hour: 'numeric',
        minute: '2-digit',
        hour12: true
      });
    } catch (e) {
      return 'N/A';
    }
  };

  const calculateDiscount = () => {
    const original = deal.originalPrice || 0;
    const newP = deal.newPrice || 0;
    if (!original || !newP || original <= newP) return 0;
    return Math.round(((original - newP) / original) * 100);
  };

  const getRemainingQuantity = () => {
    return Math.max(0, (deal.stockAvailable || 0) - (deal.claimed || 0));
  };

  const handleImageError = (e) => {
    e.target.style.display = 'none';
    const placeholder = e.target.nextSibling;
    if (placeholder) {
      placeholder.style.display = 'flex';
    }
  };

  const handleCardClick = (e) => {
    if (e.target.tagName === 'A' || e.target.tagName === 'BUTTON' || e.target.closest('a, button')) {
      return;
    }
    if (onOpenModal) {
      onOpenModal(deal);
    }
  };

  const handleImageClick = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (onOpenModal) {
      onOpenModal(deal);
    }
  };

  const discountPercentage = calculateDiscount();
  const remainingQuantity = getRemainingQuantity();

  return (
    <div className="deal-card-modern" onClick={handleCardClick} style={{ cursor: 'pointer', background: 'white', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0,0,0,0.1)', overflow: 'hidden', transition: 'transform 0.3s ease, box-shadow 0.3s ease' }}>
      {/* Image Section */}
      <div className="deal-image-container" onClick={handleImageClick} style={{ position: 'relative', width: '100%', height: '200px', overflow: 'hidden' }}>
        {deal.image && deal.image.startsWith('http') ? (
          <>
            <img 
              src={deal.image} 
              alt={deal.itemName || 'Deal'}
              className="deal-image clickable-image"
              onError={handleImageError}
              style={{ display: 'block', width: '100%', height: '100%', objectFit: 'cover' }}
            />
            <div className="deal-image-placeholder" style={{ display: 'none', width: '100%', height: '100%', background: '#f3f4f6', alignItems: 'center', justifyContent: 'center' }}>
              <span className="food-placeholder" style={{ fontSize: '2rem', color: '#9CA3AF' }}>🍽</span>
            </div>
          </>
        ) : (
          <div className="deal-image-placeholder clickable-image" style={{ width: '100%', height: '100%', background: '#f3f4f6', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <span className="food-placeholder" style={{ fontSize: '2rem', color: '#9CA3AF' }}>🍽</span>
          </div>
        )}
        
        {/* Discount Badge */}
        {discountPercentage > 0 && (
          <div className="discount-badge" style={{ position: 'absolute', top: '10px', right: '10px', background: '#dc2626', color: 'white', padding: '0.5rem 1rem', borderRadius: '20px', fontWeight: '700', fontSize: '0.875rem' }}>
            {discountPercentage}% OFF
          </div>
        )}
      </div>

      {/* Content Section */}
      <div className="deal-content-modern" style={{ padding: '1.25rem' }}>
        {/* Title */}
        <h3 className="deal-title-modern clickable-title" onClick={handleImageClick} style={{ fontSize: '1.25rem', fontWeight: '700', color: '#064e3b', marginBottom: '0.75rem', cursor: 'pointer' }}>
          {deal.itemName || 'Delicious Food'}
        </h3>

        {/* Vendor Info */}
        <div className="vendor-info-modern" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.75rem' }}>
          <div className="vendor-name" style={{ fontSize: '0.875rem', color: '#6b7280', display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
            <span className="location-icon" style={{ color: '#10b981' }}>⚬</span>
            {deal.vendor?.restaurantName || 'Unknown Vendor'} - {deal.vendor?.location || 'Location'}
          </div>
          {deal.vendor?.rating && deal.vendor.rating > 0 && (
            <div className="vendor-rating" style={{ display: 'flex', alignItems: 'center', gap: '0.25rem', fontSize: '0.875rem', fontWeight: '600', color: '#064e3b' }}>
              <span className="star-icon" style={{ color: '#F59E0B' }}>★</span>
              {deal.vendor.rating.toFixed(1)}
            </div>
          )}
        </div>

        {/* Description */}
        {deal.description && (
          <p className="deal-description-modern" style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '0.75rem', lineHeight: '1.5' }}>
            {deal.description.length > 80 
              ? `${deal.description.substring(0, 80)}...` 
              : deal.description
            }
          </p>
        )}

        {/* Time and Quantity Info */}
        <div className="deal-meta" style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.75rem', padding: '0.75rem', background: '#f9fafb', borderRadius: '8px' }}>
          <div className="pickup-time" style={{ fontSize: '0.875rem', color: '#374151', display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
            <span className="time-icon" style={{ color: '#10b981' }}>◷</span>
            {formatTime(deal.dealStartTime)} - {formatTime(deal.dealEndTime)}
          </div>
          <div className="quantity-info" style={{ fontSize: '0.875rem', color: '#374151', display: 'flex', alignItems: 'center', gap: '0.25rem', fontWeight: '600' }}>
            <span className="quantity-icon" style={{ color: '#10b981' }}>■</span>
            {remainingQuantity} left
          </div>
        </div>

        {/* Food Type Badge */}
        <div className="food-type-container" style={{ marginBottom: '1rem' }}>
          <span className="food-type-badge" style={{ display: 'inline-block', padding: '0.375rem 0.875rem', background: '#dcfce7', color: '#166534', borderRadius: '20px', fontSize: '0.75rem', fontWeight: '600' }}>
            {deal.foodType || 'Vegetarian'}
          </span>
        </div>

        {/* Price Section */}
        <div className="price-section" style={{ borderTop: '1px solid #e5e7eb', paddingTop: '1rem' }}>
          <div className="price-info" style={{ marginBottom: '0.75rem', display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <span className="current-price" style={{ fontSize: '1.75rem', fontWeight: '800', color: '#10b981' }}>₹{deal.newPrice || 0}</span>
            {deal.originalPrice && deal.originalPrice > deal.newPrice && (
              <span className="original-price" style={{ fontSize: '1.125rem', color: '#9ca3af', textDecoration: 'line-through' }}>₹{deal.originalPrice}</span>
            )}
          </div>
          <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
            {deal.vendor?.phoneNumber && (
              <a 
                href={`tel:${deal.vendor.phoneNumber}`}
                className="btn btn-success"
                style={{ 
                  flex: '1',
                  minWidth: '120px',
                  textDecoration: 'none',
                  textAlign: 'center',
                  fontSize: '0.9rem',
                  padding: '0.75rem 1rem',
                  background: '#10b981',
                  color: 'white',
                  borderRadius: '8px',
                  fontWeight: '600',
                  transition: 'background 0.3s ease'
                }}
                onClick={(e) => e.stopPropagation()}
              >
                Call Vendor
              </a>
            )}
            <button 
              className="view-deal-btn"
              style={{ 
                flex: '1', 
                minWidth: '100px',
                padding: '0.75rem 1rem',
                background: '#059669',
                color: 'white',
                border: 'none',
                borderRadius: '8px',
                fontWeight: '600',
                fontSize: '0.9rem',
                cursor: 'pointer',
                transition: 'background 0.3s ease'
              }}
              onClick={(e) => {
                e.stopPropagation();
                onOpenModal(deal);
              }}
            >
              View Deal
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DealCard;