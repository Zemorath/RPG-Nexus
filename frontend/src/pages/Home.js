import React from 'react';

const Home = () => {
  return (
    <div className="bg-background text-text min-h-screen flex flex-col items-center justify-center">
      <header className="text-center">
        <h1 className="text-5xl font-bold text-accent">Welcome to RPG Nexus</h1>
        <p className="text-secondary mt-4 text-xl">Your gateway to endless adventures</p>
      </header>
      <main className="mt-8">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-primary p-6 rounded-lg shadow-lg">
            <h2 className="text-3xl font-semibold text-accent">Create Characters</h2>
            <p className="mt-2 text-secondary">Craft unique characters with detailed stats and abilities.</p>
          </div>
          <div className="bg-primary p-6 rounded-lg shadow-lg">
            <h2 className="text-3xl font-semibold text-accent">Join Campaigns</h2>
            <p className="mt-2 text-secondary">Join epic campaigns and collaborate with other players.</p>
          </div>
          <div className="bg-primary p-6 rounded-lg shadow-lg">
            <h2 className="text-3xl font-semibold text-accent">Track Inventory</h2>
            <p className="mt-2 text-secondary">Keep track of your items and resources effortlessly.</p>
          </div>
          <div className="bg-primary p-6 rounded-lg shadow-lg">
            <h2 className="text-3xl font-semibold text-accent">Record Notes</h2>
            <p className="mt-2 text-secondary">Document your adventures and keep track of important details.</p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Home;
