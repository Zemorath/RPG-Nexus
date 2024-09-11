import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const SelectClassPage = () => {
  const [classes, setClasses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedClass, setSelectedClass] = useState(null); // To store the selected class for the modal
  const { systemId, characterId } = useParams(); // Get the RPG system ID and character ID from URL params
  const navigate = useNavigate();

  // Fetch the available classes for the selected RPG system
  useEffect(() => {
    const fetchClasses = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5555/api/classes/rpgsystem/${systemId}`);
        setClasses(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching classes:', error);
        setLoading(false);
      }
    };

    fetchClasses();
  }, [systemId]);

  const handleClassSelect = (cls) => {
    setSelectedClass(cls); // Set the selected class for the modal
  };

  const handleClassConfirm = async () => {
    try {
      // Send a request to save the selected class to the character in the backend
      const response = await axios.post(`http://127.0.0.1:5555/api/characters/update-class`, {
        class_id: selectedClass.id, // The selected class ID
        character_id: characterId // The character ID
      });
  
      // Navigate to the next step (Assign Ability Scores)
      navigate(`/character/create/ability-scores/${characterId}`);
    } catch (error) {
      console.error('Error saving class:', error);
    }
  };
  

  const handleCloseModal = () => {
    setSelectedClass(null); // Close the modal
  };

  const handleBackButton = () => {
    navigate(`/character/create/race/${characterId}`); // Navigate back to the SelectRacePage
  };

  if (loading) {
    return <div className="text-center text-text text-lg">Loading Classes...</div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        <div className="flex justify-between mb-8">
          <button
            className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
            onClick={handleBackButton}
          >
            ←
          </button>
          <h1 className="text-4xl font-bold text-center text-accent mx-auto">Select a Class</h1>
          <button
            className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
            onClick={() => navigate('/')} // Navigate to home
          >
            Home
          </button>
        </div>

        <p className="text-center mb-10 text-lg">Choose a class for your character.</p>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {classes.map(cls => (
            <div
              key={cls.id}
              className="bg-secondary p-6 rounded-lg shadow-lg hover:shadow-2xl hover:bg-accent hover:text-background transition-all duration-300 cursor-pointer transform hover:scale-105"
              onClick={() => handleClassSelect(cls)}
            >
              <div className="text-center text-2xl font-bold mb-4">{cls.name}</div>
              <p className="text-center mb-4">
                {cls.description.length > 120 ? `${cls.description.slice(0, 120)}...` : cls.description}
              </p>
            </div>
          ))}
        </div>

        {/* Modal Popup */}
        {selectedClass && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50" onClick={handleCloseModal}>
            <div className="bg-secondary p-8 rounded-lg shadow-lg max-w-xl w-full relative" onClick={(e) => e.stopPropagation()}>
              <button
                className="absolute top-2 right-2 text-background text-lg"
                onClick={handleCloseModal}
              >
                X
              </button>
              <h2 className="text-2xl font-bold mb-4">{selectedClass.name}</h2>
              <p className="mt-4"><strong>Description:</strong> {selectedClass.description}</p>
              <p className="mt-4"><strong>Hit Die:</strong> {selectedClass.hit_die}</p>
              <p className="mt-4"><strong>Primary Ability:</strong> {selectedClass.primary_ability}</p>

              <button
                className="mt-6 bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
                onClick={handleClassConfirm}
              >
                Confirm Class
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default SelectClassPage;
