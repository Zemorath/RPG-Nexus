// src/TreeBasedSpellPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TreeNode from '../components/TreeNode';
import { useNavigate } from 'react-router-dom';

const TreeBasedSpellPage = ({ systemId, characterId }) => {
  const [xp, setXp] = useState(0);
  const [availableTrees, setAvailableTrees] = useState([]);
  const [selectedTree, setSelectedTree] = useState(null);
  const [locked, setLocked] = useState({});
  const navigate = useNavigate();

  // Fetch character XP and available Force trees
  useEffect(() => {
    const fetchCharacterData = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        setXp(response.data.xp);
        
        // Fetch available Force trees from the database
        const treesResponse = await axios.get(`http://127.0.0.1:5555/force-trees`);
        setAvailableTrees(treesResponse.data);
        
        const lockedStatus = {};
        treesResponse.data.forEach(tree => {
          lockedStatus[tree.id] = !response.data.purchased_trees.includes(tree.id);
        });
        setLocked(lockedStatus);
      } catch (error) {
        console.error('Error fetching character data or trees:', error);
      }
    };

    fetchCharacterData();
  }, [characterId]);

  const handleTreeChange = (event) => {
    const treeId = parseInt(event.target.value);
    const tree = availableTrees.find(tree => tree.id === treeId);
    setSelectedTree(tree);
  };

  const handlePurchaseTree = (treeId, cost) => {
    if (xp >= cost) {
      setXp(xp - cost);
      setLocked(prev => ({ ...prev, [treeId]: false }));
      // Send a request to update the character’s purchased trees
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

        {/* XP Display */}
        <div className="text-center mb-4 text-xl font-bold">Available XP: {xp}</div>

        {/* Tree Dropdown */}
        <div className="mb-8 text-center">
          <label className="text-xl mr-4">Select Force Tree:</label>
          <select onChange={handleTreeChange} className="p-2 rounded bg-secondary text-text">
            {availableTrees.map(tree => (
              <option key={tree.id} value={tree.id}>
                {tree.name} {locked[tree.id] && "🔒"}
              </option>
            ))}
          </select>

          {selectedTree && locked[selectedTree.id] && (
            <button
              onClick={() => handlePurchaseTree(selectedTree.id, selectedTree.purchaseCost)}
              className="bg-red-600 text-white py-2 px-4 ml-4 rounded hover:bg-text hover:text-background transition duration-300"
            >
              Purchase ({selectedTree.purchaseCost} XP)
            </button>
          )}
        </div>

        {/* Tree Nodes Display */}
        {selectedTree && (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {selectedTree.force_power_tree.upgrades.map((node, index) => (
              <TreeNode
                key={index}
                node={node}
                xp={xp}
                setXp={setXp}
                locked={locked[selectedTree.id]}
                isCore={node.isCore || false} // For recommended or core nodes
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default TreeBasedSpellPage;
