import "./App.css";
import Body from "./components/Body";
import Details from "./screens/Details";
import { Route, Routes } from "react-router-dom";
import Home from "./components/Home";

function App() {
  return (
    <div className="App">
      
       <Routes>
        <Route path="/" element={<Body />} /> 
        <Route exact path="/details" element={<Details />}></Route>
       </Routes> 
    </div>
  );
}

export default App;
