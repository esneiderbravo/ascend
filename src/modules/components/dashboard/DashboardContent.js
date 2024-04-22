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

  const handleLogout = () => {
    logoutManager.logout(state, dispatch);
  };

  return (
    <Container maxWidth="auto">
      <h1>Dashboard</h1>
      <Button onClick={handleLogout} variant="contained" color="primary">
        Sign Out
      </Button>
    </Container>
  );
};

export default DashboardContent;
