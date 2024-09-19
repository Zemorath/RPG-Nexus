import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const SelectSpellsPage = () => {
  const { systemId, characterId } = useParams();
  const [spells, setSpells] = useState([]);
  const [filteredSpells, setFilteredSpells] = useState([]); // For search and level filtering
  const [selectedSpells, setSelectedSpells] = useState([]);
  const [maxSpells, setMaxSpells] = useState(0);  // Max number of spells allowed
  const [maxCantrips, setMaxCantrips] = useState(0); // Max number of cantrips allowed
  const [selectedLevel, setSelectedLevel] = useState(1); // Default character level
  const [selectedSpellLevels, setSelectedSpellLevels] = useState([]); // Array to store selected spell levels (toggle buttons)
  const [availableSpellLevels, setAvailableSpellLevels] = useState([]); // Available spell levels for class
  const [searchTerm, setSearchTerm] = useState(''); // For spell search
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Fetch character level and spells on load
  useEffect(() => {
    const fetchCharacterData = async () => {
      try {
        // Fetch character data, including level
        const characterResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        const characterLevel = characterResponse.data.level || 1; // Set character's current level or default to 1
        const characterClassId = characterResponse.data.class.id;

        setSelectedLevel(characterLevel); // Set the selected level to the character's level

        // Fetch class progression for the selected character level
        const progressionResponse = await axios.get(`http://127.0.0.1:5555/api/class_progression/${characterClassId}/level/${characterLevel}`);
        const progression = progressionResponse.data;
        setMaxSpells(progression.available_spell.spells);   // Set the max number of spells
        setMaxCantrips(progression.available_spell.cantrips);  // Set the max number of cantrips

        // Get the maximum spell level available at this character level
        const maxAvailableSpellLevel = progression.available_spell_level || 1; // Default to level 1 if missing

        // Fetch the spells for the class (up to level 9 but only show available spell levels)
        const spellsResponse = await axios.get(`http://127.0.0.1:5555/spells/class/${characterClassId}/level/9`);
        const allSpells = spellsResponse.data;

        // Filter the spells based on available spell levels (spells less than or equal to available_spell_level)
        const filteredSpellsByAvailableLevels = allSpells.filter(spell =>
          spell.level <= maxAvailableSpellLevel
        );

        // Set available spell levels for toggle buttons (levels up to the maximum spell level available)
        const uniqueSpellLevels = [...new Set(filteredSpellsByAvailableLevels.map(spell => spell.level))];
        setAvailableSpellLevels(uniqueSpellLevels);

        // Set the initial filteredSpells state to the filtered spells
        setSpells(allSpells);
        setFilteredSpells(filteredSpellsByAvailableLevels); // Ensure filteredSpells is updated on page load

        setLoading(false);
      } catch (error) {
        console.error('Error fetching character data and spells:', error);
        setLoading(false);
      }
    };

    fetchCharacterData();
  }, [characterId]);

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
      navigate(`/character/create/background/${systemId}/${characterId}`);
    } catch (error) {
      console.error('Error updating spells:', error);
    }
  };

  // Handle spell level toggle buttons
  const handleSpellLevelToggle = (level) => {
    setSelectedSpellLevels(prevLevels => 
      prevLevels.includes(level) 
        ? prevLevels.filter(l => l !== level)  // Remove if already selected
        : [...prevLevels, level]  // Add if not selected
    );
  };

  // Filter spells based on selected spell levels
  useEffect(() => {
    if (selectedSpellLevels.length > 0) {
      setFilteredSpells(spells.filter(spell => selectedSpellLevels.includes(spell.level)));
    } else {
      // If no spell level is selected, show spells based on the class's available spell levels at the current character level
      setFilteredSpells(spells.filter(spell => availableSpellLevels.includes(spell.level)));
    }
  }, [selectedSpellLevels, spells, availableSpellLevels]);

  // Handle character level change
