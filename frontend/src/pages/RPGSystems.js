import React, { useState, useEffect } from 'react';
import axios from 'axios'; // For making HTTP requests

const RPGSystemsPage = () => {
  const [systems, setSystems] = useState([]); // State to hold fetched RPG systems
  const [expandedSystem, setExpandedSystem] = useState(null); // State to track which system is expanded
  const [loading, setLoading] = useState(true); // State for loading

  // Fetch RPG systems from the backend
  useEffect(() => {
    const fetchSystems = async () => {
      try {
        const response = await axios.get('/api/rpgsystems'); // Fetch from the RPGSystemList route
        setSystems(response.data); // Set systems data
        setLoading(false); // Set loading to false
      } catch (error) {
        console.error('Error fetching RPG systems:', error);
        setLoading(false);
      }
    };

    fetchSystems();
  }, []);

  // Handle system expansion
  const handleExpand = (systemId) => {
    setExpandedSystem(systemId);
  };

  if (loading) {
    return <div>Loading RPG Systems...</div>; // Show a loading message while fetching
  }

  return (
    <div className="min-h-screen bg-background text-text">
      <div className="container mx-auto p-8">
        <h1 className="text-4xl font-bold text-center text-accent mb-6">Available RPG Systems</h1>
        <p className="text-center mb-10 text-lg">Browse and select a system to view more details and create a character or campaign.</p>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {systems.map(system => (
            <div key={system.id} className="bg-secondary p-6 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
              <div className="text-xl font-bold mb-4">{system.name}</div>
              <img src={system.logo} alt={`${system.name} logo`} className="w-24 h-24 mb-4" />
              <p className="mb-4">{system.description}</p>
              <button
                className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
                onClick={() => handleExpand(system.id)}
              >
                Learn More
              </button>
            </div>
          ))}
        </div>

        {/* Expanded System Information */}
        {expandedSystem && (
          <div className="mt-12 p-6 bg-secondary rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold mb-4">{systems.find(system => system.id === expandedSystem)?.name}</h2>
            <p>{systems.find(system => system.id === expandedSystem)?.fullDescription}</p>
            <p className="mt-4"><strong>Setting:</strong> {systems.find(system => system.id === expandedSystem)?.default_settings.setting}</p>
            <p className="mt-4"><strong>Dice Mechanics:</strong> {systems.find(system => system.id === expandedSystem)?.default_settings.dice}</p>
            <p className="mt-4"><strong>Classes:</strong> {systems.find(system => system.id === expandedSystem)?.default_settings.classes.join(', ')}</p>
            <p className="mt-4"><strong>Races:</strong> {systems.find(system => system.id === expandedSystem)?.default_settings.races.join(', ')}</p>
            <p className="mt-4"><strong>Unique Mechanics:</strong> {systems.find(system => system.id === expandedSystem)?.default_settings.mechanics.join(', ')}</p>
            <p className="mt-4"><strong>Popularity:</strong> <span className="text-yellow-500">{systems.find(system => system.id === expandedSystem)?.popularity}</span></p>
            <button className="mt-6 bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300">
              Start Character Creation
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default RPGSystemsPage;
