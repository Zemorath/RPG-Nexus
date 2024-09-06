import React, { useState, useEffect } from 'react';
import axios from 'axios'; // For making HTTP requests

const RPGSystemsPage = () => {
  const [systems, setSystems] = useState([]); // State to hold fetched RPG systems
  const [selectedSystem, setSelectedSystem] = useState(null); // State to track the selected system for modal
  const [loading, setLoading] = useState(true); // State for loading

  // Fetch RPG systems from the backend
  useEffect(() => {
    const fetchSystems = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5555/api/rpgsystems'); // Fetch from the RPGSystemList route
        setSystems(response.data); // Set systems data
        setLoading(false); // Set loading to false
      } catch (error) {
        console.error('Error fetching RPG systems:', error);
        setLoading(false);
      }
    };

    fetchSystems();
  }, []);

  // Handle opening modal
  const handleSelectSystem = (system) => {
    setSelectedSystem(system);
  };

  // Handle closing modal
  const handleCloseModal = () => {
    setSelectedSystem(null);
  };

  if (loading) {
    return <div>Loading RPG Systems...</div>; // Show a loading message while fetching
  }

  const truncateDescription = (description) => {
    return description.length > 100 ? description.slice(0, 100) + '...' : description;
  };

  return (
    <div className="min-h-screen bg-background text-text">
      <div className="container mx-auto p-8">
        <h1 className="text-4xl font-bold text-center text-accent mb-6">Available RPG Systems</h1>
        <p className="text-center mb-10 text-lg">Browse and select a system to view more details and create a character or campaign.</p>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {systems.map(system => (
            <div key={system.id} className="bg-secondary p-6 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
              <div className="text-center text-xl font-bold mb-4">{system.name}</div>
              <img src={system.default_settings.logo} alt={`${system.name} logo`} className="mx-auto w-100 h-24 mb-4" />
              <p className="mb-4">{truncateDescription(system.description)}</p>
              <button
                className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
                onClick={() => handleSelectSystem(system)}
              >
                Learn More
              </button>
            </div>
          ))}
        </div>

        {/* Modal Popup */}
        {selectedSystem && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
            <div className="bg-secondary p-8 rounded-lg shadow-lg max-w-xl w-full relative">
              <button
                className="absolute top-2 right-2 text-background text-lg"
                onClick={handleCloseModal}
              >
                X
              </button>
              <h2 className="text-2xl font-bold mb-4">{selectedSystem.name}</h2>
              <p>{selectedSystem.description}</p>
              <p className="mt-4"><strong>Setting:</strong> {selectedSystem.default_settings.setting}</p>
              <p className="mt-4"><strong>Dice Mechanics:</strong> {selectedSystem.default_settings.dice}</p>
              <p className="mt-4"><strong>Classes:</strong> {selectedSystem.default_settings.classes.join(', ')}</p>
              <p className="mt-4"><strong>Races:</strong> {selectedSystem.default_settings.races.join(', ')}</p>
              <p className="mt-4"><strong>Unique Mechanics:</strong> {selectedSystem.default_settings.mechanics.join(', ')}</p>
              <p className="mt-4"><strong>Popularity:</strong> <span className="text-yellow-500">{selectedSystem.popularity}</span></p>
              <button className="mt-6 bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300">
                Start Character Creation
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default RPGSystemsPage;
