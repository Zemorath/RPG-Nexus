// src/pages/Home.js
import React from 'react';
import { Link } from 'react-router-dom';
import { FaShieldAlt, FaBook, FaRocket } from 'react-icons/fa';

const HomePage = () => {
  console.log('Rendering updated HomePage')
  return (
    <div className="min-h-screen bg-background text-text">
      <div className="bg-gradient-to-r from-primary to-secondary p-8 text-center">
        <h1 className="text-accent text-5xl font-bold mb-4">Welcome to RPG Nexus</h1>
        <p className="text-lg mb-6">Your ultimate tool for crafting legendary characters and epic adventures.</p>
        <div className="flex justify-center gap-4">
          <Link to="/signup">
            <button className="interactive-button">Sign Up</button>
          </Link>
          <Link to="/login">
            <button className="interactive-button">Login</button>
          </Link>
        </div>
      </div>
      <div className="container mx-auto p-8">
        <h2 className="text-accent text-3xl font-bold text-center mb-8">Features</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div className="bg-secondary p-6 rounded-lg shadow-lg border border-accent/20 hover:shadow-accent/50 hover:scale-105 transition duration-300">
            <FaShieldAlt className="text-accent text-4xl mx-auto mb-4" />
            <h3 className="text-accent text-xl font-bold mb-2">Create Characters</h3>
            <p>Build unique heroes for any TTRPG system with ease.</p>
          </div>
          <div className="bg-secondary p-6 rounded-lg shadow-lg border border-accent/20 hover:shadow-accent/50 hover:scale-105 transition duration-300">
            <FaBook className="text-accent text-4xl mx-auto mb-4" />
            <h3 className="text-accent text-xl font-bold mb-2">Manage Campaigns</h3>
            <p>Organize your adventures and track your party’s journey.</p>
          </div>
          <div className="bg-secondary p-6 rounded-lg shadow-lg border border-accent/20 hover:shadow-accent/50 hover:scale-105 transition duration-300">
            <FaRocket className="text-accent text-4xl mx-auto mb-4" />
            <h3 className="text-accent text-xl font-bold mb-2">Explore Systems</h3>
            <p>Dive into a variety of RPG rulesets and homebrew options.</p>
          </div>
        </div>
      </div>
      <div className="bg-primary p-4 text-center">
        <p className="text-sm">
          <Link to="/about" className="text-accent hover:underline">About</Link> |{' '}
          <Link to="/contact" className="text-accent hover:underline">Contact</Link>
        </p>
      </div>
    </div>
  );
};

export default HomePage;