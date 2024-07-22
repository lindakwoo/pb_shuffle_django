import React from "react";
import { Box, styled } from "@mui/system";



const Home = () => {
  return (
    <main>
      <Box sx={{ height: "100vh" }}>
        <Box
          className='background_image'
          sx={{
            position: "absolute",
            top: "0",
            left: "0",
            width: "100%",
            height: "100%",
            backgroundImage: { xs: 'url("/mobile_back.jpg")', sm: 'url("/cropped_back.jpg")' },
            backgroundSize: "cover",
            backgroundPosition: "center",
            opacity: "0.3",
            zIndex: "-1",
          }}
        ></Box>
        <Box sx={{ display: "flex", justifyContent: "center", alignItems: "center", width: "100%" }}>
          <Box
            sx={{
              display: "flex",
              flexDirection: "column",
              mt: "100px",
              textAlign: { xs: "center", sm: "left" },
              alignItems: { xs: "center", sm: "start" },
              "& p": {
                fontSize: "24px",
                fontWeight: "400",
                color: "black",
              },
              "& h1": {
                fontFamily: '"Bebas Neue", sans-serif',
                fontWeight: "400",
                fontStyle: "normal",
                color: "#a9a4f4",
                fontSize: "96px",
              },
            }}
          >
            <h1>Pickleball Shuffle</h1>
            <p>Never play with the same player twice!</p>

            <a href='' className='create_button'>
              Get started
            </a>
          </Box>
        </Box>
      </Box>
    </main>
  );
};

export default Home;
