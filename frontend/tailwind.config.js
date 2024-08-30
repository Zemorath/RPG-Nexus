module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  theme: {
    extend: {
      colors: {
        primary: '#1b1f38', // Dark Indigo
        secondary: '#4a4a6a', // Muted Purple
        accent: '#d4af37', // Gold
        text: '#ffffff', // White for text
        background: '#0f0f1a', // Almost black background
      },
    },
  },
  plugins: [],
};
