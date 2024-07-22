import React from "react";
import { Box, styled } from "@mui/system";

// https://css-tricks.com/hamburger-menu-with-a-side-of-react-hooks-and-styled-components/

const StyledBurger = styled("button")({
  position: "absolute",
  top: "5%",
  left: "2rem",
  display: "flex",
  flexDirection: "column",
  justifyContent: "space-around",
  width: "2rem",
  height: "2rem",
  background: "transparent",
  border: "none",
  cursor: "pointer",
  padding: "0",
  zIndex: "10",
  "& focus": {
    outline: "none",
  },
  "& div": {
    width: "2rem",
    height: "0.25rem",
    borderRadius: "10px",
    transition: "all 0.3s linear",
    position: "relative",
    trasformOrigin: "1px",
  },
});

const Burger = () => {
  return;
  <StyledBurger>
    <div />
    <div />
    <div />
  </StyledBurger>;
};

export default Burger;
