import React from "react";
import GoogleSignInContent from "../../components/auth/GoogleSignInContent";
import { useAuthContext } from "../../providers/AuthProvider";

/**
 * Google Sign In Container Component
 * @return React.JSX.Element
 * */
const GoogleSignInContainer = () => {
  const { handleAuthentication } = useAuthContext();

  /**
   * Handle the Google response
   * */
  const handleGoogleResponse = (response) => {
    const { credential } = response;
    if (credential) {
      handleAuthentication(credential);
    }
  };

  return <GoogleSignInContent handleGoogleResponse={handleGoogleResponse} />;
};

/**
 * Google Sign In Container propTypes
 * */
GoogleSignInContainer.propTypes = {};

export default GoogleSignInContainer;
