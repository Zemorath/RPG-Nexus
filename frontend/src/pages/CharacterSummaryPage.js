import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import generateCharacterSheet from '../components/D&D_5e_CharacterSheet'; // Import the function here

const CharacterSummaryPage = () => {
  const { systemId, characterId } = useParams();
  const [character, setCharacter] = useState(null);
  const [calculatedCharacter, setCalculatedCharacter] = useState(null); // Add state for calculated character
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCharacter = async () => {
      try {
        // Fetch the character data
        const characterResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        setCharacter(characterResponse.data);

        // Fetch the calculated character data
        const calculatedResponse = await axios.get(`http://127.0.0.1:5555/api/characters/calculate/${characterId}`);
        setCalculatedCharacter(calculatedResponse.data);
      } catch (error) {
        console.error('Error fetching character data:', error);
      } finally {
        setLoading(false); // Update loading state after both calls are complete
      }
    };
  
    fetchCharacter();
  }, [characterId]);

  const handleGenerateCharacterSheet = () => {
    // Generate the PDF using the generateCharacterSheet function
    generateCharacterSheet(characterId);
  };

  if (loading) {
    return <div className="text-text">Loading character details...</div>;
  }

  if (!character || !calculatedCharacter) {
    return <div className="text-text">Character not found</div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        <h1 className="text-5xl font-bold text-accent mb-8 text-center">{character.name}</h1>

        {/* Character Info */}
        <div className="mb-8 p-6 bg-primary rounded-lg shadow-lg">
          <h2 className="text-3xl font-bold text-accent mb-4">Character Information</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
              <p><strong>Level:</strong> {character.level}</p>
              <p><strong>Health:</strong> {character.health}</p>
              <p><strong>Experience Points:</strong> {character.experience_points}</p>
              <p><strong>Race:</strong> {character.race ? character.race.name : 'None'}</p>
              <p><strong>Class:</strong> {character.class ? character.class.name : 'None'}</p>
              <p><strong>Background:</strong> {character.background ? character.background.name : 'None'}</p>
              <p><strong>Alignment:</strong> {character.alignment ? character.alignment.name : 'None'}</p>
              <p><strong>Inventory Weight Limit:</strong> {character.inventory_weight_limit}</p>
              <p><strong>Armor Class:</strong> {calculatedCharacter.armor_class}</p> {/* Armor Class */}
              <p><strong>Initiative:</strong> {calculatedCharacter.initiative}</p> {/* Initiative */}
              <p><strong>Proficiency Bonus:</strong> {calculatedCharacter.proficiency_bonus}</p> {/* Proficiency Bonus */}
            </div>
            <div>
              <h3 className="text-xl font-bold text-accent mt-4">Ability Scores</h3>
              {calculatedCharacter.ability_scores ? (
                <ul className="list-inside list-disc">
                  {Object.keys(calculatedCharacter.ability_scores).map((key) => {
                    const score = calculatedCharacter.ability_scores[key];
                    const displayedScore = score.override_score || score.total_score; // Display override_score if present, otherwise total_score
                    const modifier = score.modifier !== undefined ? ` (Modifier: ${score.modifier})` : ''; // Display modifier
                    return (
                      <li key={key}>
                        <strong>{key}:</strong> {displayedScore} {modifier}
                      </li>
                    );
                  })}
                </ul>
              ) : (
                <p>No ability scores available</p>
              )}
            </div>
          </div>
        </div>

        {/* Inventory Section */}
        <div className="mb-8 p-6 bg-secondary rounded-lg shadow-lg">
          <h2 className="text-3xl font-bold text-accent mb-4">Inventory</h2>
          {character.inventory.length > 0 ? (
            <ul className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {character.inventory.map((item) => (
                <li key={item.id} className="p-4 bg-primary rounded shadow">
                  <h3 className="text-lg font-bold text-accent">{item.name}</h3>
                  <p>Rarity: {item.rarity}</p>
                  <p>Weight: {item.weight} lbs</p>
                  <p>Cost: {item.cost} gold</p>
                  <p>Damage Type: {item.damage_type}</p>
                </li>
              ))}
            </ul>
          ) : (
            <p>No items in inventory</p>
          )}
        </div>

        {/* Action Buttons */}
        <div className="flex justify-center space-x-4">
          <button
            onClick={() => navigate(`/character/edit/${systemId}/${characterId}`)}
            className="bg-accent text-background py-2 px-6 rounded-lg hover:bg-text hover:text-background transition duration-300"
          >
            Edit Character
          </button>

          <button
            onClick={handleGenerateCharacterSheet} // Generate Character Sheet Button
            className="bg-accent text-background py-2 px-6 rounded-lg hover:bg-text hover:text-background transition duration-300"
          >
            Generate Character Sheet
          </button>

          <button
            onClick={() => navigate(`/dashboard`)}
            className="bg-accent text-background py-2 px-6 rounded-lg hover:bg-text hover:text-background transition duration-300"
          >
            Go to Dashboard
          </button>

          <button
            onClick={() => navigate(`/campaign/join/${systemId}/${characterId}`)}
            className="bg-accent text-background py-2 px-6 rounded-lg hover:bg-text hover:text-background transition duration-300"
          >
            Join Campaign
          </button>
        </div>
      </div>
    </div>
  );
};

export default CharacterSummaryPage;
