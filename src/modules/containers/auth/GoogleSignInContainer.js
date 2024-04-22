import React, { useContext } from "react";
import GoogleSignInContent from "../../components/auth/GoogleSignInContent";
import { authenticateUser } from "../../services/auth/AuthService";
import { useNavigate } from "react-router-dom";
import AppContext from "../../context/app";
import { setAuthData, setNotification } from "../../actions/state";
import LocalStorage from "../../utils/localStorage";

const GoogleSignInContainer = () => {
  const [state, dispatch] = useContext(AppContext);
  const { language } = state;
  const navigate = useNavigate();

  const handleAuthentication = async (credential) => {
    try {
      const [data, status] = await authenticateUser(credential);
      if (status === 200) {
        const authData = { token: credential, ...data };
        LocalStorage.setItem("authData", JSON.stringify(authData));
        dispatch(setAuthData(authData));
        dispatch(
          setNotification({
            type: "success",
            info: language["loginMessages"]["success"],
          }),
        );
        navigate("/dashboard", { replace: true });
      } else {
        dispatch(
          setNotification({
            type: "error",
            info: data.message,
          }),
        );
      }
    } catch (error) {
      console.error("Error authenticating user:", error);
    }
  };

  const handleGoogleResponse = (response) => {
    const { credential } = response;
    if (credential) {
      handleAuthentication(credential);
    }
  };

  return <GoogleSignInContent handleGoogleResponse={handleGoogleResponse} />;
};

GoogleSignInContainer.propTypes = {};

export default GoogleSignInContainer;
