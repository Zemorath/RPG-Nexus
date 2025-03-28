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
// import SelectSkillsFeatsPage from './pages/SelectSkillsFeatsPage'
import SelectSpellsPage from './pages/SelectSpellsPage';
import CharacterBackgroundPage from './pages/CharacterBackgroundPage'
import EquipmentSelectionPage from './pages/EquipmentSelectionPage';
import CharacterSummaryPage from './pages/CharacterSummaryPage';
import { AuthProvider, useAuth } from './components/auth/auth';
import { ProtectedRoute, PublicRoute } from './components/Routes';
import CharacterCreationLayout from './components/CharacterCreationLayout'

function AppContent() {
  const { user, loading, logout } = useAuth();

  if (loading) {
    return (
      <div className="min-h-screen bg-background text-text flex items-center justify-center">
        <div>Loading...</div>
      </div>
    );
  }

  return (
    <Router>
      <Routes>
        {/* Public Routes */}
        <Route element={<PublicRoute />}>
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/" element={<HomePage />} />
        </Route>

        {/* Protected Routes */}
        <Route element={<ProtectedRoute />}>
        <Route path="/dashboard" element={<><Navbar onLogout={logout} /><Dashboard /></>} />
          <Route path="/rpgsystems" element={<><Navbar onLogout={logout} /><RPGSystemsPage /></>} />
          <Route path="/character/view" element={<><Navbar onLogout={logout} /><ViewCharactersPage /></>} />
          <Route path="/character/create" element={<><Navbar onLogout={logout} /><CharacterCreationLandingPage /></>} />

          {/* Character Creation Routes with Progress Tracker */}
          <Route element={<CharacterCreationLayout onLogout={logout} />}>
            <Route path="/character/create/race/:systemId/:characterId?" element={<SelectRacePage />} />
            <Route path="/character/create/class/:systemId/:characterId" element={<SelectClassPage />} />
            <Route path="/character/create/ability-scores/:systemId/:characterId" element={<AbilityScoresPage />} />
            <Route path="/character/create/spells/:systemId/:characterId" element={<SelectSpellsPage />} />
            {/* <Route path="/character/create/skills/:systemId/:characterId" element={<SelectSkillsFeatsPage />} /> */}
            <Route path="/character/create/background/:systemId/:characterId" element={<CharacterBackgroundPage />} />
            <Route path="/character/create/equipment/:systemId/:characterId" element={<EquipmentSelectionPage />} />
            <Route path="/character/summary/:systemId/:characterId" element={<CharacterSummaryPage />} />
          </Route>
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