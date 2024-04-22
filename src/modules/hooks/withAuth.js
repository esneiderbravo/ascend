import React, { useContext } from "react";
import { Navigate } from "react-router-dom";
import PropTypes from "prop-types";
import AppContext from "../context/app";

/**
 * WithAuth - Validate if has token
 * @param {children} React Router Object
 */
const WithAuth = ({ children }) => {
  const [state] = useContext(AppContext);
  const { authData } = state;

  if (authData?.token) {
    return children;
  }

  return <Navigate to="/" replace />;
};

WithAuth.propTypes = {
  children: PropTypes.any,
};

export default WithAuth;
