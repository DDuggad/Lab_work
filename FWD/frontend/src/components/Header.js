import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import '../styles/theme.css';

const Header = () => {
  const { user, logout, isAuthenticated, isVendor } = useAuth();
  const navigate = useNavigate();
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleLogout = () => {
    logout();
    navigate('/');
    setIsMobileMenuOpen(false);
  };

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  const closeMobileMenu = () => {
    setIsMobileMenuOpen(false);
  };

  return (
    <header className={`header ${isScrolled ? 'scrolled' : ''}`}>
      <div className="container">
        <div className="header-content">
          <Link to="/" className="logo" onClick={closeMobileMenu}>
            FreshBites
          </Link>
          
          {/* Mobile Menu Button */}
          <button 
            className={`mobile-menu-btn ${isMobileMenuOpen ? 'active' : ''}`}
            onClick={toggleMobileMenu}
            aria-label="Toggle menu"
          >
            <span></span>
            <span></span>
            <span></span>
          </button>
          
          <nav className={`nav ${isMobileMenuOpen ? 'mobile-open' : ''}`}>
            <ul className="nav-links">
              <li>
                <Link to="/" className="nav-link" onClick={closeMobileMenu}>Home</Link>
              </li>
              {!isVendor() && (
                <li>
                  <Link to="/deals" className="nav-link" onClick={closeMobileMenu}>Deals</Link>
                </li>
              )}
              {isVendor() && (
                <>
                  <li>
                    <Link to="/vendor/manage-deals" className="nav-link" onClick={closeMobileMenu}>Dashboard</Link>
                  </li>
                  <li>
                    <Link to="/vendor/add-deal" className="nav-link" onClick={closeMobileMenu}>Add Deal</Link>
                  </li>
                  <li>
                    <Link to="/vendor/profile" className="nav-link" onClick={closeMobileMenu}>Profile</Link>
                  </li>
                </>
              )}
            </ul>
            
            <div className="auth-buttons">
              {isAuthenticated() ? (
                <>
                  <span className="user-greeting">
                    Welcome, {user?.restaurantName || user?.username}
                  </span>
                  <button onClick={handleLogout} className="btn btn-outline">
                    Logout
                  </button>
                </>
              ) : (
                <>
                  <Link to="/login" className="btn btn-secondary" onClick={closeMobileMenu}>
                    Vendor Login
                  </Link>
                  <Link to="/register" className="btn btn-primary" onClick={closeMobileMenu}>
                    Join as Vendor
                  </Link>
                </>
              )}
            </div>
          </nav>
          
          {/* Mobile Overlay */}
          {isMobileMenuOpen && (
            <div className="mobile-overlay" onClick={closeMobileMenu}></div>
          )}
        </div>
      </div>
    </header>
  );
};

export default Header;