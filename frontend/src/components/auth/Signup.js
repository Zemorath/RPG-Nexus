import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { useNavigate, Link } from 'react-router-dom';
import authService from '../../services/auth/authService';

const Signup = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex items-center justify-center bg-background text-text">
      <div className="bg-primary p-8 rounded-lg shadow-lg max-w-md w-full">
        <h1 className="text-4xl font-bold text-accent mb-6 text-center">Sign Up</h1>
        <Formik
          initialValues={{
            username: '',
            first_name: '',
            last_name: '',
            age: '',
            email: '',
            password: '',
            confirmPassword: '',
          }}
          validationSchema={Yup.object({
            username: Yup.string().required('Username is required'),
            first_name: Yup.string().required('First name is required'),
            last_name: Yup.string().required('Last name is required'),
            age: Yup.number().required('Age is required').min(13, 'You must be at least 13 years old'),
            email: Yup.string().email('Invalid email address').required('Email is required'),
            password: Yup.string().min(6, 'Password must be at least 6 characters').required('Password is required'),
            confirmPassword: Yup.string()
              .oneOf([Yup.ref('password'), null], 'Passwords must match')
              .required('Confirm Password is required'),
          })}
          onSubmit={async (values, { setSubmitting }) => {
            const { confirmPassword, ...data } = values;
            console.log(data);
            const response = await authService.register(data);
            if (response.success) {
              navigate('/dashboard');
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
                <label className="block text-sm font-medium mb-1" htmlFor="first_name">First Name</label>
                <Field
                  type="text"
                  name="first_name"
                  id="first_name"
                  className="bg-secondary text-text p-2 rounded w-full"
                />
                <ErrorMessage name="first_name" component="div" className="text-red-500 text-sm mt-1" />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-1" htmlFor="last_name">Last Name</label>
                <Field
                  type="text"
                  name="last_name"
                  id="last_name"
                  className="bg-secondary text-text p-2 rounded w-full"
                />
                <ErrorMessage name="last_name" component="div" className="text-red-500 text-sm mt-1" />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium mb-1" htmlFor="age">Age</label>
                <Field
                  type="number"
                  name="age"
                  id="age"
                  className="bg-secondary text-text p-2 rounded w-full"
                />
                <ErrorMessage name="age" component="div" className="text-red-500 text-sm mt-1" />
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
              <div className="mb-4">
                <label className="block text-sm font-medium mb-1" htmlFor="password">Password</label>
                <Field
                  type="password"
                  name="password"
                  id="password"
                  className="bg-secondary text-text p-2 rounded w-full"
                />
                <ErrorMessage name="password" component="div" className="text-red-500 text-sm mt-1" />
              </div>
              <div className="mb-6">
                <label className="block text-sm font-medium mb-1" htmlFor="confirmPassword">Confirm Password</label>
                <Field
                  type="password"
                  name="confirmPassword"
                  id="confirmPassword"
                  className="bg-secondary text-text p-2 rounded w-full"
                />
                <ErrorMessage name="confirmPassword" component="div" className="text-red-500 text-sm mt-1" />
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

export default Signup;
