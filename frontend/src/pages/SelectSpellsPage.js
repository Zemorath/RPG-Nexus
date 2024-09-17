import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const SelectSpellsPage = () => {
  const { systemId, characterId } = useParams();
  const [spells, setSpells] = useState([]);
  const [selectedSpells, setSelectedSpells] = useState([]);
  const [maxSpells, setMaxSpells] = useState(0);  // Max number of spells allowed
  const [maxCantrips, setMaxCantrips] = useState(0); // Max number of cantrips allowed
  const [selectedLevel, setSelectedLevel] = useState(1); // Default level
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Fetch spells and class progression
  useEffect(() => {
    const fetchSpellsAndProgression = async () => {
      try {
        // Get character class
        const characterResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        const characterClassId = characterResponse.data.class.id;
  
        // Fetch class progression for the selected level
        const progressionResponse = await axios.get(`http://127.0.0.1:5555/api/class_progression/${characterClassId}/level/${selectedLevel}`);
        
        const progression = progressionResponse.data;
        setMaxSpells(progression.available_spell.spells);   // Set the max number of spells
        setMaxCantrips(progression.available_spell.cantrips);  // Set the max number of cantrips
        
        // Fetch the spells for the class
        const spellsResponse = await axios.get(`http://127.0.0.1:5555/spells/class/${characterClassId}/level/${selectedLevel}`);
        setSpells(spellsResponse.data);
  
        setLoading(false);
      } catch (error) {
        console.error('Error fetching spells and class progression:', error);
        setLoading(false);
      }
    };
  
    fetchSpellsAndProgression();
  }, [characterId, selectedLevel]);

  // Handle spell selection
  const handleSpellSelect = (spell) => {
    if (spell.level === 0 && selectedSpells.filter(s => s.level === 0).length >= maxCantrips) {
      alert(`You can only select up to ${maxCantrips} cantrips.`);
      return;
    }

    if (spell.level > 0 && selectedSpells.filter(s => s.level > 0).length >= maxSpells) {
      alert(`You can only select up to ${maxSpells} spells.`);
      return;
    }

    setSelectedSpells((prevSelected) => 
      prevSelected.includes(spell) ? prevSelected.filter(s => s.id !== spell.id) : [...prevSelected, spell]
    );
  };

  // Reset selected spells
  const handleReset = () => {
    setSelectedSpells([]);
  };

  // Submit selected spells
  const handleSubmit = async () => {
    try {
      await axios.post(`http://127.0.0.1:5555/api/characters/update-spells`, {
        character_id: characterId,
        spell_ids: selectedSpells.map(spell => spell.id),
      });
      navigate(`/character/create/equipment/${systemId}/${characterId}`);
    } catch (error) {
      console.error('Error updating spells:', error);
    }
  };

  // Handle level change
  const handleLevelChange = (event) => {
    setSelectedLevel(parseInt(event.target.value));
  };

  if (loading) {
    return <div>Loading spells...</div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        <h1 className="text-4xl font-bold text-center text-accent mb-8">Select Spells</h1>

        {/* Level Selection */}
        <div className="mb-8 text-center">
          <label className="text-xl mr-4">Select Level:</label>
          <select value={selectedLevel} onChange={handleLevelChange} className="p-2 rounded bg-secondary text-text">
            {[...Array(20).keys()].map(level => (
              <option key={level + 1} value={level + 1}>{level + 1}</option>
            ))}
          </select>
        </div>

        {/* Selected Spell Count */}
        <div className="text-center mb-4">
          <p className="text-xl">Cantrips: {selectedSpells.filter(s => s.level === 0).length}/{maxCantrips}</p>
          <p className="text-xl">Spells: {selectedSpells.filter(s => s.level > 0).length}/{maxSpells}</p>
        </div>

        {/* Spell Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {spells.map(spell => (
            <div
              key={spell.id}
              className={`p-4 rounded-lg shadow-lg cursor-pointer ${selectedSpells.includes(spell) ? 'bg-accent text-background' : 'bg-secondary'}`}
              onClick={() => handleSpellSelect(spell)}
            >
              <h3 className="text-xl font-bold">{spell.name}</h3>
              <p>{spell.description}</p>
              <p>Level: {spell.level}</p>
              <p>School: {spell.school}</p>
            </div>
          ))}
        </div>

        {/* Reset and Next Buttons */}
        <div className="flex justify-between mt-8">
          <button
            onClick={handleReset}
            className="bg-red-600 text-white py-2 px-4 rounded"
          >
            Reset
          </button>

          <button
            onClick={handleSubmit}
            className="bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
};

export default SelectSpellsPage;
