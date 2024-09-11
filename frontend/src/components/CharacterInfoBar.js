// src/components/CharacterInfoBar.js
import React from 'react';

const CharacterInfoBar = ({ characterData, onNameChange }) => {
  const { name, rpgSystem, race, className } = characterData;

  return (
    <div className="bg-primary text-text p-4 shadow-lg flex justify-between">
      <div className="flex flex-col">
        <label htmlFor="name" className="text-accent font-bold">Character Name</label>
        <input
          type="text"
          id="name"
          value={name}
          onChange={(e) => onNameChange(e.target.value)}
          className="bg-secondary text-text p-2 rounded-md"
          placeholder="Enter character name"
        />
      </div>
      <div className="flex flex-col">
        <span className="text-accent font-bold">RPG System</span>
        <span>{rpgSystem || 'Not selected'}</span>
      </div>
      <div className="flex flex-col">
        <span className="text-accent font-bold">Race</span>
        <span>{race || 'Not selected'}</span>
      </div>
      <div className="flex flex-col">
        <span className="text-accent font-bold">Class</span>
        <span>{className || 'Not selected'}</span>
      </div>
    </div>
  );
};

export default CharacterInfoBar;
