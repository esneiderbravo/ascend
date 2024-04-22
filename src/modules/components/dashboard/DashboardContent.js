import React, { useContext } from "react";
import { Button, Container } from "@mui/material";
import AppContext from "../../context/app";
import logoutManager from "../../utils/logoutManager";

/**
 * DashboardContent Component
 * @return {React.JSX.Element}
 */
const DashboardContent = () => {
  const [state, dispatch] = useContext(AppContext);
  const { language } = state;

  const handleLogout = () => {
    logoutManager.logout(state, dispatch, language);
  };

  return (
    <Container maxWidth="auto">
      <h1>Dashboard</h1>
      <Button onClick={handleLogout} variant="contained" color="error">
        {language["logoutTitleButton"]}
      </Button>
    </Container>
  );
};

export default DashboardContent;
