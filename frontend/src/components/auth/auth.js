import React, { createContext, useState, useEffect, useContext } from 'react';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:5555/auth/';

// Configure axios
axios.defaults.withCredentials = true;

// Create AuthContext
const AuthContext = createContext(null);

// AuthProvider component
export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [loading, setLoading] = useState(true);
  
    useEffect(() => {
      checkAuthStatus();
    }, []);
  
    const checkAuthStatus = async () => {
      try {
        const response = await axios.get(`${API_URL}status`);
        if (response.data.success) {
          setUser(response.data.user);
          setIsAuthenticated(true);
        } else {
          setUser(null);
          setIsAuthenticated(false);
        }
      } catch (error) {
        console.error('Auth status check failed:', error);
        setUser(null);
        setIsAuthenticated(false);
      } finally {
        setLoading(false);
      }
    };
  
    const login = async (email, password) => {
      try {
        const response = await axios.post(`${API_URL}login`, { email, password });
        if (response.data.success) {
          setUser(response.data.user);
          setIsAuthenticated(true);
          return { success: true };
        }
      } catch (error) {
        console.error('Login failed:', error);
        return { success: false, message: error.response?.data?.message || 'Login failed' };
      }
    };
  
    const logout = async () => {
      try {
        await axios.post(`${API_URL}logout`);
        setUser(null);
        setIsAuthenticated(false);
      } catch (error) {
        console.error('Logout failed:', error);
      }
    };
  
    const register = async (userData) => {
      try {
        const response = await axios.post(`${API_URL}register`, userData);
        if (response.data.success) {
          setUser(response.data.user);
          setIsAuthenticated(true);
          return { success: true };
        }
      } catch (error) {
        console.error('Registration failed:', error);
        return { success: false, message: error.response?.data?.message || 'Registration failed' };
      }
    };
  
    const value = {
      user,
      isAuthenticated,
      loading,
      login,
      logout,
      register,
      checkAuthStatus
    };
  
    return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
  };

// Custom hook to use the auth context
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};


export const AuthService = {
  login: async (email, password) => {
    try {
      const response = await axios.post(`${API_URL}login`, { email, password });
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  logout: async () => {
    try {
      await axios.post(`${API_URL}logout`);
    } catch (error) {
      throw error;
    }
  },
  register: async (userData) => {
    try {
      const response = await axios.post(`${API_URL}register`, userData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  checkAuthStatus: async () => {
    try {
      const response = await axios.get(`${API_URL}status`);
      return response.data;
    } catch (error) {
      throw error;
    }
  }
};