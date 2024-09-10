import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/Home';
import Login from './components/auth/Login';
import Signup from './components/auth/Signup';
import Dashboard from './pages/Dashboard';
import Navbar from './components/Navbar';
import SelectRacePage from './pages/SelectRacePage';
import RPGSystemsPage from './pages/RPGSystems'
import CharacterCreationLandingPage from './pages/CharacterCreationLandingPage';
import SelectClassPage from './pages/SelectClassPage';
import { AuthProvider } from './services/AuthContext';
import { useAuth } from './hooks/useAuth';
import { ProtectedRoute, PublicRoute } from './components/Routes';


function App() {
  const { isAuthenticated, loading, logout } = useAuth();

  if (loading) {
    return <div>Loading...</div>; // You can customize this with a loader component
  }

  return (
    <AuthProvider>
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
            <Route path="/rpgsystems" element={<RPGSystemsPage />} />
            <Route path="/character/create" element={<CharacterCreationLandingPage />} />
            <Route path="/character/create/race/:systemId" element={<SelectRacePage />} />
            <Route path="/character/create/class/:systemId/:characterId" element={<SelectClassPage />} />
            {/* Other protected routes can go here */}
          </Route>
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
