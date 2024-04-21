import React from "react";
import { GoogleLogin } from "@react-oauth/google";

/**
 * GoogleSignIn Content Component
 * @return React.JSX.Element
 * */
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
 * */
GoogleSignInContent.propTypes = {};

export default GoogleSignInContent;
