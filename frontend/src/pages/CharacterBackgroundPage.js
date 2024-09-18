import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const CharacterBackgroundPage = () => {
  const { systemId, characterId } = useParams();
  const [alignments, setAlignments] = useState([]);
  const [backgrounds, setBackgrounds] = useState([]);
  const [characterData, setCharacterData] = useState({
    name: '',
    alignment: '',
    background: '',
    description: {
      hair: '',
      skin: '',
      eyes: '',
      height: '',
      weight: '',
      age: '',
      gender: ''
    },
    traits: [],
    ideals: [],
    bonds: [],
    flaws: [],
    organizations: [],
    allies: [],
    enemies: [],
    other: [],
  });

  const [modalContent, setModalContent] = useState('');
  const [modalCategory, setModalCategory] = useState('');
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Fetch alignment and background data
  useEffect(() => {
    const fetchAlignmentAndBackgrounds = async () => {
      try {
        const alignmentResponse = await axios.get(`http://127.0.0.1:5555/api/alignments/system/${systemId}`);
        setAlignments(alignmentResponse.data);

        const backgroundResponse = await axios.get(`http://127.0.0.1:5555/api/backgrounds/system/${systemId}`);
        setBackgrounds(backgroundResponse.data);

        setLoading(false);
      } catch (error) {
        console.error('Error fetching alignments and backgrounds:', error);
        setLoading(false);
      }
    };

    fetchAlignmentAndBackgrounds();
  }, [systemId]);

  const handleAdd = (category) => {
    setModalCategory(category);
    setModalContent('');
    document.getElementById('modal').style.display = 'block'; // Show modal
  };

  const handleAccept = () => {
    setCharacterData((prev) => ({
      ...prev,
      [modalCategory]: [...prev[modalCategory], modalContent]
    }));
    document.getElementById('modal').style.display = 'none'; // Hide modal
  };

  const handleInputChange = (e, field, subfield) => {
    if (subfield) {
      setCharacterData((prev) => ({
        ...prev,
        [field]: {
          ...prev[field],
          [subfield]: e.target.value
        }
      }));
    } else {
      setCharacterData({
        ...characterData,
        [field]: e.target.value
      });
    }
  };

  const handleNextButton = async () => {
    try {
      await axios.post(`http://127.0.0.1:5555/api/characters/update-background`, {
        character_id: characterId,
        ...characterData
      });

      // Navigate to the next step (example: roll for health)
      navigate(`/character/create/health/${systemId}/${characterId}`);
    } catch (error) {
      console.error('Error updating character background:', error);
    }
  };

  if (loading) {
    return <div className="text-center text-text text-lg">Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        <div className="flex justify-between mb-8">
          <button
            className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
            onClick={() => navigate(`/character/create/spells/${systemId}/${characterId}`)} // Navigate back
          >
            ← Back
          </button>
          <h1 className="text-4xl font-bold text-center text-accent mx-auto">Character Background</h1>
          <button
            className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
            onClick={() => navigate('/')} // Navigate to home
          >
            Home
          </button>
        </div>

        {/* Name Field */}
        <label className="block mb-2 text-lg w-1/2 mx-auto">
          Name:
          <input 
            type="text" 
            value={characterData.name}
            onChange={(e) => handleInputChange(e, 'name')}
            className="input-field w-full bg-secondary text-text rounded px-4 py-2 mt-1"
            placeholder="Enter character's name"
          />
        </label>

        {/* Alignment Dropdown */}
        <label className="block mb-2 text-lg w-1/2 mx-auto">
          Alignment:
          <select 
            value={characterData.alignment}
            onChange={(e) => handleInputChange(e, 'alignment')}
            className="input-field w-full bg-secondary text-text rounded px-4 py-2 mt-1"
          >
            <option value="">Select Alignment</option>
            {alignments.map(alignment => (
              <option key={alignment.id} value={alignment.name}>{alignment.name}</option>
            ))}
          </select>
        </label>

        {/* Background Dropdown */}
        <label className="block mb-2 text-lg w-1/2 mx-auto">
          Background:
          <select 
            value={characterData.background}
            onChange={(e) => handleInputChange(e, 'background')}
            className="input-field w-full bg-secondary text-text rounded px-4 py-2 mt-1"
          >
            <option value="">Select Background</option>
            {backgrounds.map(bg => (
              <option key={bg.id} value={bg.name}>{bg.name}</option>
            ))}
          </select>
        </label>

        {/* Description Fields */}
        <h3 className="text-xl font-bold mt-6 text-center">Description</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4 w-3/4 mx-auto">
          {['hair', 'skin', 'eyes', 'height', 'weight', 'age', 'gender'].map((feature) => (
            <label key={feature} className="block mb-2 text-lg">
              {feature.charAt(0).toUpperCase() + feature.slice(1)}:
              <input 
                type="text" 
                value={characterData.description[feature]}
                onChange={(e) => handleInputChange(e, 'description', feature)}
                className="input-field w-full bg-secondary text-text rounded px-4 py-2 mt-1"
                placeholder={`Enter ${feature}`}
              />
            </label>
          ))}
        </div>

        {/* Addable Traits/Features */}
        <h3 className="text-xl font-bold mt-4 text-center">Traits and Features</h3>
        <div className="flex flex-wrap justify-center">
          {[
            { label: 'Traits', key: 'traits' },
            { label: 'Ideals', key: 'ideals' },
            { label: 'Bonds', key: 'bonds' },
            { label: 'Flaws', key: 'flaws' },
            { label: 'Organizations', key: 'organizations' },
            { label: 'Allies', key: 'allies' },
            { label: 'Enemies', key: 'enemies' },
            { label: 'Other', key: 'other' },
          ].map((category) => (
            <div key={category.key} className="mb-4 w-1/2 sm:w-1/4 p-2">
              <div className="bg-secondary p-4 rounded-lg shadow-lg text-center">
                <div className="flex justify-between items-center">
                  <span className="text-lg font-bold">{category.label}</span>
                  <button 
                    className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300 ml-4" 
                    onClick={() => handleAdd(category.key)}
                  >
                    Add
                  </button>
                </div>
                <ul className="list-disc pl-4 mt-2 text-sm">
                  {characterData[category.key].map((item, index) => (
                    <li key={index} className="bg-accent text-background p-2 rounded mb-1">{item}</li>
                  ))}
                </ul>
              </div>
            </div>
          ))}
        </div>

        {/* Modal for adding traits */}
        <div id="modal" className="fixed inset-0 z-50 hidden flex-items-center justify-center bg-black bg-opacity-50">
          <div className="bg-secondary p-8 rounded-lg shadow-lg max-w-xl w-full relative">
            <button
              className="absolute top-2 right-2 text-background text-lg"
              onClick={() => (document.getElementById('modal').style.display = 'none')}
            >
              X
            </button>
            <h3 className="text-2xl font-bold mb-4">Add {modalCategory}</h3>
            <textarea
              className="input-field w-full bg-secondary text-text rounded px-4 py-2 mt-1"
              value={modalContent}
              onChange={(e) => setModalContent(e.target.value)}
              placeholder={`Enter ${modalCategory}`}
            />
            <div className="mt-4">
              <button 
                className="bg-accent text-background py-2 px-4 rounded mr-2 hover:bg-text hover:text-background transition duration-300" 
                onClick={handleAccept}
              >
                Accept
              </button>
              <button 
                className="bg-red-600 text-white py-2 px-4 rounded"
                onClick={() => (document.getElementById('modal').style.display = 'none')}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>

        {/* Next Button */}
        <div className="flex justify-end mt-6">
          <button
            className="bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300"
            onClick={handleNextButton}
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
};

export default CharacterBackgroundPage;
