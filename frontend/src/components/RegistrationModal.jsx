import React, { useState } from 'react';
import AuthenticationModal from './AuthenticationModal.jsx'; 
import './Modal.css'

const RegistrationModal = ({ onClose, onLoginClick }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [showAuthentication, setShowAuthentication] = useState(false); 

  const handleRegister = () => {
    fetch('https://otvetoved.ru/api/v1/authentication/register', {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        email,
        password,
      }),
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        return response.json().then(error => Promise.reject(error));
      }
    })
    .then(data => {
      alert(`Вы успешно зарегистрировались: ${data.username}`);
    })
    .catch(error => {
      console.error('Error occurred while registering: ', error);
      if (error.detail) {
        alert('Ошибка регистрации: ' + error.detail);
      } else {
        alert('Произошла ошибка регистрации. Пожалуйста, попробуйте позже.');
      }
    });
  };
  

  return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={onClose}>&times;</span>
        <h2 className="modal-head">Регистрация</h2>
        <form>
          <input type="text" className="modal-input" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Имя пользователя" />
          <input type="email" className="modal-input"  value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Почта" />
          <input type="password" className="modal-input"  value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Пароль" />
          <button className="modal-button" type="button"  onClick={handleRegister}>Зарегистрироваться</button>
        </form>
        <p className="modal-p" >Уже есть аккаунт? <span className="modal-span" onClick={onLoginClick}>Войдите</span></p>
        {showAuthentication && <AuthenticationModal onClose={() => setShowAuthentication(false)} onRegisterClick={() => setShowAuthentication(false)} />}
      </div>
    </div>
  );
};

export default RegistrationModal;
