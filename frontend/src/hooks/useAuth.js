import { useState, useEffect } from 'react';
import authService from '../services/auth/authService';

export const useAuth = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuthStatus = async () => {
      try {
        const authStatus = await authService.checkAuthStatus();
        setIsAuthenticated(authStatus.success);
      } catch (error) {
        console.error('Error checking auth status:', error);
      } finally {
        setLoading(false);
      }
    };

    const storedAuth = localStorage.getItem('auth');
    if (storedAuth) {
      setIsAuthenticated(true);
      setLoading(false);
    } else {
      checkAuthStatus();
    }
  }, []);

  const logout = async () => {
    try {
      await authService.logout();
      localStorage.removeItem('auth'); // Clear local storage
      setIsAuthenticated(false);
    } catch (error) {
      console.error('Error logging out:', error);
    }
  };

  return { isAuthenticated, loading, logout };
};
