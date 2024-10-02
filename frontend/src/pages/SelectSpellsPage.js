import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const SelectSpellsPage = () => {
  const { systemId, characterId } = useParams();
  const [spells, setSpells] = useState([]);
  const [filteredSpells, setFilteredSpells] = useState([]);
  const [selectedSpells, setSelectedSpells] = useState([]); // Store selected spell IDs
  const [maxSpells, setMaxSpells] = useState(0);
  const [maxCantrips, setMaxCantrips] = useState(0);
  const [selectedLevel, setSelectedLevel] = useState(1);
  const [selectedSpellLevels, setSelectedSpellLevels] = useState([]);
  const [availableSpellLevels, setAvailableSpellLevels] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false); // Control the modal
  const [modalMessage, setModalMessage] = useState(''); // Store modal message
  const navigate = useNavigate();

  // Fetch character data, spells, and progression on load
  useEffect(() => {
    const fetchCharacterData = async () => {
      try {
        const characterResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        const characterLevel = characterResponse.data.level || 1;
        const characterClassId = characterResponse.data.class.id;

        setSelectedLevel(characterLevel);

        // Fetch class progression for the character level
        const progressionResponse = await axios.get(`http://127.0.0.1:5555/api/class_progression/${characterClassId}/level/${characterLevel}`);
        const progression = progressionResponse.data;
        setMaxSpells(progression.available_spell.spells);
        setMaxCantrips(progression.available_spell.cantrips);

        const maxAvailableSpellLevel = progression.available_spell_level || 1;

        // Fetch spells up to level 9 and filter based on available spell levels
        const spellsResponse = await axios.get(`http://127.0.0.1:5555/spells/class/${characterClassId}/level/9`);
        const allSpells = spellsResponse.data;

        const filteredSpellsByAvailableLevels = allSpells.filter(spell => spell.level <= maxAvailableSpellLevel);
        setSpells(allSpells);
        setFilteredSpells(filteredSpellsByAvailableLevels);

        const uniqueSpellLevels = [...new Set(filteredSpellsByAvailableLevels.map(spell => spell.level))];
        setAvailableSpellLevels(uniqueSpellLevels);

        // Pre-select spells stored in system_data under "selected_spells"
        const selectedSpellIds = characterResponse.data.system_data?.selected_spells || [];
        setSelectedSpells(selectedSpellIds); // Set the selected spells based on system_data

        setLoading(false);
      } catch (error) {
        console.error('Error fetching character data and spells:', error);
        setLoading(false);
      }
    };

    fetchCharacterData();
  }, [characterId]);

  // Handle spell selection/unselection
  const handleSpellSelect = (spell) => {
    const isSelected = selectedSpells.includes(spell.id);

    if (!isSelected) {
      if (spell.level === 0 && selectedSpells.filter(spellId => spells.find(s => s.id === spellId)?.level === 0).length >= maxCantrips) {
        setModalMessage(`You can only select up to ${maxCantrips} cantrips.`);
        setShowModal(true);
        return;
      }

      if (spell.level > 0 && selectedSpells.filter(spellId => spells.find(s => s.id === spellId)?.level > 0).length >= maxSpells) {
        setModalMessage(`You can only select up to ${maxSpells} spells.`);
        setShowModal(true);
        return;
      }
    }

    setSelectedSpells((prevSelected) =>
      isSelected ? prevSelected.filter(spellId => spellId !== spell.id) : [...prevSelected, spell.id]
    );
  };

  // Close modal
  const closeModal = () => {
    setShowModal(false);
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
        spell_ids: selectedSpells,
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
        ? prevLevels.filter(l => l !== level)
        : [...prevLevels, level]
    );
  };

  // Filter spells based on selected spell levels
  useEffect(() => {
    if (selectedSpellLevels.length > 0) {
      setFilteredSpells(spells.filter(spell => selectedSpellLevels.includes(spell.level)));
    } else {
      setFilteredSpells(spells.filter(spell => availableSpellLevels.includes(spell.level)));
    }
  }, [selectedSpellLevels, spells, availableSpellLevels]);

  // Filter spells based on search term
  const handleSearch = (event) => {
    const search = event.target.value.toLowerCase();
    setSearchTerm(search);
    setFilteredSpells(spells.filter(spell =>
      spell.name.toLowerCase().includes(search) ||
      spell.description.toLowerCase().includes(search)
    ));
  };

  // Handle character level change
  const handleCharacterLevelChange = async (event) => {
    const newLevel = parseInt(event.target.value);
    setSelectedLevel(newLevel);

    try {
      const characterResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
      const characterClassId = characterResponse.data.class.id;

      const progressionResponse = await axios.get(`http://127.0.0.1:5555/api/class_progression/${characterClassId}/level/${newLevel}`);
      const progression = progressionResponse.data;
      setMaxSpells(progression.available_spell.spells);
      setMaxCantrips(progression.available_spell.cantrips);

      const maxAvailableSpellLevel = progression.available_spell.available_spell_level || 1;
      const spellsResponse = await axios.get(`http://127.0.0.1:5555/spells/class/${characterClassId}/level/9`);
      const allSpells = spellsResponse.data;

      const filteredSpellsByAvailableLevels = allSpells.filter(spell => spell.level <= maxAvailableSpellLevel);
      setSpells(allSpells);
      setFilteredSpells(filteredSpellsByAvailableLevels);

      const uniqueSpellLevels = [...new Set(filteredSpellsByAvailableLevels.map(spell => spell.level))];
      setAvailableSpellLevels(uniqueSpellLevels);
    } catch (error) {
      console.error('Error fetching spells or class progression:', error);
    }
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
            onClick={() => navigate(`/character/create/ability-scores/${systemId}/${characterId}`)}
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
          <p className="text-xl">Cantrips: {selectedSpells.filter(spellId => spells.find(s => s.id === spellId)?.level === 0).length}/{maxCantrips}</p>
          <p className="text-xl">Spells: {selectedSpells.filter(spellId => spells.find(s => s.id === spellId)?.level > 0).length}/{maxSpells}</p>
        </div>

        {/* Spell Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredSpells.map(spell => (
            <div
              key={spell.id}
              className={`p-4 rounded-lg shadow-lg cursor-pointer ${selectedSpells.includes(spell.id) ? 'bg-accent text-background' : 'bg-secondary'}`}
              onClick={() => handleSpellSelect(spell)}
            >
              <h3 className="text-xl font-bold">{spell.name}</h3>
              <p>{spell.description}</p>
              <p className="text-black text-center text-lg mt-4">Level: {spell.level}</p>
              <p>School: {spell.school}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Custom Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-secondary p-6 rounded-lg max-w-md w-full relative">
            <button className="absolute top-2 right-4 text-background text-2xl" onClick={closeModal}>X</button>
            <h2 className="text-2xl font-bold text-center mb-4">Max Spells Reached</h2>
            <p className="text-center text-lg mb-4">{modalMessage}</p>
            <button
              className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300 mx-auto block"
              onClick={closeModal}
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default SelectSpellsPage;
