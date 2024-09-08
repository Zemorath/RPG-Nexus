// CharacterCreationLandingPage.js

import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const CharacterCreationLandingPage = () => {
  const [rpgSystems, setRpgSystems] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchRpgSystems = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5555/api/rpgsystems');
        setRpgSystems(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching RPG systems:', error);
        setLoading(false);
      }
    };

    fetchRpgSystems();
  }, []);

  const handleSelectSystem = (systemId) => {
    // Navigate to the first step (Select Race) with the selected RPG system ID
    navigate(`/character/create/race/${systemId}`);
  };

  if (loading) {
    return <div>Loading RPG Systems...</div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        <h1 className="text-4xl font-bold text-center text-accent mb-6">Start Character Creation</h1>
        <p className="text-center mb-10 text-lg">Select an RPG system to create your character.</p>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {rpgSystems.map(system => (
            <div
              key={system.id}
              className="bg-secondary p-6 rounded-lg shadow-lg hover:shadow-xl transition duration-300 cursor-pointer"
              onClick={() => handleSelectSystem(system.id)}
            >
              <div className="text-center text-xl font-bold mb-4">{system.name}</div>
              <img src={system.default_settings.logo} alt={`${system.name} logo`} className="mx-auto w-100 h-24 mb-4" />
              <p className="mb-4">{system.description.length > 100 ? `${system.description.slice(0, 100)}...` : system.description}</p>
            </div>
          ))}
        </div>
        {/* Home Button */}
        <button
          className="mt-6 bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
          onClick={() => navigate('/')}
        >
          Home
        </button>
      </div>
    </div>
  );
};

export default CharacterCreationLandingPage;
