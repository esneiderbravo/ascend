import { Avatar, Grid, MenuItem, Typography } from "@mui/material";
import {
  CustomSelect,
  GridCustom,
  GridSelect,
} from "../../styles/layout/Layout.styled";
import usaIcon from "../../../resources/layout/usa.png";
import spainIcon from "../../../resources/layout/spain.png";
import React, { useContext } from "react";
import { setLanguage } from "../../actions/state";
import english from "../../language/en_us.json";
import spanish from "../../language/es_es.json";
import AppContext from "../../context/app";

/**
 * Footer Content Component
 * @return React.JSX.Element
 * */
const FooterContent = () => {
  const [state, dispatch] = useContext(AppContext);
  const { language } = state;
  /**
   * Handle language change events
   * @param {EventTarget} event - event with language change target.
   * **/
  const handleChangeLanguage = (event) => {
    const languageSelected = event.target.value;
    switch (languageSelected) {
      case "en_us":
        dispatch(setLanguage(english));
        break;
      case "es_es":
        setLanguage(spanish);
        break;
      default:
        setLanguage(english);
        break;
    }
  };

  return (
    <Grid
      container
      spacing={2}
      sx={{ position: "fixed", bottom: "10px", right: "10px" }}
    >
      <Grid item xs={7} md={10.5} display="flex">
        <Typography
          variant="h6"
          display="flex"
          alignItems="center"
          sx={{ marginLeft: "auto" }}
        >
          {language["changeLangTitle"]}
        </Typography>
      </Grid>
      <GridSelect item xs={5} md={1.5}>
        <CustomSelect
          onChange={handleChangeLanguage}
          autoWidth
          defaultValue="en_us"
          inputProps={{
            MenuProps: {
              MenuListProps: {
                sx: {
                  backgroundColor: (theme) => theme.body.backgroundColor,
                },
              },
            },
          }}
        >
          <MenuItem value="en_us">
            <GridCustom>
              <Avatar src={usaIcon} alt="Usa Icon" />
              <Typography variant="h6" color="white.main">
                {language["langTitles"]["en"]}
              </Typography>
            </GridCustom>
          </MenuItem>
          <MenuItem value="es_es">
            <GridCustom>
              <Avatar src={spainIcon} alt="Spain Icon" />
              <Typography variant="h6" color="white.main">
                {language["langTitles"]["es"]}
              </Typography>
            </GridCustom>
          </MenuItem>
        </CustomSelect>
      </GridSelect>
    </Grid>
  );
};

/**
 * FooterContent propTypes
 * */
FooterContent.propTypes = {};

export default FooterContent;
