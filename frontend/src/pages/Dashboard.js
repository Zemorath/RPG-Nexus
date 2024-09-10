import React, { useState, useEffect, useContext } from 'react';
import { AuthContext } from '../services/AuthContext'; // Use the context
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
  const [characters, setCharacters] = useState([]);
  const { user, loading } = useContext(AuthContext); // Access user from context
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCharacters = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5555/api/users/${user.id}/characters`);
        setCharacters(response.data);
      } catch (error) {
        console.error('Error fetching characters:', error);
      }
    };

    if (user) {
      fetchCharacters();
    }
  }, [user]);

  if (loading) {
    return <div>Loading...</div>; // Loading state
  }

  return (
    <div className="min-h-screen bg-background text-text">
      <div className="container mx-auto p-8">
        <h1 className="text-4xl font-bold mb-8">Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Character Overview Section */}
          <div className="bg-primary p-6 rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold mb-4">Character Overview</h2>
            {characters.length > 0 ? (
              <ul>
                {characters.map(character => (
                  <li key={character.id} className="mb-2">
                    <strong>{character.name}</strong> (Level {character.level}) - {character.rpg_system.name}
                    <button
                      className="ml-2 text-accent hover:text-secondary"
                      onClick={() => navigate(`/characters/${character.id}/details`)}
                    >
                      View
                    </button>
                  </li>
                ))}
              </ul>
            ) : (
              <p>No characters found. Create your first character!</p>
            )}
            <button
              className="mt-4 bg-accent text-white px-4 py-2 rounded hover:bg-secondary"
              onClick={() => navigate('/character/create')}
            >
              Create New Character
            </button>
          </div>

          {/* Campaign Overview Section */}
          <div className="bg-primary p-6 rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold mb-4">Campaign Overview</h2>
            <p>Manage your campaigns here. You can view, edit, or create new campaigns.</p>
            <button
              className="mt-4 bg-accent text-white px-4 py-2 rounded hover:bg-secondary"
              onClick={() => navigate('/campaigns/create')}
            >
              Create New Campaign
            </button>
          </div>

          {/* Recent Activities Section */}
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
