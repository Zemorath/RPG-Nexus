import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="bg-background text-text min-h-screen flex flex-col items-center justify-center">
      <header className="text-center">
        <h1 className="text-5xl font-bold text-accent">Welcome to RPG Nexus</h1>
        <p className="text-secondary mt-4 text-xl">Your gateway to endless adventures</p>
      </header>
      <main className="mt-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <Link to="/craft-characters">
            <div className="bg-primary p-6 rounded-lg shadow-lg transform hover:scale-105 transition-transform duration-300 cursor-pointer">
              <h2 className="text-3xl font-semibold text-accent">Craft Characters</h2>
              <p className="mt-2 text-secondary">Create unique characters with detailed stats and abilities.</p>
            </div>
          </Link>
          <Link to="/create-campaigns">
            <div className="bg-primary p-6 rounded-lg shadow-lg transform hover:scale-105 transition-transform duration-300 cursor-pointer">
              <h2 className="text-3xl font-semibold text-accent">Create Campaigns</h2>
              <p className="mt-2 text-secondary">Create epic campaigns and collaborate with other players.</p>
            </div>
          </Link>
          <Link to="/design-homebrew">
            <div className="bg-primary p-6 rounded-lg shadow-lg transform hover:scale-105 transition-transform duration-300 cursor-pointer">
              <h2 className="text-3xl font-semibold text-accent">Design Homebrew Content</h2>
              <p className="mt-2 text-secondary">Create custom items, monsters, and more for your campaigns.</p>
            </div>
          </Link>
        </div>
      </main>
    </div>
  );
};

export default Home;
