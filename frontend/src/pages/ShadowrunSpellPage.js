import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";

const ShadowrunSpellPage = () => {
  const { systemId, characterId } = useParams();
  const SPELL_COST = 5; // Default Karma cost per spell
  const [karma, setKarma] = useState(null);
  const [customKarma, setCustomKarma] = useState("");
  const [characterLevel, setCharacterLevel] = useState(1);
  const [availableSpells, setAvailableSpells] = useState([]);
  const [selectedSpells, setSelectedSpells] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [modalMessage, setModalMessage] = useState("");
  const navigate = useNavigate();

  // Fetch character and spell data on mount
  useEffect(() => {
    const fetchCharacterData = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        setKarma(response.data.experience_points || 0);
        setCharacterLevel(response.data.level || 1);

        const spellsResponse = await axios.get(`http://127.0.0.1:5555/spells/shadowrun`);
        setAvailableSpells(spellsResponse.data);

        const systemData = response.data.system_data || {};
        const savedSpells = systemData.selected_spells || [];

        setSelectedSpells(savedSpells);
      } catch (error) {
        console.error("Error fetching character data or spells:", error);
      }
    };

    fetchCharacterData();
  }, [characterId]);

  // Handle Character Level Change
  const handleLevelChange = (event) => {
    setCharacterLevel(parseInt(event.target.value));
  };

  // Handle Karma Change
  const handleKarmaChange = (event) => {
    setCustomKarma(event.target.value);
  };

  // Submit Updated Karma and Level
  const handleSubmitLevelAndKarma = async () => {
    try {
      const response = await axios.post(`http://127.0.0.1:5555/api/characters/update-level`, {
        character_id: characterId,
        level: characterLevel,
        experience_points: customKarma ? parseInt(customKarma) : karma
      });
      setKarma(response.data.experience_points);
      setCharacterLevel(response.data.level);
    } catch (error) {
      console.error("Error updating character level and Karma:", error);
    }
  };

  // Handle Spell Selection
  const handleSpellSelect = (spellId) => {
    if (selectedSpells.includes(spellId)) {
      setSelectedSpells((prevSelected) => prevSelected.filter((id) => id !== spellId));
      setKarma((prevKarma) => prevKarma + SPELL_COST);
    } else {
      if (karma >= SPELL_COST) {
        setSelectedSpells((prevSelected) => [...prevSelected, spellId]);
        setKarma((prevKarma) => prevKarma - SPELL_COST);
      } else {
        setModalMessage(`Not enough Karma to purchase this spell. Requires ${SPELL_COST} Karma.`);
        setShowModal(true);
      }
    }
  };

  // Save Selected Spells
  const handleSubmitSpells = async () => {
    console.log("Submitting spells:", selectedSpells);
    console.log("Submitting remaining Karma:", karma);

    try {
      const response = await axios.post(`http://127.0.0.1:5555/characters/update-spells`, {
        character_id: characterId,
        spell_ids: selectedSpells,
        remaining_karma: karma,
      });

      console.log("Response from backend:", response.data)
      navigate(`/character/create/background/${systemId}/${characterId}`);
    } catch (error) {
      console.error("Error saving selected spells:", error);
    }
  };

  const closeModal = () => setShowModal(false);

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        {/* Navigation Buttons */}
        <div className="flex justify-between mb-4">
          <button
            onClick={() => navigate(`/character/create/previous-step/${systemId}/${characterId}`)}
            className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
          >
            ← Back
          </button>
          <button
            onClick={handleSubmitSpells}
            className="bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300"
          >
            Next →
          </button>
        </div>

        {/* Level and Karma Selection */}
        <div className="mb-4 text-center">
          <label className="text-xl mr-4">Select Character Level:</label>
          <select onChange={handleLevelChange} value={characterLevel} className="p-2 rounded bg-secondary text-text">
            {[...Array(20).keys()].map(level => (
              <option key={level + 1} value={level + 1}>{level + 1}</option>
            ))}
          </select>
        </div>

        <div className="mb-4 text-center">
          <label className="text-xl mr-4">Enter Total Karma:</label>
          <input
            type="number"
            value={customKarma}
            onChange={handleKarmaChange}
            placeholder={karma !== null ? karma.toString() : ""}
            className="p-2 rounded bg-secondary text-text"
          />
          <button
            onClick={handleSubmitLevelAndKarma}
            className="ml-4 bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 transition duration-300"
          >
            Update Karma & Level
          </button>
        </div>

        <div className="text-center mb-4 text-xl font-bold">
          Available Karma: {karma !== null ? karma : "Loading..."}
        </div>

        {/* Spell Selection Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {availableSpells.map((spell) => (
            <div
              key={spell.id}
              className={`p-4 rounded-lg shadow-lg cursor-pointer ${
                selectedSpells.includes(spell.id) ? "bg-accent text-background" : "bg-secondary"
              }`}
              onClick={() => handleSpellSelect(spell.id)}
            >
              <h3 className="text-xl font-bold">{spell.name}</h3>
              <p>{spell.description}</p>
              <p className="text-black text-center text-lg mt-4">Type: {spell.type}</p>
              <p>Range: {spell.range}</p>
              <p>Duration: {spell.duration}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Custom Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-secondary p-6 rounded-lg max-w-md w-full relative">
            <button className="absolute top-2 right-4 text-background text-2xl" onClick={closeModal}>X</button>
            <h2 className="text-2xl font-bold text-center mb-4">Insufficient Karma</h2>
            <p className="text-center text-lg mb-4">{modalMessage}</p>
            <button className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300 mx-auto block" onClick={closeModal}>Close</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ShadowrunSpellPage;
