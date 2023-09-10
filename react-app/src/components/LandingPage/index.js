import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, NavLink } from "react-router-dom/cjs/react-router-dom.min";
import "./LandingPage.css";

const LandingPage = () => {
  //Initialize things
  const dispatch = useDispatch();
  const history = useHistory();

  //useSelectors

  //State

  //Dispatch

  return (
    <div className="landing-page-parent-div">
      <div className="landing-page-h1-container">
        <h1>Welcome to Sensory Score</h1>
      </div>
    </div>
  );
};

export default LandingPage;
