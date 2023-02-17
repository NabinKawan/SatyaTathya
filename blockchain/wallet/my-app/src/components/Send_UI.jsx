import React from 'react'
import { useState } from 'react';
import { useNavigate } from "react-router";
import { useLocation } from "react-router-dom";

function Send_UI() {
  const location = useLocation();
  const voterid = location.state.sender_wallet_id;
  const id = location.state.voteid;
  
  const [sender_wallet_id, setsender_wallet_id] = useState(voterid || id);
  const [receiver_wallet_id, setreceiver_wallet_id] = useState("");
  const [amount, setamount] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    fetch("http://localhost:8000/api/transfer/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sender_wallet_id, receiver_wallet_id, amount }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message === "Transfer successful") {
          console.log("Transfer successful");
          navigate('/details', { state: { sender_wallet_id, receiver_wallet_id, amount } });
        } else {
          console.log(data.message);
        }
      });
      
    const response = await fetch("http://localhost:8000/api/cards", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        Senders_name: sender_wallet_id,
        Receivers_name: receiver_wallet_id,
        balance: amount,
      }),
    });
  };

  return (
    <div className="card position-absolute top-50 start-50 translate-middle shadow-lg">
      <div className="rounded-lg p-4">
        <div className="bg-blue-800 text-white p-8 z-40 td">
          <h1 className="text-xl font-bold text-white">Send Balance</h1>
          <form action="" onSubmit={handleSubmit} className="form_class">
            <div className="inputs">
              <label htmlFor="">Sender's wallet Id </label>
              <h1 style={{ fontWeight: "bold" }}>{sender_wallet_id}</h1>
              <label htmlFor="">Enter Receiver's Wallet Id </label>
              <input
                type="text"
                value={receiver_wallet_id}
                onChange={(e) => setreceiver_wallet_id(e.target.value)}
                placeholder="Receiver's Wallet Id"
                className="form-control"
              />
              <label htmlFor="">Enter Amount </label>
              <input
                type="text"
                value={amount}
                onChange={(e) => setamount(e.target.value)}
                placeholder="Balance"
                className="form-control"
              />
            </div>
            <button type="submit" className="btn btn-primary">
              Send
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Send_UI;
