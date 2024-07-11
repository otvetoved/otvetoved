import React, { useState, useEffect } from 'react'; 
import './Header.css';
import userLogo from '../assets/user.png';
import exit from '../assets/exit.png';
import AuthenticationModal from '../components/AuthenticationModal.jsx';
import RegistrationModal from '../components/RegistrationModal.jsx';
import {Link} from "react-router-dom";


export default function Header() {
  const [showLogin, setShowLogin] = useState(false);
  const [showRegister, setShowRegister] = useState(false);
  const [username, setUsername] = useState('');
  const sessionToken = localStorage.getItem('sessionToken');
  const isLoggedIn = sessionToken !== null;

  useEffect(() => {
    if (sessionToken) {
      fetch('https://otvetoved.ru/api/v1/authentication/me?session_token=' + sessionToken)
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            if (response.status === 419) {
              alert("Сессия истекла. Войдите заново")
              throw new Error('Authentication timeout');
            } else {
              throw new Error('Failed to fetch user information');
            }
          }
        })
        .then(data => {
          setUsername(data.username);
          console.log('User Name:', data.username);
        })
        .catch(error => {
          if (error.message === 'Authentication timeout') {
            console.error('Authentication timeout. Redirecting to login page...');
          } else {
            console.error('Failed to fetch user information:', error);
          }
        });
    }
  }, [sessionToken]);
  

  const handleExit = () => {
    fetch('https://otvetoved.ru/api/v1/authentication/close_session?session_token=' + sessionToken, {
      method: 'DELETE'
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Failed to fetch close session');
      }
    })
    .then(data => {
      localStorage.removeItem('sessionToken'); 
      setTimeout(() => {
        window.location.reload();
    }, 2000); 
    })
    .catch(error => {
      console.error('Ошибка при закрытии сессии:', error);
    });
  };
  


  return (
    <div className='header'>
        <Link to="/" className="linkSiteName">
          <h1 className='siteName'>Ответовед</h1>
        </Link>
        <div className='user'>
        <h1 className='userText'>{username || 'Войдитe'}</h1>
                <img onClick={() => setShowLogin(true)} src={userLogo} className="userLogo" alt="Profile" />
                {isLoggedIn && (
          <>
            <button type="button" onClick={handleExit} src={exit} className="exit" alt="Exit">Exit</button>
          </>
        )}
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
