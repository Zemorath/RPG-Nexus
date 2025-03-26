// src/pages/ViewCharacters.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { FaUser, FaEdit, FaTrash } from 'react-icons/fa';

const ViewCharactersPage = () => {
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedCharacter, setSelectedCharacter] = useState(null);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const navigate = useNavigate();

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

  const handleDelete = async (characterId) => {
    try {
      await axios.delete(`http://127.0.0.1:5555/api/characters/${characterId}`, { withCredentials: true });
      setCharacters(characters.filter(character => character.id !== characterId));
      setShowDeleteModal(false);
    } catch (error) {
      console.error('Error deleting character:', error);
    }
  };

  const openDeleteModal = (character) => {
    setSelectedCharacter(character);
    setShowDeleteModal(true);
  };

  const closeDeleteModal = () => {
    setShowDeleteModal(false);
    setSelectedCharacter(null);
  };

  const handleEdit = (systemId, characterId) => {
    navigate(`/character/create/race/${systemId}/${characterId}`);
  };

  const getCardColor = (rpgSystem) => {
    switch (rpgSystem.toLowerCase()) {
      case 'dungeons & dragons 5th edition':
        return 'bg-red-700';
      case 'pathfinder':
        return 'bg-yellow-700';
      case 'call of cthulhu':
        return 'bg-green-700';
      case 'shadowrun':
        return 'bg-blue-700';
      case 'star wars: edge of the empire':
        return 'bg-purple-700';
      case 'mothership rpg':
        return 'bg-gray-700';
      default:
        return 'bg-accent'; // #d4af37 remains as is
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-background text-accent flex items-center justify-center">
        <div className="text-2xl font-bold">Loading Characters...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-background text-text">
      <div className="container mx-auto p-8">
        <div className="bg-gradient-to-r from-primary to-secondary p-4 rounded-t-lg text-center">
          <h1 className="text-accent text-4xl font-bold">Your Characters</h1>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 mt-8">
          {characters.map((character) => (
            <div
              key={character.id}
              className={`${getCardColor(character.rpg_system.name)} p-6 rounded-lg shadow-lg hover:shadow-xl transition duration-300`}
            >
              <div className="flex items-center justify-center mb-4">
                <FaUser className="text-text text-3xl mr-2" />
                <h2 className="text-text text-2xl font-bold">{character.name}</h2>
              </div>
              <p className="text-center mb-2"><strong>Race:</strong> {character.race.name}</p>
              <p className="text-center mb-2"><strong>Class:</strong> {character.class.name}</p>
              <p className="text-center mb-2"><strong>Level:</strong> {character.level}</p>
              <p className="text-center text-xs italic text-text mt-4">{character.rpg_system.name}</p>
              <div className="flex justify-center gap-4 mt-4">
                <button
                  className="interactive-button flex items-center"
                  onClick={() => handleEdit(character.rpg_system.id, character.id)}
                >
                  <FaEdit className="mr-2" /> Edit
                </button>
                <button
                  className="interactive-button flex items-center"
                  onClick={() => openDeleteModal(character)}
                >
                  <FaTrash className="mr-2" /> Delete
                </button>
              </div>
            </div>
          ))}
        </div>
        <div className="mt-8 flex justify-center">
          <button
            className="interactive-button"
            onClick={() => navigate('/dashboard')}
          >
            Back to Dashboard
          </button>
        </div>
      </div>

      {showDeleteModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
          <div className="bg-secondary p-8 rounded-lg shadow-lg border border-accent/20 max-w-sm w-full text-center">
            <h2 className="text-accent text-2xl font-bold mb-4">Delete Character</h2>
            <p className="text-text">Are you sure you want to delete <strong>{selectedCharacter.name}</strong>?</p>
            <div className="mt-6 flex justify-center gap-4">
              <button
                className="interactive-button bg-red-600 hover:bg-red-700"
                onClick={() => handleDelete(selectedCharacter.id)}
              >
                Delete
              </button>
              <button
                className="interactive-button bg-gray-600 hover:bg-gray-700"
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