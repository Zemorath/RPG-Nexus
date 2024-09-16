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
import ViewCharactersPage from './pages/ViewCharacters'
import AbilityScoresPage from './pages/AbilityScoresPage'
import { AuthProvider, useAuth } from './components/auth/auth';
import { ProtectedRoute, PublicRoute } from './components/Routes';

function AppContent() {
  const { user, loading, logout } = useAuth();

  if (loading) {
    return <div>Loading...</div>; // You can customize this with a loader component
  }

  return (
    <Router>
      {user && <Navbar onLogout={logout} />} {/* Render the navbar only if authenticated */}
      <Routes>
        {/* Public Routes */}
        <Route element={<PublicRoute />}>
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/" element={<HomePage />} />
        </Route>

        {/* Protected Routes */}
        <Route element={<ProtectedRoute />}>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/rpgsystems" element={<RPGSystemsPage />} />
          <Route path="/character/create" element={<CharacterCreationLandingPage />} />
          <Route path="/character/create/race/:systemId/:characterId?" element={<SelectRacePage />} />
          <Route path="/character/create/class/:systemId/:characterId" element={<SelectClassPage />} />
          <Route path="/character/create/ability-scores/:systemId/:characterId" element={<AbilityScoresPage />} />
          <Route path="/character/view" element={<ViewCharactersPage />} />
          {/* Other protected routes can go here */}
        </Route>
      </Routes>
    </Router>
  );
}

function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
}

export default App;