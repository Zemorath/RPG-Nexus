import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const ViewCharactersPage = () => {
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedCharacter, setSelectedCharacter] = useState(null); // Character selected for deletion
  const [showDeleteModal, setShowDeleteModal] = useState(false); // Control delete modal visibility
  const navigate = useNavigate();

  // Fetch characters for the logged-in user
  useEffect(() => {
    const fetchCharacters = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5555/api/characters/view', { withCredentials: true });
        setCharacters(response.data.characters);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching characters:', error);
        setLoading(false);
      }
    };

    fetchCharacters();
  }, []);

  // Handle delete character
  const handleDelete = async (characterId) => {
    try {
      await axios.delete(`http://127.0.0.1:5555/api/characters/${characterId}`, { withCredentials: true });
      setCharacters(characters.filter(character => character.id !== characterId)); // Remove from state
      setShowDeleteModal(false);
    } catch (error) {
      console.error('Error deleting character:', error);
    }
  };

  // Handle open delete modal
  const openDeleteModal = (character) => {
    setSelectedCharacter(character);
    setShowDeleteModal(true);
  };

  // Handle close delete modal
  const closeDeleteModal = () => {
    setShowDeleteModal(false);
    setSelectedCharacter(null);
  };

  // Handle edit character
  const handleEdit = (systemId, characterId) => {
    navigate(`/character/create/race/${systemId}/${characterId}`);
  };

  // Determine the border color based on RPG system
  const getBorderColor = (rpgSystem) => {
    switch (rpgSystem.toLowerCase()) {
      case 'dungeons & dragons 5th edition':
        return 'border-red-600'; // D&D
      case 'pathfinder':
        return 'border-yellow-500'; // Pathfinder
      case 'call of cthulhu':
        return 'border-green-600'; // Call of Cthulhu
      case 'shadowrun':
        return 'border-blue-600'; // Shadowrun
      case 'star wars: edge of the empire':
        return 'border-purple-600'; // Star Wars
      case 'mothership rpg':
        return 'border-gray-600';
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

              {/* Edit Button */}
              <button
                className="mt-4 bg-blue-500 text-white py-1 px-3 rounded hover:bg-blue-600 transition"
                onClick={() => handleEdit(character.rpg_system.id, character.id)}
              >
                Edit
              </button>

              {/* Delete Button */}
              <button
                className="mt-4 ml-2 bg-red-500 text-white py-1 px-3 rounded hover:bg-red-600 transition"
                onClick={() => openDeleteModal(character)}
              >
                Delete
              </button>
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

      {/* Delete Modal */}
      {showDeleteModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
          <div className="bg-primary p-8 rounded-lg shadow-lg max-w-sm w-full text-center">
            <h2 className="text-xl font-bold mb-4">Delete Character</h2>
            <p>Are you sure you want to delete {selectedCharacter.name}?</p>
            <div className="mt-6 flex justify-center gap-4">
              <button
                className="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600"
                onClick={() => handleDelete(selectedCharacter.id)}
              >
                Delete
              </button>
              <button
                className="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600"
                onClick={closeDeleteModal}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ViewCharactersPage;
