import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const ViewCharactersPage = () => {
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Fetch characters for the logged-in user
  useEffect(() => {
    const fetchCharacters = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5555/api/characters/view'); // Adjust API endpoint as needed
        setCharacters(response.data.characters);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching characters:', error);
        setLoading(false);
      }
    };

    fetchCharacters();
  }, []);

  // Determine the border color based on RPG system
  const getBorderColor = (systemName) => {
    switch (systemName.toLowerCase()) {
      case 'dungeons & dragons':
        return 'border-red-600'; // D&D
      case 'pathfinder':
        return 'border-yellow-500'; // Pathfinder
      case 'call of cthulhu':
        return 'border-blue-600'; // Call of Cthulhu
      case 'shadowrun':
        return 'border-green-600'; // Shadowrun
      case 'star wars: edge of the empire':
        return 'border-gray-600'; // Star Wars
      default:
        return 'border-accent'; // Default accent color
    }
  };

  if (loading) {
    return <div className="text-center text-text text-lg">Loading Characters...</div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        <h1 className="text-4xl font-bold text-center text-accent mb-8">Your Characters</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {characters.map((character) => (
            <div
              key={character.id}
              className={`p-6 rounded-lg shadow-lg ${getBorderColor(character.rpg_system.name)} border-4 hover:shadow-2xl transition-all duration-300`}
            >
              <h2 className="text-2xl font-bold text-center mb-2">{character.name}</h2>
              <p className="text-center mb-2">
                <strong>Race:</strong> {character.race.name}
              </p>
              <p className="text-center mb-2">
                <strong>Class:</strong> {character.class.name}
              </p>
              <p className="text-center mb-2">
                <strong>Level:</strong> {character.level}
              </p>
              <p className="text-center text-xs italic text-accent mt-4">
                {character.rpg_system.name}
              </p>
            </div>
          ))}
        </div>

        {/* Back Button */}
        <button
          className="mt-6 bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
          onClick={() => navigate('/dashboard')}
        >
          Back to Dashboard
        </button>
      </div>
    </div>
  );
};

export default ViewCharactersPage;
