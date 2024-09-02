import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/Home';
import Login from './components/auth/Login';
import Signup from './components/auth/Signup';
import Dashboard from './pages/Dashboard';
import Navbar from './components/Navbar';
import { useAuth } from './hooks/useAuth';
import { ProtectedRoute, PublicRoute } from './components/Routes';

function App() {
  const { isAuthenticated, loading, logout } = useAuth();

  if (loading) {
    return <div>Loading...</div>; // You can customize this with a loader component
  }

  return (
    <Router>
      {isAuthenticated && <Navbar onLogout={logout} />} {/* Render the navbar only if authenticated */}
      <Routes>
        {/* Public Routes */}
        <Route element={<PublicRoute isAuthenticated={isAuthenticated} />}>
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/" element={<HomePage />} />
        </Route>

        {/* Protected Routes */}
        <Route element={<ProtectedRoute isAuthenticated={isAuthenticated} />}>
          <Route path="/dashboard" element={<Dashboard />} />
          {/* Other protected routes can go here */}
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
