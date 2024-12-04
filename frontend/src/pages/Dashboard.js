import React, { useState, useEffect } from 'react';
import { useAuth } from '../components/auth/auth';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
  const [characters, setCharacters] = useState([]);
  const { user, loading } = useAuth(); // Use the useAuth hook
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCharacters = async () => {
      if (!user) return; // Exit if there's no user

      try {
        const response = await axios.get(`http://127.0.0.1:5555/api/characters/view`, {
          withCredentials: true // Ensure cookies are sent with the request
        });
        setCharacters(response.data);
      } catch (error) {
        console.error('Error fetching characters:', error);
        // Handle error (e.g., redirect to login if unauthorized)
        if (error.response && error.response.status === 401) {
          navigate('/login');
        }
      }
    };

    fetchCharacters();
  }, [user, navigate]);

  if (loading) {
    return <div>Loading...</div>; // Loading state
  }

  if (!user) {
    navigate('/login');
    return null;
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
            <p>See what you've been up to recently with your characters and campaigns.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;