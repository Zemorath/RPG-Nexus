import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';
import { useAuth } from '../components/auth/auth'; // Update this import path as needed

const SelectRacePage = () => {
  const [races, setRaces] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedRace, setSelectedRace] = useState(null);
  const { systemId } = useParams();
  const navigate = useNavigate();
  const modalRef = useRef(null);
  
  const { user } = useAuth(); // Use the useAuth hook

  useEffect(() => {
    const fetchRaces = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5555/api/races/rpgsystem/${systemId}`, {
          withCredentials: true // Ensure cookies are sent with the request
        });
        setRaces(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching races:', error);
        setLoading(false);
        // Handle unauthorized access
        if (error.response && error.response.status === 401) {
          navigate('/login');
        }
      }
    };

    fetchRaces();
  }, [systemId, navigate]);

  const handleRaceSelect = (race) => {
    setSelectedRace(race);
  };

  const handleRaceConfirm = async () => {
    try {
      const response = await axios.post(`http://127.0.0.1:5555/api/characters/initialize`, {
        user_id: user.id,
        rpg_system_id: systemId,
        race_id: selectedRace.id
      }, {
        withCredentials: true // Ensure cookies are sent with the request
      });
  
      const characterId = response.data.id;
      navigate(`/character/create/class/${systemId}/${characterId}`);
    } catch (error) {
      console.error('Error initializing character with race:', error);
      // Handle unauthorized access
      if (error.response && error.response.status === 401) {
        navigate('/login');
      }
    }
  };

  const handleCloseModal = () => {
    setSelectedRace(null);
  };

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (modalRef.current && !modalRef.current.contains(event.target)) {
        handleCloseModal();
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [selectedRace]);

  if (loading) {
    return <div className="text-center text-text text-lg">Loading Races...</div>;
  }

  if (!user) {
    navigate('/login');
    return null;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        <h1 className="text-4xl font-bold text-center text-accent mb-8">Select a Race</h1>
        <p className="text-center mb-10 text-lg">Choose a race for your character.</p>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {races.map(race => (
            <div
              key={race.id}
              className="bg-secondary p-6 rounded-lg shadow-lg hover:shadow-2xl hover:bg-accent hover:text-background transition-all duration-300 cursor-pointer transform hover:scale-105"
              onClick={() => handleRaceSelect(race)}
            >
              <div className="text-center text-2xl font-bold mb-4">{race.name}</div>
              <p className="text-center mb-4">
                {race.description.length > 120 ? `${race.description.slice(0, 120)}...` : race.description}
              </p>
            </div>
          ))}
        </div>

        {selectedRace && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
            <div
              ref={modalRef}
              className="bg-secondary p-8 rounded-lg shadow-lg max-w-xl w-full relative"
            >
              <button
                className="absolute top-2 right-2 text-background text-lg"
                onClick={handleCloseModal}
              >
                X
              </button>
              <h2 className="text-2xl font-bold mb-4">{selectedRace.name}</h2>
              <p className="mt-4"><strong>Description:</strong> {selectedRace.description}</p>
              <p className="mt-4"><strong>Size:</strong> {selectedRace.size}</p>
              <p className="mt-4"><strong>Speed:</strong> {selectedRace.speed} ft</p>
              <p className="mt-4">
                <strong>Languages: </strong>
                {Array.isArray(selectedRace.languages)
                  ? selectedRace.languages.join(', ')
                  : JSON.parse(selectedRace.languages).join(', ')}
              </p>
              <p className="mt-4"><strong>Vision Type:</strong> {selectedRace.vision_type}</p>
              <p className="mt-4"><strong>Natural Weapons/Abilities:</strong> {selectedRace.natural_weapons}</p>

              <button
                className="mt-6 bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
                onClick={handleRaceConfirm}
              >
                Confirm Race
              </button>
            </div>
          </div>
        )}

        <button
          className="mt-6 bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
          onClick={() => navigate("/character/create")}
        >
          Back
        </button>
      </div>
    </div>
  );
};

export default SelectRacePage;