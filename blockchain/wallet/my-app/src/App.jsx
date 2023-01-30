import "./App.css";
import Body from "./components/Body";
import Details from "./screens/Details";
import { Route, Routes } from "react-router-dom";
import Send_UI from "./components/Send_UI";


function App() {
  return (
    <div className="App">
      
       <Routes>
        <Route path="/" element={<Body />} /> 
        <Route exact path="/details" element={<Details />}></Route>
        <Route exact path="/send_ui" element={<Send_UI />}></Route>
       </Routes> 
    </div>
  );
}

export default App;
