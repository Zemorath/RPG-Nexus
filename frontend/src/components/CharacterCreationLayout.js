// src/components/CharacterCreationLayout.js
import React, { useState, useEffect } from 'react';
import { Outlet, useLocation, useParams, Link } from 'react-router-dom';
import Navbar from './Navbar';
import axios from 'axios';

// Base steps for all systems
const baseSteps = [
  { name: 'Race', path: '/character/create/race', required: true },
  { name: 'Class', path: '/character/create/class', required: true },
  { name: 'Scores', path: '/character/create/ability-scores', required: true },
//   { name: 'Skills', path: '/character/create/skills', required: true },
  { name: 'Spells', path: '/character/create/spells', required: false },
  { name: 'Background', path: '/character/create/background', required: false },
  { name: 'Equipment', path: '/character/create/equipment', required: true },
  { name: 'Summary', path: '/character/summary', required: true },
];

// System-specific step exclusions (e.g., Mothership skips Spells and Background)
const systemStepExclusions = {
  6: ['Spells'], // Mothership (systemId: 6)
  // Add other systems if needed
};

const CharacterCreationLayout = ({ onLogout }) => {
  const location = useLocation();
  const { systemId, characterId } = useParams();
  const [characterProgress, setCharacterProgress] = useState(null);
  const [loading, setLoading] = useState(true);

  // Fetch character progress on mount
  useEffect(() => {
    if (characterId) {
      const fetchCharacterProgress = async () => {
        try {
          const response = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
          setCharacterProgress(response.data); // Expecting { completed_steps: ['Race', 'Class', ...] } or similar
          setLoading(false);
        } catch (error) {
          console.error('Error fetching character progress:', error);
          setLoading(false);
        }
      };
      fetchCharacterProgress();
    } else {
      setLoading(false); // No characterId means new character, no progress yet
    }
  }, [characterId]);

  // Filter steps based on systemId
  const activeSteps = baseSteps.filter(step => {
    const exclusions = systemStepExclusions[systemId] || [];
    return !exclusions.includes(step.name);
  });

  // Determine current step and completion status
  const currentStepIndex = activeSteps.findIndex(step => location.pathname.includes(step.path));
  const completedSteps = characterProgress?.completed_steps || [];
  const isCharacterComplete = characterProgress?.is_complete || false;

  if (loading) {
    return (
      <div className="min-h-screen bg-background text-text flex items-center justify-center">
        <div>Loading...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-background text-text">
      <Navbar onLogout={onLogout} />
      {/* Progress Tracker */}
      <div className="bg-primary p-4 shadow-md">
        <div className="container mx-auto flex justify-center space-x-6">
          {activeSteps.map((step, index) => {
            const isCompleted = isCharacterComplete || completedSteps.includes(step.name) || index < currentStepIndex;
            const stepPath = `${step.path}/${systemId}/${characterId}`;

            return (
              <div key={index} className="flex items-center">
                <Link
                  to={isCompleted ? stepPath : '#'} // Only clickable if completed
                  className={`flex flex-col items-center ${!isCompleted ? 'cursor-not-allowed' : ''}`}
                >
                  <div
                    className={`w-10 h-10 rounded-full flex items-center justify-center font-bold transition-all duration-300 ${
                      isCompleted ? 'bg-accent text-background' : 'bg-secondary text-text'
                    }`}
                  >
                    {index + 1}
                  </div>
                  <span className="text-text text-sm mt-1">{step.name}</span>
                </Link>
                {index < activeSteps.length - 1 && (
                  <div
                    className={`h-1 w-12 ${isCompleted && index < currentStepIndex ? 'bg-accent' : 'bg-secondary'}`}
                  />
                )}
              </div>
            );
          })}
        </div>
      </div>
      <div className="container mx-auto p-8">
        <Outlet />
      </div>
    </div>
  );
};

export default CharacterCreationLayout;