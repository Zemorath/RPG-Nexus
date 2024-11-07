import React, { useState } from 'react';

const TreeNode = ({ node, xp, setXp, locked, isCore, onInsufficientXp, unlockedTiers, onNodePurchase }) => {
  const [isSelected, setIsSelected] = useState(false);

  const handleSelect = () => {
    if (isSelected) {
      setXp(xp + node.xp_cost);
      setIsSelected(false);
    } else {
      if (xp >= node.xp_cost && unlockedTiers.includes(node.tier - 1)) {
        setXp(xp - node.xp_cost);
        setIsSelected(true);
        onNodePurchase(node.id); // Track the purchased node by its ID
      } else {
        onInsufficientXp(`You need to unlock previous tiers to access "${node.name}". Requires ${node.xp_cost} XP.`);
      }
    }
  };

  // Tier-based border styling
  const tierClass = {
    1: 'border-green-500',
    2: 'border-blue-500',
    3: 'border-purple-500',
    4: 'border-red-500',
  }[node.tier] || 'border-gray-400';

  return (
    <div
      className={`p-4 rounded-lg shadow-lg border-2 transition duration-300 ${tierClass} ${
        isCore ? 'border-dashed' : 'border-solid'
      } ${isSelected ? 'bg-accent text-background' : 'bg-secondary'}`}
    >
      <div className="flex justify-between items-center mb-2">
        <span className="font-bold text-lg">{node.name} (Tier {node.tier})</span>
        {locked ? (
          <span className="text-red-600">🔒</span>
        ) : (
          <input
            type="checkbox"
            checked={isSelected}
            onChange={handleSelect}
            className="transform scale-125"
          />
        )}
      </div>
      <p className="mb-2">{node.effect}</p>
      <div className="text-sm text-right">XP Cost: {node.xp_cost}</div>
      <div className="mt-2 text-xs text-center italic text-gray-400">{node.stat_changes}</div>
    </div>
  );
};

export default TreeNode;
