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
          <Link to="/create-character" className="bg-primary p-6 rounded-lg shadow-lg hover:bg-secondary transition duration-300">
            <h2 className="text-3xl font-semibold text-accent">Create Characters</h2>
            <p className="mt-2 text-secondary">Craft unique characters with detailed stats and abilities.</p>
          </Link>
          <Link to="/create-campaign" className="bg-primary p-6 rounded-lg shadow-lg hover:bg-secondary transition duration-300">
            <h2 className="text-3xl font-semibold text-accent">Create Campaigns</h2>
            <p className="mt-2 text-secondary">Create epic campaigns and collaborate with other players.</p>
          </Link>
          <Link to="/create-homebrew" className="bg-primary p-6 rounded-lg shadow-lg hover:bg-secondary transition duration-300">
            <h2 className="text-3xl font-semibold text-accent">Design Homebrew Content</h2>
            <p className="mt-2 text-secondary">Craft your own items, skills, and more.</p>
          </Link>
        </div>
        <div className="mt-8">
          <Link to="/login" className="bg-accent text-background font-bold py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300">
            Login / Signup
          </Link>
        </div>
      </main>
    </div>
  );
};

export default Home;

