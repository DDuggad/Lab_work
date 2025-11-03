import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import '../styles/theme.css';

const HomePage = () => {
  const { isAuthenticated } = useAuth();

  return (
    <div className="homepage">
      <section className="hero" style={{ background: 'linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%)' }}>
        <div className="container">
          <div className="hero-content" style={{ textAlign: 'center', padding: '4rem 0' }}>
            <h1 className="hero-title" style={{ color: '#064e3b', marginBottom: '1.5rem' }}>
              🍽️ Reduce Food Waste,<br />
              <span style={{ color: '#10b981' }}>Grow Your Business</span>
            </h1>
            <p className="hero-subtitle" style={{ color: '#374151', fontSize: '1.25rem', marginBottom: '2rem' }}>
              Join FreshBites as a vendor and turn your surplus food into profit. 
              Help reduce food waste while attracting new customers in Bangalore 
              with exclusive last-minute deals.
            </p>
            <div className="hero-buttons">
              <Link to="/deals" className="btn btn-primary btn-large">
                🔍 Browse Active Deals
              </Link>
              {!isAuthenticated() && (
                <Link to="/register" className="btn btn-success btn-large">
                  🏪 Join as Vendor
                </Link>
              )}
            </div>
          </div>
        </div>
      </section>

      <section className="section" style={{ padding: '4rem 0', background: 'white' }}>
        <div className="container">
          <h2 className="section-title" style={{ color: '#10b981', textAlign: 'center', marginBottom: '1rem' }}>Why Vendors Choose FreshBites?</h2>
          <p className="section-subtitle" style={{ textAlign: 'center', color: '#6b7280', marginBottom: '3rem' }}>
            Transform surplus inventory into revenue while making an environmental impact.
          </p>
          
          <div className="grid grid-3">
            <div className="card fade-in" style={{ border: '2px solid #81C784', background: 'white', padding: '2rem', borderRadius: '12px' }}>
              <div className="feature-icon" style={{ fontSize: '3rem' }}>💰</div>
              <h3 style={{ color: '#064e3b', marginTop: '1rem', marginBottom: '0.5rem' }}>Increase Revenue</h3>
              <p style={{ color: '#6b7280' }}>Turn surplus food into profit instead of waste. Set your own prices and manage inventory in real-time.</p>
            </div>
            
            <div className="card fade-in" style={{ border: '2px solid #81C784', background: 'white', padding: '2rem', borderRadius: '12px' }}>
              <div className="feature-icon" style={{ fontSize: '3rem' }}>🌱</div>
              <h3 style={{ color: '#064e3b', marginTop: '1rem', marginBottom: '0.5rem' }}>Reduce Waste</h3>
              <p style={{ color: '#6b7280' }}>Contribute to sustainability and reduce food waste. Be part of the eco-friendly movement in Bangalore.</p>
            </div>
            
            <div className="card fade-in" style={{ border: '2px solid #81C784', background: 'white', padding: '2rem', borderRadius: '12px' }}>
              <div className="feature-icon" style={{ fontSize: '3rem' }}>📱</div>
              <h3 style={{ color: '#064e3b', marginTop: '1rem', marginBottom: '0.5rem' }}>Easy Management</h3>
              <p style={{ color: '#6b7280' }}>Simple dashboard to add deals, track stock, and manage your offerings with just a few clicks.</p>
            </div>
          </div>
        </div>
      </section>

      <section className="section" style={{ background: '#f9fafb', padding: '4rem 0' }}>
        <div className="container">
          <h2 className="section-title" style={{ textAlign: 'center', color: '#064e3b', marginBottom: '3rem' }}>How It Works for Vendors</h2>
          <div className="grid grid-3">
            <div className="card" style={{ background: 'white', padding: '2rem', borderRadius: '12px', textAlign: 'center' }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>1️⃣</div>
              <h3 style={{ color: '#064e3b', marginBottom: '0.5rem' }}>Register Your Restaurant</h3>
              <p style={{ color: '#6b7280' }}>Create your vendor account and complete your restaurant profile with details and images.</p>
            </div>
            <div className="card" style={{ background: 'white', padding: '2rem', borderRadius: '12px', textAlign: 'center' }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>2️⃣</div>
              <h3 style={{ color: '#064e3b', marginBottom: '0.5rem' }}>Add Daily Deals</h3>
              <p style={{ color: '#6b7280' }}>Post surplus food items with discounted prices, set stock levels, and timing for pickup.</p>
            </div>
            <div className="card" style={{ background: 'white', padding: '2rem', borderRadius: '12px', textAlign: 'center' }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>3️⃣</div>
              <h3 style={{ color: '#064e3b', marginBottom: '0.5rem' }}>Manage & Track</h3>
              <p style={{ color: '#6b7280' }}>Update stock in real-time, receive calls from customers, and track your sales performance.</p>
            </div>
          </div>
        </div>
      </section>

      <section className="section" style={{ padding: '4rem 0', background: 'white' }}>
        <div className="container">
          <div className="cta-section" style={{ background: 'linear-gradient(135deg, #10b981, #059669)', color: 'white', padding: '3rem', borderRadius: '16px', textAlign: 'center' }}>
            <h2 style={{ color: 'white', marginBottom: '1rem' }}>Ready to Reduce Waste & Boost Revenue?</h2>
            <p style={{ color: 'rgba(255,255,255,0.95)', marginBottom: '2rem', fontSize: '1.125rem' }}>Join leading Pure Veg restaurants in Bangalore already making a difference.</p>
            <div className="cta-buttons">
              <Link to="/deals" className="btn" style={{ background: 'white', color: '#10b981', padding: '0.875rem 2rem', borderRadius: '8px', textDecoration: 'none', fontWeight: '600', display: 'inline-block', marginRight: '1rem' }}>
                See How It Works
              </Link>
              {!isAuthenticated() && (
                <Link to="/register" className="btn btn-outline" style={{ borderColor: 'white', color: 'white', border: '2px solid white', padding: '0.875rem 2rem', borderRadius: '8px', textDecoration: 'none', fontWeight: '600', display: 'inline-block' }}>
                  🚀 Start Today - It's Free!
                </Link>
              )}
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;