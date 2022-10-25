import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowRightFromBracket } from '@fortawesome/free-solid-svg-icons';
import { Link, useNavigate } from 'react-router-dom'


export const Navbar = ({userId,setIsOpen}) => {

  const navigate = useNavigate();
  
  const handleClcik = () => {
    setIsOpen('open')
  }

  return (
      <nav id="navbar" className="global-nav w-full h-20">
              <ul className="global-nav-links w-1/2 h-full mx-auto flex items-center">
                  <li className="mr-auto cursor-pointer" href="">ICON</li>
                  <li className="nav-ele ml-10 cursor-pointer" href=""><a onClick={() => navigate(`/${userId}admin`)}>Home</a></li>
                  <li className="nav-ele dropdown ml-10 relative cursor-pointer" href="">Menu<i className="dropdown-toggle top-0.5 absolute ml-1.5 text-slate-400"></i>
                    <ul className="py-2.5 px-4 absolute rounded-md left-0">
                          <li className="nav-link"><a onClick={() => navigate(`/${userId}admin/table`)}>Table</a></li>
                          <li className="nav-link"><a href="#projects">Cart</a></li>
                    </ul>
                  </li>
                  <li className="nav-ele ml-10 cursor-pointer"><a onClick={() => handleClcik()}>ICON</a></li>
              </ul>

          {/* <i className="top-nav">ICON</i>
          <span className="top-nav">Name</span>
          <span className="top-nav">Number</span>
          <i className="top-nav"><FontAwesomeIcon icon={faArrowRightFromBracket}/></i> */}

        
      </nav>
  )
}
