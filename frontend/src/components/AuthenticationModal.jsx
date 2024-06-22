import React, { useState } from 'react';
import RegistrationModal from './RegistrationModal.jsx';
import './AuthenticationModal.css'

const AuthenticationModal = ({ onClose, onRegisterClick }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showRegistration, setShowRegistration] = useState(false); 

  const handleLogin = () => {
    fetch(`${import.meta.env.VITE_BACKEND_URL}/v1/authentication`, {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        password,
      }),
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Failed to log in');
      }
    })
    .then(data => {
      alert('Вы успешно вошли!');
      console.log(data.session_token);
    })
    .catch(error => {
      console.error('Error occurred while logging in: ', error);
      alert('Вы провалили вход');
    });
  };
  

  return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={onClose}>&times;</span>
        <h2>Вход</h2>
        <form>
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Имя пользователя" />
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Пароль" />
          <button onClick={handleLogin}>Войти</button>
        </form>
        <p>Нет аккаунта? <span onClick={onRegisterClick}>Регистрация</span></p>
        {showRegistration && <RegistrationModal onClose={() => setShowRegistration(false)} onLoginClick={() => setShowRegistration(false)} />}
      </div>
    </div>
  );
};

export default AuthenticationModal;
