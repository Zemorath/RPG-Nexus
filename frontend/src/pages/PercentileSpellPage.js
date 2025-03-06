import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const SelectSpellsPageCoC = () => {
  const { systemId, characterId } = useParams();
  const [spells, setSpells] = useState([]);
  const [filteredSpells, setFilteredSpells] = useState([]);
  const [selectedSpells, setSelectedSpells] = useState([]); // Store selected spell IDs
  const [maxSpells] = useState(3); // Fixed cap for CoC
  const [startingSanity, setStartingSanity] = useState(50); // Default Sanity from experience_points
  const [totalSanityCost, setTotalSanityCost] = useState(0); // Calculated Sanity cost
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [modalMessage, setModalMessage] = useState('');
  const navigate = useNavigate();

  // Fetch character data and spells on load
  useEffect(() => {
    const fetchCharacterData = async () => {
      try {
        const characterResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        const character = characterResponse.data;
        const sanity = character.experience_points || 50; // Use experience_points as Sanity
        setStartingSanity(sanity);

        // Load pre-selected spells from system_data
        const selectedSpellIds = character.system_data?.selected_spells || [];
        setSelectedSpells(selectedSpellIds);

        // Fetch all CoC spells
        const spellsResponse = await axios.get(`http://127.0.0.1:5555/spells/callofcthulhu`);
        const allSpells = spellsResponse.data;
        setSpells(allSpells);
        setFilteredSpells(allSpells);

        // Calculate initial Sanity cost
        const initialCost = calculateSanityCost(selectedSpellIds, allSpells);
        setTotalSanityCost(initialCost);

        setLoading(false);
      } catch (error) {
        console.error('Error fetching character data and spells:', error);
        setLoading(false);
      }
    };

    fetchCharacterData();
  }, [characterId, systemId]);

  // Calculate total Sanity cost by parsing description or defaulting to 1
  const calculateSanityCost = (spellIds, spellList) => {
    return spellIds.reduce((total, spellId) => {
      const spell = spellList.find(s => s.id === spellId);
      if (!spell || !spell.description) return total;

      // Parse Sanity cost from description (e.g., "Sanity cost: 1d6")
      const match = spell.description.match(/Sanity cost: (\d+d?\d*)/i);
      let cost = 1; // Default if no Sanity cost specified
      if (match) {
        const costStr = match[1];
        cost = costStr.includes('d') ? parseInt(costStr.split('d')[1]) : parseInt(costStr);
      }
      return total + (cost || 0);
    }, 0);
  };

  // Handle spell selection/unselection
  const handleSpellSelect = (spell) => {
    const isSelected = selectedSpells.includes(spell.id);
    let newSelectedSpells;

    if (isSelected) {
      newSelectedSpells = selectedSpells.filter(spellId => spellId !== spell.id);
    } else {
      if (selectedSpells.length >= maxSpells) {
        setModalMessage(`You can only select up to ${maxSpells} spells.`);
        setShowModal(true);
        return;
      }
      newSelectedSpells = [...selectedSpells, spell.id];
    }

    const newSanityCost = calculateSanityCost(newSelectedSpells, spells);
    if (newSanityCost > startingSanity * 0.5) {
      setModalMessage(`Warning: Total Sanity cost (${newSanityCost}) exceeds 50% of your starting Sanity (${startingSanity}). Proceed with caution.`);
      setShowModal(true);
    }

    setSelectedSpells(newSelectedSpells);
    setTotalSanityCost(newSanityCost);
  };

  // Close modal
  const closeModal = () => {
    setShowModal(false);
  };

  // Reset selected spells
  const handleReset = () => {
    setSelectedSpells([]);
    setTotalSanityCost(0);
  };

  // Submit selected spells
  const handleSubmit = async () => {
    try {
      await axios.post(`http://127.0.0.1:5555/api/characters/update-spells`, {
        character_id: characterId,
        spell_ids: selectedSpells,
      });
      await axios.put(`http://127.0.0.1:5555/api/characters/${characterId}`, {
        system_data: {
          selected_spells: selectedSpells,
          total_sanity_cost: totalSanityCost,
        },
      });
      navigate(`/character/create/background/${systemId}/${characterId}`);
    } catch (error) {
      console.error('Error updating spells:', error);
    }
  };

  // Filter spells based on search term
  const handleSearch = (event) => {
    const search = event.target.value.toLowerCase();
    setSearchTerm(search);
    setFilteredSpells(
      spells.filter(spell =>
        spell.name.toLowerCase().includes(search) ||
        (spell.description && spell.description.toLowerCase().includes(search))
      )
    );
  };

  if (loading) {
    return <div className="text-text text-center">Loading spells...</div>;
  }

  return (
    <div className="min-h-screen bg-primary text-text p-8">
      <div className="container mx-auto">
        <h1 className="text-4xl font-bold text-center text-accent mb-8">Select Spells</h1>
        <p className="text-center mb-8">
          Spells reflect your investigator’s brush with the Mythos. They cost Magic Points and Sanity. Choose wisely (up to {maxSpells}).
        </p>

        {/* Navigation */}
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

        {/* Selection Tracker */}
        <div className="text-center mb-4">
          <p className="text-xl">Spells Selected: {selectedSpells.length}/{maxSpells}</p>
          <p className="text-xl">Total Sanity Cost: {totalSanityCost} | Starting Sanity: {startingSanity}</p>
          <p className="text-xl">Magic Points: Variable (see spell details)</p>
        </div>

        {/* Spell Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredSpells.map(spell => {
            const sanityMatch = spell.description?.match(/Sanity cost: (\d+d?\d*)/i);
            const sanityCost = sanityMatch ? sanityMatch[1] : '1'; // Default to 1 if not found
            return (
              <div
                key={spell.id}
                className={`p-4 rounded-lg shadow-lg cursor-pointer ${selectedSpells.includes(spell.id) ? 'bg-accent text-background' : 'bg-secondary'}`}
                onClick={() => handleSpellSelect(spell)}
              >
                <h3 className="text-xl font-bold">{spell.name}</h3>
                <p>{spell.description || 'No description available'}</p>
                <p className="mt-2">Sanity Cost: {sanityCost}</p>
                <p>Magic Points: {spell.cost || 'Variable'}</p>
                <p>Casting Time: {spell.casting_time || 'Instant'}</p>
                <p>Duration: {spell.duration || 'Instant'}</p>
              </div>
            );
          })}
        </div>
      </div>

      {/* Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-secondary p-6 rounded-lg max-w-md w-full relative">
            <button className="absolute top-2 right-4 text-background text-2xl" onClick={closeModal}>X</button>
            <h2 className="text-2xl font-bold text-center mb-4">Spell Selection Warning</h2>
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

export default SelectSpellsPageCoC;