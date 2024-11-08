import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TreeNode from '../components/TreeNode';
import { useNavigate } from 'react-router-dom';

const TreeBasedSpellPage = ({ systemId, characterId }) => {
  const TREE_COST = 10; // Hardcoded cost to unlock the base tree
  const [xp, setXp] = useState(null);
  const [customXp, setCustomXp] = useState("");
  const [characterLevel, setCharacterLevel] = useState(1);
  const [availableTrees, setAvailableTrees] = useState([]);
  const [selectedTree, setSelectedTree] = useState(null);
  const [purchasedTrees, setPurchasedTrees] = useState({});
  const [purchasedNodes, setPurchasedNodes] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [modalMessage, setModalMessage] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCharacterData = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`);
        setXp(response.data.experience_points || 0);
        setCharacterLevel(response.data.level || 1);

        const treesResponse = await axios.get(`http://127.0.0.1:5555/force-trees`);
        setAvailableTrees(treesResponse.data);

        const systemData = response.data.system_data || {};
        setPurchasedTrees(systemData.purchased_trees || {});
      } catch (error) {
        console.error('Error fetching character data or trees:', error);
      }
    };

    fetchCharacterData();
  }, [characterId]);

  const assignTiersToNodes = (nodes) => {
    const sortedNodes = nodes.slice().sort((a, b) => a.xp_cost - b.xp_cost);
    let currentTier = 1;
    let tierThreshold = 10; // Adjust based on actual data
  
    sortedNodes.forEach((node, index) => {
      node.tier = currentTier;
      if (index > 0 && node.xp_cost > sortedNodes[index - 1].xp_cost + tierThreshold) {
        currentTier++;
      }
    });
  
    return sortedNodes;
  };
  

  const handleLevelChange = (event) => {
    const newLevel = parseInt(event.target.value);
    setCharacterLevel(newLevel);
  };

  const handleXpChange = (event) => {
    setCustomXp(event.target.value);
  };

  const handleSubmitLevelAndXp = async () => {
    try {
      const response = await axios.post(`http://127.0.0.1:5555/api/characters/update-level`, {
        character_id: characterId,
        level: characterLevel,
        experience_points: customXp ? parseInt(customXp) : xp
      });
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

  const handlePurchaseTree = (treeId) => {
    if (xp >= TREE_COST) {
      setXp(xp - TREE_COST);
      setPurchasedTrees(prev => ({ ...prev, [treeId]: [] }));
  
      axios.post(`http://127.0.0.1:5555/api/characters/${characterId}/purchase-tree`, {
        tree_id: treeId,
        xp_cost: TREE_COST,
      }).catch(error => console.error("Error purchasing tree:", error));
    } else {
      setModalMessage(`Not enough XP to unlock this tree. Requires ${TREE_COST} XP.`);
      setShowModal(true);
    }
  };

  const handleNodePurchase = (nodeId) => {
    setPurchasedNodes(prevNodes => [...prevNodes, nodeId]);
  };

  const submitPurchasedData = async () => {
    try {
      await axios.post(`http://127.0.0.1:5555/api/characters/update-trees-nodes`, {
        character_id: characterId,
        tree_id: selectedTree.id,
        node_ids: purchasedNodes,
      });
      console.log('Purchased trees and nodes saved successfully');
    } catch (error) {
      console.error('Error saving purchased trees and nodes:', error);
    }
  };

  const closeModal = () => setShowModal(false);

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
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

        <div className="mb-4 text-center">
          <label className="text-xl mr-4">Select Character Level:</label>
          <select onChange={handleLevelChange} value={characterLevel} className="p-2 rounded bg-secondary text-text">
            {[...Array(20).keys()].map(level => (
              <option key={level + 1} value={level + 1}>{level + 1}</option>
            ))}
          </select>
        </div>

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

        <div className="text-center mb-4 text-xl font-bold">
          Available XP: {xp !== null ? xp : 'Loading...'}
        </div>

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
              onClick={() => handlePurchaseTree(selectedTree.id)}
              className="bg-red-600 text-white py-2 px-4 ml-4 rounded hover:bg-text hover:text-background transition duration-300"
            >
              Purchase Tree ({TREE_COST} XP)
            </button>
          )}
        </div>

        {selectedTree ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {assignTiersToNodes(selectedTree.force_power_tree.upgrades).map((node, index) => (
              <TreeNode
                key={index}
                node={node}
                xp={xp}
                setXp={setXp}
                locked={!purchasedTrees[selectedTree.id]} // Unlock only if the tree is purchased
                unlockedTiers={Object.keys(purchasedTrees[selectedTree.id] || {})} // Correct unlockedTiers calculation
                onInsufficientXp={() => {
                  setModalMessage(`Not enough XP to unlock ${node.name}. Requires ${node.xp_cost} XP.`);
                  setShowModal(true);
                }}
                isCore={node.isCore || false}
                onNodePurchase={handleNodePurchase}
              />
            ))}
          </div>
        ) : (
          <div className="text-center text-lg text-gray-500">Please select an ability tree to view its nodes.</div>
        )}

        <button
          onClick={submitPurchasedData}
          className="bg-green-600 text-white py-2 px-4 rounded hover:bg-green-700 transition duration-300 mt-4"
        >
          Save Purchased Trees and Nodes
        </button>
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-secondary p-6 rounded-lg max-w-md w-full relative">
            <button className="absolute top-2 right-4 text-background text-2xl" onClick={closeModal}>X</button>
            <h2 className="text-2xl font-bold text-center mb-4">Insufficient XP</h2>
            <p className="text-center text-lg mb-4">{modalMessage}</p>
            <button
              className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300 mx-auto block"
              onClick={closeModal}
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default TreeBasedSpellPage;
