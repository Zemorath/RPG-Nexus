export const CallOfCthulhuConfig = {
    systemName: "Call of Cthulhu",
    physicalFeatures: {
      fields: ["hair", "skin", "eyes", "height", "weight", "age", "gender"], // Common fields
    },
    categories: [
      { label: "Traits", key: "traits" },
      { label: "Phobias", key: "phobias" }, // Unique to Call of Cthulhu
      { label: "Manias", key: "manias" }, // Unique to Call of Cthulhu
      { label: "Bonds", key: "bonds" },
      { label: "Flaws", key: "flaws" },
      { label: "Organizations", key: "organizations" },
      { label: "Allies", key: "allies" },
      { label: "Enemies", key: "enemies" },
      { label: "Other", key: "other" },
    ],
  };
  