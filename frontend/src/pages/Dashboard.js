import React from 'react';

const Dashboard = () => {
  return (
    <div className="min-h-screen bg-background text-text">
      <div className="container mx-auto p-8">
        <h1 className="text-4xl font-bold mb-8">Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-primary p-6 rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold mb-4">Character Overview</h2>
            <p>Manage your characters here. You can view, edit, or create new characters.</p>
            <button className="mt-4 bg-accent text-white px-4 py-2 rounded hover:bg-secondary">Create New Character</button>
          </div>
          <div className="bg-primary p-6 rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold mb-4">Campaign Overview</h2>
            <p>Manage your campaigns here. You can view, edit, or create new campaigns.</p>
            <button className="mt-4 bg-accent text-white px-4 py-2 rounded hover:bg-secondary">Create New Campaign</button>
          </div>
          <div className="bg-primary p-6 rounded-lg shadow-lg md:col-span-2">
            <h2 className="text-2xl font-bold mb-4">Recent Activities</h2>
            <p>See what you’ve been up to recently with your characters and campaigns.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