const handleCharacterLevelChange = async (event) => {
  const newLevel = parseInt(event.target.value);
  setSelectedLevel(newLevel);

  try {
    // Fetch updated class progression based on the new character level
    const characterResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
    const characterClassId = characterResponse.data.class.id;

    const progressionResponse = await axios.get(`http://127.0.0.1:5555/api/class_progression/${characterClassId}/level/${newLevel}`);
    const progression = progressionResponse.data;
    setMaxSpells(progression.available_spell.spells);
    setMaxCantrips(progression.available_spell.cantrips);

    // Set available spell levels for the new character level
    const maxAvailableSpellLevel = progression.available_spell.available_spell_level || 1; // Default to level 1 if missing
    console.log(maxAvailableSpellLevel)
    // Fetch all spells (up to level 9) and filter based on available spell levels
    const spellsResponse = await axios.get(`http://127.0.0.1:5555/spells/class/${characterClassId}/level/9`);
    const allSpells = spellsResponse.data;

    // Filter spells based on the available spell levels (<= available_spell_level)
    const filteredSpellsByAvailableLevels = allSpells.filter(spell => spell.level <= maxAvailableSpellLevel);

    // Update state with new filtered spells and available levels
    setSpells(allSpells);
    setFilteredSpells(filteredSpellsByAvailableLevels);

    // Update available spell levels for toggles
    const uniqueSpellLevels = [...new Set(filteredSpellsByAvailableLevels.map(spell => spell.level))];
    setAvailableSpellLevels(uniqueSpellLevels);

  } catch (error) {
    console.error('Error fetching spells or class progression:', error);
  }
};


  // Filter spells based on search term
  const handleSearch = (event) => {
    const search = event.target.value.toLowerCase();
    setSearchTerm(search);
    setFilteredSpells(spells.filter(spell => 
      spell.name.toLowerCase().includes(search) || 
      spell.description.toLowerCase().includes(search)
    ));
  };

  if (loading) {
    return <div>Loading spells...</div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        <h1 className="text-4xl font-bold text-center text-accent mb-8">Select Spells</h1>

        {/* Top Navigation - Back and Reset Buttons */}
        <div className="flex justify-between mb-8">
          <button
            onClick={() => navigate(`/character/create/ability-scores/${systemId}/${characterId}`)} // Go back to previous page
            className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
          >
            ← Back
          </button>

          <button
            onClick={handleReset}
            className="bg-red-600 text-white py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
          >
            Reset
          </button>

          {/* Next Button */}
          <button
            onClick={handleSubmit}
            className="bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300"
          >
            Next
          </button>
        
        </div>

        {/* Search Bar */}
        <div className="mb-8 text-center">
          <input
            type="text"
            placeholder="Search spells..."
            value={searchTerm}
            onChange={handleSearch}
            className="p-2 rounded bg-secondary text-text w-full max-w-md"
          />
        </div>

        {/* Character Level Selection */}
        <div className="mb-8 text-center">
          <label className="text-xl mr-4">Select Character Level:</label>
          <select value={selectedLevel} onChange={handleCharacterLevelChange} className="p-2 rounded bg-secondary text-text">
            {[...Array(20).keys()].map(level => (
              <option key={level + 1} value={level + 1}>{level + 1}</option>
            ))}
          </select>
        </div>

        {/* Filter Buttons for Spell Levels */}
        <div className="mb-8 flex justify-center space-x-2">
          {availableSpellLevels.map(level => (
            level <= selectedLevel && (
              <button
                key={level}
                className={`py-2 px-4 rounded ${selectedSpellLevels.includes(level) ? 'bg-accent text-background' : 'bg-secondary text-text'}`}
                onClick={() => handleSpellLevelToggle(level)}
              >
                -{level}-
              </button>
            )
          ))}
        </div>

        {/* Selected Spell Count */}
        <div className="text-center mb-4">
          <p className="text-xl">Cantrips: {selectedSpells.filter(s => s.level === 0).length}/{maxCantrips}</p>
          <p className="text-xl">Spells: {selectedSpells.filter(s => s.level > 0).length}/{maxSpells}</p>
        </div>

        {/* Spell Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredSpells.map(spell => (
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
      </div>
    </div>
  );
};

export default SelectSpellsPage;
