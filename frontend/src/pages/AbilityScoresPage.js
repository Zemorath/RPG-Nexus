import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const AssignmentRow = ({ abilityScores, availableScores, onAssign }) => {
  return (
    <div className="grid grid-cols-6 gap-4 mb-8">
      {abilityScores.map((ability) => (
        <div key={ability} className="bg-secondary p-4 rounded-lg">
          <h3 className="text-accent text-lg font-bold mb-2">{ability}</h3>
          <select
            onChange={(e) => onAssign(ability, parseInt(e.target.value))}
            className="bg-primary text-text border border-accent p-2 w-full text-center rounded-lg"
          >
            <option value="">Assign</option>
            {availableScores.length > 0 ? (
              availableScores.map((score) => (
                <option key={score} value={score}>
                  {score}
                </option>
              ))
            ) : (
              <option value="">No scores available</option>
            )}
          </select>
        </div>
      ))}
    </div>
  );
};

const AbilityScoreCard = ({ ability, score, onOverride }) => {
  const [isOverriding, setIsOverriding] = useState(false);
  const [overrideValue, setOverrideValue] = useState(score);

  useEffect(() => {
    setOverrideValue(score);
  }, [score]);

  const handleOverride = () => {
    onOverride(ability, parseInt(overrideValue));
    setIsOverriding(false);
  };

  const calculateModifier = (score) => {
    return Math.floor((score - 10) / 2);
  };

  return (
    <div className="bg-secondary p-6 rounded-lg shadow-lg w-full max-w-xs">
      <div className="bg-primary text-accent p-3 rounded-t-lg text-center">
        <h2 className="text-xl font-bold">{ability}</h2>
      </div>
      <div className="p-3 space-y-2">
        <div className="text-center">
          <span className="text-accent text-2xl font-bold">{score}</span>
          <span className="text-text ml-2">({calculateModifier(score)})</span>
        </div>
        {isOverriding ? (
          <div className="flex items-center justify-between">
            <input
              type="number"
              value={overrideValue}
              onChange={(e) => setOverrideValue(e.target.value)}
              className="bg-primary text-text border border-accent p-2 w-20 text-center rounded-lg"
            />
            <button
              onClick={handleOverride}
              className="bg-accent text-background py-1 px-3 rounded hover:bg-text hover:text-background transition duration-300"
            >
              Save
            </button>
          </div>
        ) : (
          <button
            onClick={() => setIsOverriding(true)}
            className="bg-accent text-background py-1 px-3 rounded hover:bg-text hover:text-background transition duration-300 w-full"
          >
            Override
          </button>
        )}
      </div>
    </div>
  );
};

const AbilityScoresPage = () => {
  const { systemId, characterId } = useParams();
  const [abilityScores, setAbilityScores] = useState([]);
  const [scores, setScores] = useState({});
  const [generationMethod, setGenerationMethod] = useState('manual');
  const [availableScores, setAvailableScores] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchAbilityScores = async () => {
      try {
        const systemResponse = await axios.get(`http://127.0.0.1:5555/api/rpgsystems/${systemId}/default_settings`);
        const systemSettings = systemResponse.data;
        setAbilityScores(systemSettings.ability_scores);

        const characterResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        const characterScores = characterResponse.data.ability_scores || {};
        
        // Set scores directly from the character data
        setScores(characterScores);

        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchAbilityScores();
  }, [systemId, characterId]);

  const handleMethodChange = async (method) => {
    setGenerationMethod(method);
    if (method === 'standard_array' || method === 'point_buy') {
      try {
        const response = await axios.post(
          `http://127.0.0.1:5555/api/characters/generate-ability-scores/${systemId}/${method}`,
          {},
          {
            headers: {
              'Content-Type': 'application/json',
            },
          }
        );
        
        let newScores = [];
        if (method === 'standard_array' && response.data.standard_array) {
          newScores = response.data.standard_array;
        } else if (method === 'point_buy' && response.data.available_scores) {
          newScores = response.data.available_scores;
        }

        if (newScores.length > 0) {
          setAvailableScores(newScores);
        } else {
          console.error('No scores found in response data');
          setAvailableScores([]);
        }
      } catch (error) {
        console.error('Error generating ability scores:', error);
        setAvailableScores([]);
      }
    } else {
      setAvailableScores([]);
    }
  };

  const handleAssign = (ability, value) => {
    setScores(prev => ({
      ...prev,
      [ability]: value
    }));
    setAvailableScores(prev => prev.filter(score => score !== value));
  };

  const handleOverride = (ability, value) => {
    setScores(prev => ({
      ...prev,
      [ability]: value
    }));
  };

  const handleSubmit = async () => {
    try {
      await axios.post(`http://127.0.0.1:5555/api/characters/update-ability-scores`, {
        character_id: characterId,
        ability_scores: scores
      });
      navigate(`/character/create/spells/${systemId}/${characterId}`);
    } catch (error) {
      console.error('Error submitting scores:', error);
    }
  };

  if (loading) {
    return <div className="min-h-screen bg-background text-text flex items-center justify-center">
      <div className="text-2xl">Loading...</div>
    </div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="flex justify-between mt-8">
        <button onClick={() => navigate(`/character/create/class/${systemId}/${characterId}`)} className="bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300">Back</button>
        <button onClick={handleSubmit} className="bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300">Next</button>
      </div>

      <div className="container mx-auto">
        <h1 className="text-4xl font-bold text-center text-accent mb-8">Assign Ability Scores</h1>

        <div className="text-center mb-8">
          <select 
            value={generationMethod} 
            onChange={(e) => handleMethodChange(e.target.value)} 
            className="bg-secondary text-text py-2 px-4 rounded-lg border border-accent"
          >
            <option value="manual">Manual</option>
            <option value="standard_array">Standard Array</option>
            <option value="point_buy">Point Buy</option>
          </select>
        </div>

        {(generationMethod === 'standard_array' || generationMethod === 'point_buy') && (
          <AssignmentRow
            abilityScores={abilityScores}
            availableScores={availableScores}
            onAssign={handleAssign}
          />
        )}

        {generationMethod === 'manual' && (
          <div className="grid grid-cols-6 gap-4 mb-8">
            {abilityScores.map((ability) => (
              <div key={ability} className="bg-secondary p-4 rounded-lg">
                <h3 className="text-accent text-lg font-bold mb-2">{ability}</h3>
                <input
                  type="number"
                  value={scores[ability] || ''}
                  onChange={(e) => handleOverride(ability, parseInt(e.target.value))}
                  className="bg-primary text-text border border-accent p-2 w-full text-center rounded-lg"
                />
              </div>
            ))}
          </div>
        )}

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 justify-items-center">
          {abilityScores.map((ability) => (
            <AbilityScoreCard
              key={ability}
              ability={ability}
              score={scores[ability] || 0}
              onOverride={handleOverride}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default AbilityScoresPage;