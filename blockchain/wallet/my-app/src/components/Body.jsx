import React, { useState, useEffect } from "react";
import "../App.css";
import Details from "../screens/Details";
import { useNavigate } from "react-router";
import {Link } from "react-router-dom";
function Body() {
  const navigate = useNavigate();
  const [voterId, setVoterId] = useState("");
  const [password, setPassword] = useState("");
  const [items, setItems] = useState([]);
  const handleSubmit = (event) => {

    
    event.preventDefault();
    fetch("http://localhost:8000/api/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username: voterId, password }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message === "Success") {
          console.log("success");
          navigate('/details',{ state: { voterId,password } });
          
        } else {
          console.log("Wrong username password");
        }
      });
  };
  const fetchApiData = () => {
    fetch("http://localhost:8000/")
      .then((r) => {
        return r.json();
      })
      .then((data) => {
        setItems(data);
      });
  };
  useEffect(() => {
    fetchApiData();
  }, []);
  return (
    <div className="card position-absolute top-50 start-50 translate-middle p-5">
      <form onSubmit={handleSubmit} className="form_class">
        <div
          className="Title "
          style={{ fontFamily: "Brush Script MT", color: "blue" }}
        >
          <h2>Khwopa Wallet</h2>
        </div>
        <div className="inputs">
          <label htmlFor="">Enter Voter Id</label>
          <input
            type="text"
            value={voterId}
            onChange={(e) => setVoterId(e.target.value)}
            placeholder="Wallet Id"
            className="form-control"
          />
          <label htmlFor="">Enter Password</label>
          <input
            type="password"
            name=""
            className="form-control"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Login
        </button>
      </form>
    </div>
  );
}

export default Body;
