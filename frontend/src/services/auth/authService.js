import axios from 'axios';

// Base URL for the API
const API_URL = '/api/auth/';

// Login user
const login = async (username, password) => {
  try {
    const response = await axios.post(`${API_URL}login`, {
      username,
      password,
    });

    if (response.data.token) {
      localStorage.setItem('user', JSON.stringify(response.data));
    }

    return response.data;
  } catch (error) {
    throw new Error('Login failed. Please check your credentials and try again.');
  }
};

// Logout user
const logout = () => {
  localStorage.removeItem('user');
  return axios.post(`${API_URL}logout`);
};

// Register new user
const register = async (username, email, password) => {
  try {
    const response = await axios.post(`${API_URL}signup`, {
      username,
      email,
      password,
    });

    return response.data;
  } catch (error) {
    throw new Error('Registration failed. Please check your details and try again.');
  }
};

// Get current user profile
const getProfile = async (userId) => {
  try {
    const response = await axios.get(`/profile/${userId}`);
    return response.data;
  } catch (error) {
    throw new Error('Failed to retrieve user profile.');
  }
};

 const authService = {
  login,
  logout,
  register,
  getProfile,
};

export default authService