export const ShadowrunConfig = {
    systemName: "Shadowrun",
    physicalFeatures: {
      fields: ["hair", "skin", "eyes", "height", "weight", "age", "gender"], // Common fields
    },
    categories: [
      { label: "Traits", key: "traits" },
      { label: "Cyberware", key: "cyberware" }, // Unique to Shadowrun
      { label: "Bioware", key: "bioware" }, // Unique to Shadowrun
      { label: "Bonds", key: "bonds" },
      { label: "Flaws", key: "flaws" },
      { label: "Organizations", key: "organizations" },
      { label: "Allies", key: "allies" },
      { label: "Enemies", key: "enemies" },
      { label: "Other", key: "other" },
    ],
  };
  