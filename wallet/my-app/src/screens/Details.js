import "../App.css";
import React, { useState, useEffect } from "react";
function Details() {
  const [items, setItems] = useState([]);
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
    <div className="card position-absolute top-50 start-50 translate-middle shadow-lg">
      <div class="rounded-lg p-4">
        <div class="bg-blue-800 text-white p-8 z-40 td ">
          <h1 className="name">
            {items.map((data) => {
              return <>{data.username}</>;
            })}
          </h1>
          <h1 className="text-xl font-bold text-white ">Transaction Details</h1>
          <p>
            Your Balance:{" "}
            {items.map((data) => {
              return <>{data.balance}</>;
            })}
          </p>
        </div>
        <button type="submit" id="button1" className=" bg-blue-500 p-0.5">
          Send
        </button>
        <button type="submit" id="button2" className=" bg-blue-500 p-0.5">
          Receive
        </button>
      </div>
      <Cards Title={"Transaction one"} />
    </div>
  );
}
function Cards({ Title }) {
  return (
    <div className="card main pl-5 pr-4 pb-3">
      <div className="card inside mb-3">
        <h2>{Title}</h2>
        <p>200$</p>
      </div>
      <div className="card inside mb-3">
        <h2>Transaction Two</h2>
        <p>200$</p>
      </div>
      <div className="card inside mb-3">
        <h2>Transaction Three</h2>
        <p>200$</p>
      </div>
      <div className="card inside mb-3">
        <h2>Transaction one</h2>
        <p>200$</p>
      </div>
    </div>
  );
}

export default Details;
