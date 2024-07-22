import React, { useState } from "react";
import { Box, styled } from "@mui/system";
const HeaderTag = styled("header")({});

const Header = () => {
  const [isActive, setIsActive] = useState(false);
  return (
    <HeaderTag
      sx={{
        height: "84px",
        backgroundColor: "#a9a4f4",
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "space-between",
        "& p": {
          mr: "40px",
          color: "white",
        },
      }}
    >
      <Box
        sx={{
          display: "flex",
          flexDirection: { xs: "row-reverse", sm: "row" },
          justifyContent: "start",
          alignItems: "center",
          ml: "40px",
          "& img": { height: "75px" },
          "& h3": {
            fontFamily: `"Bebas Neue", sans-serif`,
            fontWeight: "400",
            fontStyle: "normal",
            color: "white",
            fontSize: "32px",
          },
        }}
      >
        <img class='icon' src='/white_pickle.png' />
        <h3 class='pickleball_icon_text'>Pickleball Shuffle</h3>
      </Box>
      <Box
        class='header_right'
        sx={{
          display: "flex",
          flexDirection: { xs: "row-reverse", sm: "row" },
          justifyContent: "start",
          alignItems: "center",
          ml: "40px",
        }}
      >
        <nav class='nav' id='nav'>
          <button onClick='hamburgerToggle()' class='hamburger' id='hamburger'>
            <span class='hamburger-line'></span>
            <span class='hamburger-line'></span>
            <span class='hamburger-line'></span>
          </button>
          <ul class='items' id='items'>
            <li class='item'>
              <a class='link-btn' href="{% url 'players_lists' %}">
                My Lists
              </a>
            </li>
            <li class='item'>
              <a class='link-btn' href="{% url 'players_list_create' %}">
                Create a List
              </a>
            </li>
            <li class='item'>
              <a class='link-btn' href="{% url 'logout' %}">
                Logout
              </a>
            </li>

            <li class='item'>
              <a class='link-btn' href="{% url 'login' %}">
                Login
              </a>
            </li>
            <li class='item'>
              <a class='link-btn' href="{% url 'signup' %}">
                Sign Up
              </a>
            </li>
          </ul>
        </nav>
      </Box>
    </HeaderTag>
  );
};

export default Header;
