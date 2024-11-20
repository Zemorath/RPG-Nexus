export const EdgeOfTheEmpireConfig = {
    systemName: "Star Wars: Edge of the Empire",
    physicalFeatures: {
      fields: ["hair", "skin", "eyes", "height", "weight", "age", "gender"], // Common fields
    },
    categories: [
      { label: "Obligations", key: "obligations" }, // Unique to Edge of the Empire
      { label: "Motivations", key: "motivations" }, // Unique to Edge of the Empire
      { label: "Organizations", key: "organizations" },
      { label: "Allies", key: "allies" },
      { label: "Enemies", key: "enemies" },
      { label: "Other", key: "other" },
    ],
    defaultValues: {
      obligations: [
        { type: "Debt", value: 10, description: "" },
        { type: "Family", value: 10, description: "" },
      ],
      motivations: [
        { category: "Ambition", description: "" },
        { category: "Cause", description: "" },
      ],
    },
  };
  