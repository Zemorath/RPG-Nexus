import React from 'react';

const TreeNode = ({ node, xp, setXp, locked, isCore, onInsufficientXp, unlockedTiers, onNodePurchase, isSelected }) => {
  const handleSelect = () => {
    if (isSelected) {
      setXp(xp + node.xp_cost);
      onNodePurchase(node.name, false); // false indicates deselection
    } else {
      const canUnlock = xp >= node.xp_cost && (!locked || unlockedTiers.includes(node.tier.toString()));
      
      if (canUnlock) {
        setXp(xp - node.xp_cost);
        onNodePurchase(node.name, true); // true indicates selection
      } else {
        onInsufficientXp(`You need to unlock previous tiers to access "${node.name}". Requires ${node.xp_cost} XP.`);
      }
    }
  };

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
