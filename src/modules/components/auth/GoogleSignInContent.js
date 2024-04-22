import React from "react";
import PropTypes from "prop-types";
import { GoogleLogin } from "@react-oauth/google";

/**
 * GoogleSignIn Content Component
 * @param {Function} handleGoogleResponse - Callback function for handling Google sign-in response
 * @return {React.JSX.Element}
 */
const GoogleSignInContent = ({ handleGoogleResponse }) => {
  return (
    <GoogleLogin
      onSuccess={handleGoogleResponse}
      onFailure={handleGoogleResponse}
      cookiePolicy={"single_host_origin"}
    />
  );
};

/**
 * GoogleSignIn Content propTypes
 */
GoogleSignInContent.propTypes = {
  handleGoogleResponse: PropTypes.func.isRequired,
};

export default GoogleSignInContent;
