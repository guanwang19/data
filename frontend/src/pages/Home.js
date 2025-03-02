import React from "react";
import { Link } from "react-router-dom";
import "./Home.css"; // Styling for the page

const Home = () => {
  return (
    <div className="home-container">
      <nav className="navbar">
        <div className="logo">Course Platform</div>
        <div className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/courses">Courses</Link>
          <Link to="/contact">Contact</Link>
          <Link to="/cart" className="cart-icon">🛒</Link>
          <Link to="/signup" className="signup-btn">Sign Up</Link>
          <Link to="/login" className="login-btn">Login</Link>
        </div>
      </nav>

      <header className="hero">
        <h1>Data Literacy Fundamentals</h1>
        <p>Understanding the Power & Value of Data</p>
        <div className="cta-buttons">
          <Link to="/signup" className="btn">Enroll Now</Link>
          <Link to="/pricing" className="btn">Team Pricing</Link>
          <Link to="/all-access" className="btn">All-Access</Link>
        </div>
        <p className="preview-text">
          <Link to="/preview">▶ Preview the first lesson for free</Link>
        </p>
      </header>
    </div>
  );
};

export default Home;
