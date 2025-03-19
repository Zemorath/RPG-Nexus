module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  theme: {
    extend: {
      colors: {
        primary: '#1b1f38',
        secondary: '#4a4a6a',
        accent: '#d4af37',
        text: '#e0e0e0',
        background: '#0f0f1a',
      },
      boxShadow: {
        'glow': '0 0 10px #d4af37',
      }
    },
  },
  plugins: [],
};
