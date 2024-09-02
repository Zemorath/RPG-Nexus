import axios from 'axios';

// Base URL for the API
const API_URL = 'http://127.0.0.1:5000/auth/';

// Login user
const login = async (email, password) => {
  try {
    const response = await axios.post(`${API_URL}login`, { email, password });

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
    localStorage.removeItem('user');
    await axios.post(`${API_URL}logout`);
  } catch (error) {
    throw new Error('Logout failed. Please try again.');
  }
};

// Register new user
const register = async (data) => {
  try {
    const response = await axios.post(`${API_URL}register`, data);
    return response.data;
  } catch (error) {
    throw new Error('Registration failed. Please check your details and try again.');
  }
};


// Get current user profile
const getProfile = async (userId) => {
  try {
    const response = await axios.get(`${API_URL}profile/${userId}`);
    return response.data;
  } catch (error) {
    throw new Error('Failed to retrieve user profile.');
  }
};

const checkAuthStatus = async () => {
  try {
    const response = await axios.get(`${API_URL}status`);
    return response.data;
  } catch (error) {
    console.error('Auth status check failed', error);
    return { isAuthenticated: false };
  }
};

const authService = {
  login,
  logout,
  register,
  getProfile,
  checkAuthStatus
};

export default authService;
