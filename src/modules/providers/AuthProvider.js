import React, { createContext, useContext, useState } from "react";
import { authenticateUser } from "../services/auth/AuthService";
import PropTypes from "prop-types";
import { useAppContext } from "./AppProvider";
import { jwtDecode } from "jwt-decode";

const AuthContext = createContext();

/**
 * AuthProvider Component
 * */
export const AuthProvider = ({ children }) => {
  const [authData, setAuthData] = useState({});
  const { language, setNotification } = useAppContext();

  /**
   * Handle the Authentication
   * @param {string} credential - JWT credential
   * */
  const handleAuthentication = async (credential) => {
    const [data, status] = await authenticateUser(credential);
    console.log(data);
    if (status === 200) {
      setAuthData(data);
      setNotification({
        type: "success",
        info: language["loginMessages"]["success"],
      });
      window.location.href = "/dashboard";
    } else {
      setNotification({
        type: "error",
        info: data.message,
      });
    }
  };

  const value = {
    authData: authData,
    setAuthData: setAuthData,
    handleAuthentication: handleAuthentication,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

/**
 * AuthProvider propTypes
 * */
AuthProvider.propTypes = {
  children: PropTypes.node,
};

export const useAuthContext = () => useContext(AuthContext);
