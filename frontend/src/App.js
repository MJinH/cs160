import { Table } from "./pages/Table";
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import './App.css'
import { useState } from "react";
import { Register } from "./pages/Register";
import { Login } from "./pages/Login";
import { Admin } from "./pages/Admin";
function App() {

  const [userId,setUserId] = useState('')
  const [isOpen,setIsOpen] = useState('closed')
  console.log(isOpen)

  return (
    <div className="App w-screen h-screen">
      <BrowserRouter>
          <Routes>
              <Route exact path="/" element={<Register/>} ></Route>
              <Route path='/login' element={<Login setUserId={setUserId}/>}></Route>
              {userId && <Route path={`/${userId}admin/table`} element={<Table userId={userId} isOpen={isOpen} setIsOpen={setIsOpen} setUserId={setUserId}/>}></Route>}
              {userId && <Route path={`/${userId}admin`} element={<Admin userId={userId} isOpen={isOpen} setIsOpen={setIsOpen} setUserId={setUserId}/>}></Route>}
          </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
