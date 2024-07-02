import React, { useState } from 'react'; 
import './Header.css';
import userLogo from '../assets/user.png';
import AuthenticationModal from '../components/AuthenticationModal.jsx';
import RegistrationModal from '../components/RegistrationModal.jsx';
import {Link} from "react-router-dom";


export default function Header() {
  const [showLogin, setShowLogin] = useState(false);
  const [showRegister, setShowRegister] = useState(false);

  return (
    <div className='header'>
        <Link to="/" className="linkSiteName">
          <h1 className='siteName'>Ответовед</h1>
        </Link>
        <div className='user'>
            <h1 className='userText'>Account name</h1>
                <img onClick={() => setShowLogin(true)} src={userLogo} className="userLogo" alt="Profile" />
        {showLogin && <AuthenticationModal onClose={() => setShowLogin(false)} onRegisterClick={() => {
          setShowLogin(false);
          setShowRegister(true);
        }} />}
        {showRegister && <RegistrationModal onClose={() => setShowRegister(false)} onLoginClick={() => {
          setShowRegister(false);
          setShowLogin(true);
        }} />}
        </div>
    </div>
  )
}
