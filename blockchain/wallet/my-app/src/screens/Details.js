import "../App.css";
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router";
import { useLocation } from "react-router-dom";
function Details() {
  const [items, setItems] = useState([]);
  const [amounts, setAmounts] = useState([]);
  const navigate = useNavigate();
  const location = useLocation();
  const dataArray = [location.state];
  const { sender_wallet_id } = location.state;
  const { receiver_wallet_id } = location.state;
  const { amount } = location.state;

  const voteid = location.state.voterId;
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
          <h1 className="name">{voteid}</h1>
          <h1 className="name">{sender_wallet_id}</h1>
          <h1 className="text-xl font-bold text-white ">Transaction Details</h1>
          Your Balance:{" "}
          {items.map((data, index) => {
            if (voteid == data.username)
              return <p key={index}>{data.balance}</p>;
            if (sender_wallet_id == data.username)
              return <p key={index}>{data.balance}</p>;
          })}
        </div>
        <button
          type="submit"
          id="button1"
          className=" bg-blue-500 p-0.5"
          onClick={() => {
            navigate("/send_ui");
          }}
        >
          Send
        </button>
        <button
          type="submit"
          id="button2"
          className=" bg-blue-500 p-0.5"
          onClick={fetchApiData}
        >
          Receive
        </button>
      </div>

      {dataArray.map((item, index) => (
        <Cards
          key={index}
          sender={item.sender_wallet_id}
          receiver={item.receiver_wallet_id}
          amount={item.amount}
        />
      ))}
    </div>
  );
}
function Cards({ sender, receiver, amount }) {
  return (
    <div className="card main pl-5 pr-4 pb-3">
      <div className="card inside mb-3">
        <h2>{sender}</h2>
        <h2>{receiver}</h2>
        <p>{amount}</p>
        <p></p>
      </div>
    </div>
  );
}

export default Details;
