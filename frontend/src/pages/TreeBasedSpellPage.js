import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TreeNode from '../components/TreeNode';
import { useNavigate } from 'react-router-dom';

const TreeBasedSpellPage = ({ systemId, characterId }) => {
  const [xp, setXp] = useState(null);
  const [customXp, setCustomXp] = useState(""); // Input for manual XP entry
  const [availableTrees, setAvailableTrees] = useState([]);
  const [selectedTree, setSelectedTree] = useState(null);
  const [purchasedTrees, setPurchasedTrees] = useState({});
  const [characterLevel, setCharacterLevel] = useState(1);
  const navigate = useNavigate();

  // Fetch character data and available Force trees on load
  useEffect(() => {
    const fetchCharacterData = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        setXp(response.data.experience_points || 0);
        setCharacterLevel(response.data.level || 1);

        // Fetch available Force trees from the database
        const treesResponse = await axios.get(`http://127.0.0.1:5555/force-trees`);
        setAvailableTrees(treesResponse.data);

        // Extract purchased trees from system_data
        const systemData = response.data.system_data || {};
        setPurchasedTrees(systemData.purchased_trees || {});
      } catch (error) {
        console.error('Error fetching character data or trees:', error);
      }
    };

    fetchCharacterData();
  }, [characterId]);

  // Handle character level change
  const handleLevelChange = (event) => {
    const newLevel = parseInt(event.target.value);
    setCharacterLevel(newLevel);
  };

  // Handle custom XP input change
  const handleXpChange = (event) => {
    setCustomXp(event.target.value);
  };

  // Submit level and XP updates
  const handleSubmitLevelAndXp = async () => {
    try {
      const response = await axios.post(`http://127.0.0.1:5555/api/characters/update-level`, {
        character_id: characterId,
        level: characterLevel,
        experience_points: customXp ? parseInt(customXp) : xp
      });

      // Update XP and level based on response
      setXp(response.data.experience_points);
      setCharacterLevel(response.data.level);
    } catch (error) {
      console.error('Error updating character level and XP:', error);
    }
  };

  const handleTreeChange = (event) => {
    const treeId = parseInt(event.target.value);
    const tree = availableTrees.find(tree => tree.id === treeId);
    setSelectedTree(tree || null);
  };

  const handlePurchaseTree = (treeId, cost) => {
    if (xp >= cost) {
      setXp(xp - cost);
      // Update purchased trees in state and backend
      setPurchasedTrees(prev => ({ ...prev, [treeId]: [] }));
      axios.post(`http://127.0.0.1:5555/api/characters/purchase-tree`, {
        character_id: characterId,
        tree_id: treeId,
        xp_cost: cost,
      }).catch(error => console.error("Error purchasing tree:", error));
    }
  };

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
            onClick={() => navigate(`/character/create/next-step/${systemId}/${characterId}`)}
            className="bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300"
          >
            Next →
          </button>
        </div>

        {/* Character Level Selection */}
        <div className="mb-4 text-center">
          <label className="text-xl mr-4">Select Character Level:</label>
          <select onChange={handleLevelChange} value={characterLevel} className="p-2 rounded bg-secondary text-text">
            {[...Array(20).keys()].map(level => (
              <option key={level + 1} value={level + 1}>{level + 1}</option>
            ))}
          </select>
        </div>

        {/* Custom XP Input */}
        <div className="mb-4 text-center">
          <label className="text-xl mr-4">Enter Total XP:</label>
          <input
            type="number"
            value={customXp}
            onChange={handleXpChange}
            placeholder={xp !== null ? xp.toString() : ""}
            className="p-2 rounded bg-secondary text-text"
          />
          <button
            onClick={handleSubmitLevelAndXp}
            className="ml-4 bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 transition duration-300"
          >
            Update XP & Level
          </button>
        </div>

        {/* Display Current XP */}
        <div className="text-center mb-4 text-xl font-bold">
          Available XP: {xp !== null ? xp : 'Loading...'}
        </div>

        {/* Tree Dropdown */}
        <div className="mb-8 text-center">
          <label className="text-xl mr-4">Select Force Tree:</label>
          <select onChange={handleTreeChange} className="p-2 rounded bg-secondary text-text" defaultValue="">
            <option value="" disabled>Choose ability tree</option>
            {availableTrees.map(tree => (
              <option key={tree.id} value={tree.id}>
                {tree.name} {!purchasedTrees[tree.id] && "🔒"}
              </option>
            ))}
          </select>

          {selectedTree && !purchasedTrees[selectedTree.id] && (
            <button
              onClick={() => handlePurchaseTree(selectedTree.id, selectedTree.purchaseCost)}
              className="bg-red-600 text-white py-2 px-4 ml-4 rounded hover:bg-text hover:text-background transition duration-300"
            >
              Purchase Tree ({selectedTree.purchaseCost} XP)
            </button>
          )}
        </div>

        {/* Tree Nodes Display */}
        {selectedTree ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {selectedTree.force_power_tree.upgrades.map((node, index) => (
              <TreeNode
                key={index}
                node={node}
                xp={xp}
                setXp={setXp}
                locked={!purchasedTrees[selectedTree.id]}
                isCore={node.isCore || false}
                purchasedNodes={purchasedTrees[selectedTree.id] || []}
              />
            ))}
          </div>
        ) : (
          <div className="text-center text-lg text-gray-500">Please select an ability tree to view its nodes.</div>
        )}
      </div>
    </div>
  );
};

export default TreeBasedSpellPage;
