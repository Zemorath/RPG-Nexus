import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const SelectSkillsFeatsPage = () => {
  const { systemId, characterId } = useParams();
  const [classSkills, setClassSkills] = useState([]);
  const [raceSkills, setRaceSkills] = useState([]);
  const [feats, setFeats] = useState([]);
  const [selectedSkills, setSelectedSkills] = useState([]);
  const [selectedFeats, setSelectedFeats] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Fetch skills and feats
  useEffect(() => {
    const fetchSkillsFeats = async () => {
      try {
        const skillResponse = await axios.get(`http://127.0.0.1:5555/skills/rpgsystem/${systemId}`);
        const featResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}/feats`);
        
        setClassSkills(skillResponse.data.class_skills);
        setRaceSkills(skillResponse.data.race_skills);
        setFeats(featResponse.data.feats);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching skills and feats:', error);
        setLoading(false);
      }
    };

    fetchSkillsFeats();
  }, [systemId, characterId]);

  const handleSkillSelect = (skillId) => {
    setSelectedSkills((prevSelected) =>
      prevSelected.includes(skillId)
        ? prevSelected.filter((id) => id !== skillId)
        : [...prevSelected, skillId]
    );
  };

  const handleFeatSelect = (featId) => {
    setSelectedFeats((prevSelected) =>
      prevSelected.includes(featId)
        ? prevSelected.filter((id) => id !== featId)
        : [...prevSelected, featId]
    );
  };

  const handleSubmit = async () => {
    try {
      await axios.post(`http://127.0.0.1:5555/api/characters/update-skills`, {
        character_id: characterId,
        skill_ids: selectedSkills,
      });
      await axios.post(`http://127.0.0.1:5555/api/characters/update-feats`, {
        character_id: characterId,
        feat_ids: selectedFeats,
      });
      // Navigate to the next step
      navigate(`/character/create/equipment/${systemId}/${characterId}`);
    } catch (error) {
      console.error('Error updating skills and feats:', error);
    }
  };

  if (loading) {
    return <div>Loading skills and feats...</div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        <h1 className="text-4xl font-bold text-center text-accent mb-8">Select Skills and Feats</h1>

        {/* Class Skills */}
        <h2 className="text-2xl font-bold mb-4">Class Skills</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {classSkills.map((skill) => (
            <div
              key={skill.id}
              className={`p-4 rounded-lg shadow-lg cursor-pointer ${selectedSkills.includes(skill.id) ? 'bg-accent text-background' : 'bg-secondary'}`}
              onClick={() => handleSkillSelect(skill.id)}
            >
              <h3 className="text-xl font-bold">{skill.name}</h3>
              <p>{skill.description}</p>
            </div>
          ))}
        </div>

        {/* Race Skills */}
        <h2 className="text-2xl font-bold mb-4">Race Skills</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {raceSkills.map((skill) => (
            <div
              key={skill.id}
              className={`p-4 rounded-lg shadow-lg cursor-pointer ${selectedSkills.includes(skill.id) ? 'bg-accent text-background' : 'bg-secondary'}`}
              onClick={() => handleSkillSelect(skill.id)}
            >
              <h3 className="text-xl font-bold">{skill.name}</h3>
              <p>{skill.description}</p>
            </div>
          ))}
        </div>

        {/* Feats */}
        <h2 className="text-2xl font-bold mb-4">Feats</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {feats.map((feat) => (
            <div
              key={feat.id}
              className={`p-4 rounded-lg shadow-lg cursor-pointer ${selectedFeats.includes(feat.id) ? 'bg-accent text-background' : 'bg-secondary'}`}
              onClick={() => handleFeatSelect(feat.id)}
            >
              <h3 className="text-xl font-bold">{feat.name}</h3>
              <p>{feat.description}</p>
            </div>
          ))}
        </div>

        {/* Submit Button */}
        <button
          onClick={handleSubmit}
          className="mt-8 bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300 block mx-auto"
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default SelectSkillsFeatsPage;
