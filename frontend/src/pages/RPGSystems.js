import React, { useState } from 'react';

const systems = [
  {
    id: 1,
    name: 'Dungeons & Dragons 5th Edition',
    logo: '/path/to/dnd-logo.png',
    shortDescription: 'A high-fantasy adventure filled with magic, dungeons, and dragons.',
    fullDescription: 'Dungeons & Dragons is the world’s most popular role-playing game, ...',
    setting: 'High Fantasy',
    diceMechanics: 'd20 system, with advantage/disadvantage mechanic.',
    classes: ['Fighter', 'Wizard', 'Cleric', 'Rogue', 'Ranger', 'Druid'],
    races: ['Human', 'Elf', 'Dwarf', 'Halfling', 'Orc'],
    uniqueMechanics: ['Advantage/Disadvantage', 'Hit Dice', 'Proficiency Bonus'],
    popularity: '★★★★☆',
  },
  // Add other systems here
];

const RPGSystemsPage = () => {
  const [expandedSystem, setExpandedSystem] = useState(null);

  const handleExpand = (systemId) => {
    setExpandedSystem(systemId);
  };

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
              <p className="mb-4">{system.shortDescription}</p>
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
            <h2 className="text-2xl font-bold mb-4">{systems[expandedSystem - 1].name}</h2>
            <p>{systems[expandedSystem - 1].fullDescription}</p>
            <p className="mt-4"><strong>Setting:</strong> {systems[expandedSystem - 1].setting}</p>
            <p className="mt-4"><strong>Dice Mechanics:</strong> {systems[expandedSystem - 1].diceMechanics}</p>
            <p className="mt-4"><strong>Classes:</strong> {systems[expandedSystem - 1].classes.join(', ')}</p>
            <p className="mt-4"><strong>Races:</strong> {systems[expandedSystem - 1].races.join(', ')}</p>
            <p className="mt-4"><strong>Unique Mechanics:</strong> {systems[expandedSystem - 1].uniqueMechanics.join(', ')}</p>
            <p className="mt-4"><strong>Popularity:</strong> <span className="text-yellow-500">{systems[expandedSystem - 1].popularity}</span></p>
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
