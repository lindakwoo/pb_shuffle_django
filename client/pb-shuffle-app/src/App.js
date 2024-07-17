import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';

function App() {

  const fetchData = async () => {
    const url = "http://localhost:8000/players_lists/";
    try {
      const response = await fetch(url, { user: "lindakwoo" });
      console.log("hello", response)

      if (response.ok) {
        const data = await response.json();
        console.log(data)

      } else {
        console.log(`Failure to get locations. Status code: ${response.status}`);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };
  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
