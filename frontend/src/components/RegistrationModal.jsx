import React, { useState } from 'react';
import AuthenticationModal from './AuthenticationModal.jsx'; 
import './RegistrationModal.css'

const RegistrationModal = ({ onClose, onLoginClick }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [showAuthentication, setShowAuthentication] = useState(false); 

  const handleRegister = () => {
    fetch(`${process.env.VITE_BACKEND_URL}/v1/authentication/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        email,
        password
      }),
    })
    .then(response => {
        if (response.ok) {
          // Successful registration
          alert(`Вы успешно зарегистрировались, ${response.username}`);
        } else {
          // Server returned an error
          alert('Вы провалили регистрацию');
        }
      })
      .catch(error => {
        // Request error
        console.error('Error occurred while registration in: ', error);
        alert('Возникла ошибка!')
      });
  };
  

  return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={onClose}>&times;</span>
        <h2>Регистрация</h2>
        <form>
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Имя пользователя" />
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Почта" />
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Пароль" />
          <button onClick={handleRegister}>Зарегистрироваться</button>
        </form>
        <p>Уже есть аккаунт? <span onClick={onLoginClick}>Войдите</span></p>
        {showAuthentication && <AuthenticationModal onClose={() => setShowAuthentication(false)} onRegisterClick={() => setShowAuthentication(false)} />}
      </div>
    </div>
  );
};

export default RegistrationModal;
