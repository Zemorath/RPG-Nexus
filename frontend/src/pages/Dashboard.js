// src/pages/Dashboard.js
import React, { useState, useEffect } from 'react';
import { useAuth } from '../components/auth/auth';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { FaUser, FaBook, FaClock } from 'react-icons/fa';

const Dashboard = () => {
  const [characters, setCharacters] = useState([]);
  const { user, loading } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCharacters = async () => {
      if (!user) return;
      try {
        const response = await axios.get(`http://127.0.0.1:5555/api/characters/view`, {
          withCredentials: true,
        });
        setCharacters(response.data.characters); // Adjusted to match ViewCharacters.js
      } catch (error) {
        console.error('Error fetching characters:', error);
        if (error.response?.status === 401) {
          navigate('/login');
        }
      }
    };
    fetchCharacters();
  }, [user, navigate]);

  if (loading) {
    return (
      <div className="min-h-screen bg-background text-accent flex items-center justify-center">
        <div className="text-2xl font-bold">Loading...</div>
      </div>
    );
  }
  if (!user) {
    navigate('/login');
    return null;
  }

  return (
    <div className="min-h-screen bg-background text-text">
      <div className="container mx-auto p-8">
        <div className="bg-gradient-to-r from-primary to-secondary p-4 rounded-t-lg text-center">
          <h1 className="text-accent text-4xl font-bold">Your Dashboard</h1>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mt-8">
          <div className="bg-secondary p-6 rounded-lg shadow-lg border border-accent/20 hover:shadow-accent/50 transition duration-300">
            <div className="flex items-center mb-4">
              <FaUser className="text-accent text-3xl mr-2" />
              <h2 className="text-accent text-2xl font-bold">Characters</h2>
            </div>
            <div className="max-h-64 overflow-y-auto">
              {characters.length > 0 ? (
                <div className="space-y-2">
                  {characters.map(character => (
                    <div
                      key={character.id}
                      className="bg-primary p-3 rounded-md flex justify-between items-center hover:bg-primary/80 transition duration-200 cursor-pointer"
                      onClick={() => navigate(`/characters/${character.id}/details`)}
                    >
                      <span className="text-text font-semibold">{character.name}</span>
                      <span className="text-text">{character.race.name} / {character.class.name}</span>
                      <span className="text-accent">Level {character.level}</span>
                    </div>
                  ))}
                </div>
              ) : (
                <p>No characters found. Create your first character!</p>
              )}
            </div>
            <button
              className="interactive-button mt-4 w-full"
              onClick={() => navigate('/character/create')}
            >
              Create New Character
            </button>
          </div>
          <div className="bg-secondary p-6 rounded-lg shadow-lg border border-accent/20 hover:shadow-accent/50 transition duration-300">
            <div className="flex items-center mb-4">
              <FaBook className="text-accent text-3xl mr-2" />
              <h2 className="text-accent text-2xl font-bold">Campaigns</h2>
            </div>
            <p>Manage your campaigns here. View, edit, or start a new adventure.</p>
            <button
              className="interactive-button mt-4 w-full"
              onClick={() => navigate('/campaigns/create')}
            >
              Create New Campaign
            </button>
          </div>
          <div className="bg-secondary p-6 rounded-lg shadow-lg border border-accent/20 hover:shadow-accent/50 transition duration-300 md:col-span-2">
            <div className="flex items-center mb-4">
              <FaClock className="text-accent text-3xl mr-2" />
              <h2 className="text-accent text-2xl font-bold">Recent Activities</h2>
            </div>
            <p>See what you’ve been up to recently with your characters and campaigns.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;