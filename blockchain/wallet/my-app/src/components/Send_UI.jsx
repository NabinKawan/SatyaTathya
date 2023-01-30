import React from 'react'

function Send_UI() {
  return (
    <div className="card position-absolute top-50 start-50 translate-middle shadow-lg">
    <div class="rounded-lg p-4">
      <div class="bg-blue-800 text-white p-8 z-40 td ">

        <h1 className="text-xl font-bold text-white ">Send Balance</h1>
      
    <form action="" method="post" className="form_class">
    <div className="inputs">
          <label htmlFor="">Enter Receiver's Wallet Id </label>
          <input
            type="text"
            placeholder="Receiver's Wallet Id"
            className="form-control"
          />
          <label htmlFor="">Enter Balance</label>
          <input
            type="number"
            name=""
            className="form-control"
            placeholder="Balance"
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Send
        </button>
    </form>
  </div>
  </div>
  </div>
  )
}

export default Send_UI