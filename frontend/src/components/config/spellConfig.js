// src/spellConfig.js
const spellConfig = {
    1: {
      name: "Dungeons & Dragons 5e",
      type: "level",
      spellPage: "LevelBasedSpellPage", // Routes to LevelBasedSpellPage for level-based selection
    },
    2: {
      name: "Pathfinder",
      type: "level",
      spellPage: "LevelBasedSpellPage", // Uses same page as D&D due to similar spell system
    },
    3: {
      name: "Call of Cthulhu",
      type: "percentile",
      spellPage: "PercentileSpellPage",
    },
    4: {
      name: "Shadowrun",
      type: "special",
      spellPage: "ShadowrunSpellPage",
    },
    5: {
      name: "Star Wars: Edge of the Empire",
      type: "tree",
      spellPage: "TreeBasedSpellPage",
    },
    6: {
      name: "Mothership RPG",
      type: "percentile",
      spellPage: "PercentileSpellPage",
    }
  };
  
  export default spellConfig;
  