import React from "react";
import { NavLink } from "react-router-dom";
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import logo from "../Navigation/SensoryScore.png";
import "./Navigation.css";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);

  return (
    <ul className="navigation-ul">
      <li>
        <NavLink exact to="/">
          <img
            className="navbar-logo"
            src={logo}
            alt="Sensory Score Logo and Link to Home Page"
          ></img>
        </NavLink>
      </li>
      <li>
        <NavLink exact to="/">
          Places
        </NavLink>
      </li>
      <li>
        <NavLink exact to="/">
          Preferences
        </NavLink>
      </li>
      {isLoaded && (
        <li>
          <ProfileButton user={sessionUser} />
        </li>
      )}
    </ul>
  );
}

export default Navigation;
