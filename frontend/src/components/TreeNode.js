// src/TreeNode.js
import React, { useState } from 'react';

const TreeNode = ({ node, xp, setXp, locked, isCore }) => {
  const [isSelected, setIsSelected] = useState(false);

  const handleSelect = () => {
    if (xp >= node.xp_cost) {
      setXp(xp - node.xp_cost);
      setIsSelected(!isSelected);
    }
  };

  return (
    <div
      className={`p-4 rounded-lg shadow-lg transition duration-300 ${
        isCore ? 'border-2 border-dashed border-blue-500' : 'border'
      } ${isSelected ? 'bg-accent text-background' : 'bg-secondary'}`}
    >
      <div className="flex justify-between items-center mb-2">
        <span className="font-bold text-lg">{node.name}</span>
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
