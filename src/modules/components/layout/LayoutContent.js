import React from "react";
import { Container, Grid, Typography } from "@mui/material";
import GoogleSignInContainer from "../../containers/auth/GoogleSignInContainer";
import { useAppContext } from "../../providers/AppProvider";

/**
 * Layout Content Component
 * @return React.JSX.Element
 * */
const LayoutContent = () => {
  const { language } = useAppContext();
  return (
    <Container
      maxWidth="auto"
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        minHeight: "80vh",
      }}
    >
      <Grid item xs={12} md={12}>
        <Typography variant="h1">{language["title"]}</Typography>
      </Grid>
      <Grid item xs={12} md={12} mt="50px">
        <GoogleSignInContainer />
      </Grid>
    </Container>
  );
};

/**
 * Layout Content propTypes
 * */
LayoutContent.propTypes = {};

export default LayoutContent;
