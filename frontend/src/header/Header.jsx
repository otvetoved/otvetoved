import React, { useState, useEffect } from 'react'; 
import './Header.css';
import userLogo from '../assets/user.png';
import AuthenticationModal from '../components/AuthenticationModal.jsx';
import RegistrationModal from '../components/RegistrationModal.jsx';
import {Link} from "react-router-dom";


export default function Header() {
  const [showLogin, setShowLogin] = useState(false);
  const [showRegister, setShowRegister] = useState(false);
  const [username, setUsername] = useState('');
  const sessionToken = localStorage.getItem('sessionToken');

  useEffect(() => {
    if (sessionToken) {
      fetch('https://otvetoved.ru/api/v1/authentication/me?session_token=' + sessionToken)
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error('Failed to fetch user information');
          }
        })
        .then(data => {
          setUsername(data.username);
          console.log('Имя пользователя:', data.username);
        })
        .catch(error => {
          console.error('Ошибка получения имени пользователя:', error);
        });
    }
  }, [sessionToken]);

  
  return (
    <div className='header'>
        <Link to="/" className="linkSiteName">
          <h1 className='siteName'>Ответовед</h1>
        </Link>
        <div className='user'>
        <h1 className='userText'>{username || 'Войдитe'}</h1>
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
