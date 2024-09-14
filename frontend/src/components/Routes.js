import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from './auth/auth';

const ProtectedRoute = () => {
  const { user } = useAuth();
  return user ? <Outlet /> : <Navigate to="/login" />;
};

const PublicRoute = () => {
  const { user } = useAuth();
  return !user ? <Outlet /> : <Navigate to="/dashboard" />;
};

export { ProtectedRoute, PublicRoute };