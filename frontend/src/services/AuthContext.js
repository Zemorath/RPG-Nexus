import React, { createContext, useState, useEffect } from 'react';
import authService from './auth/authService';

// Create the AuthContext
const AuthContext = createContext();

// AuthProvider component to wrap the entire app
const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);

  // This function will run on mount and check if the user is already authenticated
  useEffect(() => {
    const checkAuthStatus = async () => {
      const storedUser = localStorage.getItem('user');  // Check local storage for user session
      if (storedUser) {
        setIsAuthenticated(true);
        setUser(JSON.parse(storedUser));
      } else {
        const response = await authService.checkAuthStatus();
        if (response.success) {
          setIsAuthenticated(true);
          setUser(response.user);
          localStorage.setItem('user', JSON.stringify(response.user));  // Persist the user session
        }
      }
    };
    checkAuthStatus();
  }, []);

  const login = async (email, password) => {
    const response = await authService.login(email, password);
    if (response.success) {
      setIsAuthenticated(true);
      setUser(response.user);
      localStorage.setItem('user', JSON.stringify(response.user));  // Persist the user session
    }
    return response;
  };

  const logout = () => {
    authService.logout();
    setIsAuthenticated(false);
    setUser(null);
    localStorage.removeItem('user');
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
