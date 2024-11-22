export const MothershipConfig = {
    systemName: "Mothership RPG",
    physicalFeatures: {
      fields: ["hair", "skin", "eyes", "height", "weight", "age", "gender"], // Common fields
    },
    categories: [
      { label: "Traits", key: "traits" },
      { label: "Fears", key: "fears" }, // Unique to Mothership
      { label: "Skills", key: "skills" }, // Unique to Mothership
      { label: "Flaws", key: "flaws" },
      { label: "Organizations", key: "organizations" },
      { label: "Allies", key: "allies" },
      { label: "Enemies", key: "enemies" },
      { label: "Other", key: "other" },
    ],
  };
  