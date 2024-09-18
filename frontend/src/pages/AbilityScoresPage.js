import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const AbilityScoresPage = () => {
  const { systemId, characterId } = useParams();
  const [abilityScores, setAbilityScores] = useState([]);
  const [loading, setLoading] = useState(true);
  const [scores, setScores] = useState({});
  const navigate = useNavigate();

  // Fetch ability scores from the RPG system and the character's saved scores (if any)
  useEffect(() => {
    const fetchAbilityScores = async () => {
      try {
        // Fetch system default ability scores
        const systemResponse = await axios.get(`http://127.0.0.1:5555/api/rpgsystems/${systemId}/default_settings`);
        const systemSettings = systemResponse.data;
        setAbilityScores(systemSettings.ability_scores);

        // Fetch character's ability scores (if they exist)
        const characterResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        const characterScores = characterResponse.data.ability_scores || {};

        // Initialize scores with either saved character scores or default structure
        const initialScores = {};
        systemSettings.ability_scores.forEach((ability) => {
          initialScores[ability] = {
            total_score: characterScores[ability]?.total_score || '--',
            modifier: characterScores[ability]?.modifier || '--',
            base_score: characterScores[ability]?.base_score || '--',
            species_bonus: characterScores[ability]?.species_bonus || '--',
            ability_improvements: characterScores[ability]?.ability_improvements || '--',
            misc_bonus: characterScores[ability]?.misc_bonus || '--',
            set_score: characterScores[ability]?.set_score || '--',
            other_modifier: characterScores[ability]?.other_modifier || '--',
            override_score: characterScores[ability]?.override_score || 0 // Default to 0 if not set
          };
        });

        setScores(initialScores);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching ability scores and character data:', error);
        setLoading(false);
      }
    };

    fetchAbilityScores();
  }, [systemId, characterId]);

  // Handle score changes
  const handleScoreChange = (ability, field, value) => {
    setScores((prevScores) => ({
      ...prevScores,
      [ability]: {
        ...prevScores[ability],
        [field]: value === '' ? '--' : parseInt(value) || 0 // If empty, set '--', else use int or 0
      }
    }));
  };

  // Submit the ability scores and navigate to the next step
  const handleSubmit = async () => {
    try {
      // Ensure any fields left unchanged remain '--'
      const updatedScores = { ...scores };

      for (const ability in updatedScores) {
        for (const field in updatedScores[ability]) {
          if (updatedScores[ability][field] === '--' || updatedScores[ability][field] === '') {
            updatedScores[ability][field] = '--';
          }
        }
      }

      await axios.post(`http://127.0.0.1:5555/api/characters/update-ability-scores`, {
        character_id: characterId,
        ability_scores: updatedScores
      });

      // Navigate to the next step (placeholder URL for now)
      navigate(`/character/create/spells/${systemId}/${characterId}`);
    } catch (error) {
      console.error('Error submitting ability scores:', error);
    }
  };

  if (loading) {
    return <div>Loading Ability Scores...</div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="flex justify-between mt-8">
        {/* Back Button */}
        <button
          onClick={() => navigate(`/character/create/class/${systemId}/${characterId}`)}
          className="bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300"
        >
          Back
        </button>

        {/* Next Button */}
        <button
          onClick={handleSubmit}
          className="bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300"
        >
          Next
        </button>
      </div>
      <div className="container mx-auto">
        <h1 className="text-4xl font-bold text-center text-accent mb-8">Assign Ability Scores</h1>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 justify-items-center">
          {abilityScores.map((ability) => (
            <div key={ability} className="bg-secondary p-6 rounded-lg shadow-lg w-full max-w-xs"> {/* Keep width consistent */}
              {/* Ability Name Header with Bar */}
              <div className="bg-primary text-accent p-3 rounded-t-lg text-center">
                <h2 className="text-xl font-bold">{ability}</h2>
              </div>

              {/* Ability Stats */}
              <div className="p-3 space-y-2">
                <div className="flex justify-between">
                  <span>Total Score</span>
                  <span>{scores[ability].total_score || '--'}</span>
                </div>
                <div className="flex justify-between">
                  <span>Modifier</span>
                  <span>{scores[ability].modifier || '--'}</span>
                </div>
                <div className="flex justify-between">
                  <span>Base Score</span>
                  <span>{scores[ability].base_score || '--'}</span>
                </div>
                <div className="flex justify-between">
                  <span>Species Bonus</span>
                  <span>{scores[ability].species_bonus || '--'}</span>
                </div>
                <div className="flex justify-between">
                  <span>Ability Improvements</span>
                  <span>{scores[ability].ability_improvements || '--'}</span>
                </div>
                <div className="flex justify-between">
                  <span>Misc Bonus</span>
                  <span>{scores[ability].misc_bonus || '--'}</span>
                </div>
                <div className="flex justify-between">
                  <span>Set Score</span>
                  <span>{scores[ability].set_score || '--'}</span>
                </div>
                <div className="flex justify-between">
                  <span>Other Modifier</span>
                  <input
                    type="number"
                    value={scores[ability].other_modifier === '--' ? '' : scores[ability].other_modifier}
                    onChange={(e) => handleScoreChange(ability, 'other_modifier', e.target.value)}
                    className="bg-gray-700 text-white border border-gray-400 p-3 w-20 text-center rounded-lg"
                  />
                </div>
                <div className="flex justify-between">
                  <span>Override Score</span>
                  <input
                    type="number"
                    value={scores[ability].override_score === '--' ? '' : scores[ability].override_score}
                    onChange={(e) => handleScoreChange(ability, 'override_score', e.target.value)}
                    className="bg-gray-700 text-white border border-gray-400 p-3 w-20 text-center rounded-lg"
                  />
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AbilityScoresPage;
