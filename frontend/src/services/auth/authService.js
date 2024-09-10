import axios from 'axios';

// Base URL for the API
const API_URL = 'http://127.0.0.1:5555/auth/';

// Login user
const login = async (email, password) => {
  try {
    const response = await axios.post(`${API_URL}login`, { email, password }, { withCredentials: true });
    
    if (response.data.success) {
      // Store some form of authentication token or flag in localStorage
      localStorage.setItem('auth', JSON.stringify(response.data)); 
    }

    return response.data;
  } catch (error) {
    throw new Error('Login failed');
  }
};

// Logout user
const logout = async () => {
  try {
    await axios.post(`${API_URL}logout`, {}, { withCredentials: true });
    localStorage.removeItem('auth');
  } catch (error) {
    throw new Error('Logout failed. Please try again.');
  }
};

// Register new user
const register = async (data) => {
  try {
    const response = await axios.post(`${API_URL}register`, data);
    console.log('Registration response:', response);  // Added log to see backend response
    return response.data;
  } catch (error) {
    console.error('Registration error:', error.response ? error.response.data : error.message); // Log detailed error
    throw new Error('Registration failed. Please check your details and try again.');
  }
};

const authService = {
  login,
  logout,
  register,
};

export default authService;
