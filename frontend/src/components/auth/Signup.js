import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { useNavigate } from 'react-router-dom';
import authService from '../../services/auth/authService';

const Signup = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex items-center justify-center bg-background text-text">
      <div className="bg-primary p-8 rounded-lg shadow-lg max-w-md w-full">
        <h1 className="text-4xl font-bold text-accent mb-6 text-center">Sign Up</h1>
        <Formik
          initialValues={{ username: '', email: '', password: '' }}
          validationSchema={Yup.object({
            username: Yup.string().required('Required'),
            email: Yup.string().email('Invalid email address').required('Required'),
            password: Yup.string().min(6, 'Password must be at least 6 characters').required('Required'),
          })}
          onSubmit={async (values, { setSubmitting }) => {
            const response = await authService.signup(values);
            if (response.success) {
              navigate('/login');
            } else {
              alert(response.message);
            }
            setSubmitting(false);
          }}
        >
          {({ isSubmitting }) => (
            <Form>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-1" htmlFor="username">Username</label>
                <Field
                  type="text"
                  name="username"
                  id="username"
                  className="bg-secondary text-text p-2 rounded w-full"
                />
                <ErrorMessage name="username" component="div" className="text-red-500 text-sm mt-1" />
              </div>
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
                {isSubmitting ? 'Signing up...' : 'Sign Up'}
              </button>
            </Form>
          )}
        </Formik>
        <p className="mt-4 text-center">
          Already have an account?{' '}
          <a href="/login" className="text-accent hover:text-secondary">Login here</a>
        </p>
      </div>
    </div>
  );
};

export default Signup;
