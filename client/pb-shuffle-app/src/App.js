import React, { useState, useEffect } from "react";
import { ThemeProvider } from "@mui/system";
import { theme } from "./theme";
import logo from './logo.svg';
import Home from "./components/Home";
import Header from "./components/Header";
import './App.css';

function App() {

  const fetchData = async () => {
    const url = "http://localhost:8000/players_lists/";
    try {
      const fetchOptions = {
        method: "POST",
        body: JSON.stringify({ user: "lindawoo" }),
        headers: {
          "Content-Type": "application/json",
        },
      }
      const response = await fetch(url, fetchOptions);

      if (response.ok) {
        const data = await response.json();
        console.log(data)

      } else {
        console.log(`Failure to get player lists. Status code: ${response.status}`);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };
  useEffect(() => {
    fetchData();
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <Header />
      <Home />
    </ThemeProvider>
  );
}

export default App;
