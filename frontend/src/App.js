
import Login from "./login/login";
import Profile from './Profile/Profile'
import { Routes, Route } from "react-router-dom";
import { RequireToken } from "./Auth";

function App(){
return  (
    <div className ="App">
        <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/profile" element={<RequireToken><Profile /></RequireToken>} />
        </Routes>
    </div>
)}

export default App;