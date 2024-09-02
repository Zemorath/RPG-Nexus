import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { useNavigate, Link } from 'react-router-dom';
import authService from '../../services/auth/authService';

const Login = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex items-center justify-center bg-background text-text">
      <div className="bg-primary p-8 rounded-lg shadow-lg max-w-md w-full">
        <h1 className="text-4xl font-bold text-accent mb-6 text-center">Login</h1>
        <Formik
          initialValues={{ email: '', password: '' }}
          validationSchema={Yup.object({
            email: Yup.string().email('Invalid email address').required('Required'),
            password: Yup.string().min(6, 'Password must be at least 6 characters').required('Required'),
          })}
          onSubmit={async (values, { setSubmitting }) => {
            try {
              const response = await authService.login(values.email, values.password);
              console.log(response);
          
              if (response.success) {
                navigate('/dashboard');
                window.location.reload(); // Force a reload to reset the state
              } else {
                alert(response.message || 'Login failed');
              }
            } catch (error) {
              console.error(error);
              alert('An error occurred during login.');
            }
            setSubmitting(false);
          }}
        >
          {({ isSubmitting }) => (
            <Form>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-1" htmlFor="email">Email</label>
                <Field
                  type="email"
                  name="email"
                  id="email"
                  className="bg-secondary text-text p-2 rounded w-full"
                />
                <ErrorMessage name="email" component="div" className="text-red-500 text-sm mt-1" />
              </div>
              <div className="mb-6">
                <label className="block text-sm font-medium mb-1" htmlFor="password">Password</label>
                <Field
                  type="password"
                  name="password"
                  id="password"
                  className="bg-secondary text-text p-2 rounded w-full"
                />
                <ErrorMessage name="password" component="div" className="text-red-500 text-sm mt-1" />
              </div>
              <button
                type="submit"
                className="bg-accent text-background font-bold py-2 px-4 rounded w-full hover:bg-text hover:text-background transition duration-300"
                disabled={isSubmitting}
              >
                {isSubmitting ? 'Logging in...' : 'Login'}
              </button>
            </Form>
          )}
        </Formik>
        <p className="mt-4 text-center">
          Don't have an account?{' '}
          <a href="/signup" className="text-accent hover:text-secondary">Sign up here</a>
        </p>
        <div className="mt-6 text-center">
          <Link
            to="/"
            className="bg-secondary text-text font-bold py-2 px-4 rounded hover:bg-accent hover:text-background transition duration-300"
          >
            Back to Home
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Login;