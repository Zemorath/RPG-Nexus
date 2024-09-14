// import { useState, useEffect } from 'react';
// import authService from '../services/auth/authService';

// export const useAuth = () => {
//   const [isAuthenticated, setIsAuthenticated] = useState(false);
//   const [user, setUser] = useState(null);

//   useEffect(() => {
//     const storedUser = localStorage.getItem('user'); // Check local storage for user session
//     if (storedUser) {
//       setIsAuthenticated(true);
//       setUser(JSON.parse(storedUser));
//     }
//   }, []);

//   const login = async (email, password) => {
//     const response = await authService.login(email, password);
//     if (response.success) {
//       setIsAuthenticated(true);
//       setUser(response.user);
//       localStorage.setItem('user', JSON.stringify(response.user));  // Persist the user session
//     }
//     return response;
//   };

//   const logout = () => {
//     authService.logout();
//     setIsAuthenticated(false);
//     setUser(null);
//     localStorage.removeItem('user');
//   };

//   return { isAuthenticated, user, login, logout };
// };
