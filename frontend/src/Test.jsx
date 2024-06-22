import React, { useState } from 'react';
import AuthenticationModal from './components/AuthenticationModal.jsx';
import RegistrationModal from './components/RegistrationModal.jsx';

//Test.jsx используется для теста всплывающих окон, которые должны всплывать при нажатии фото профиля

const Test = () => {
  const [showLogin, setShowLogin] = useState(false);
  const [showRegister, setShowRegister] = useState(false);

  return (
    <div>

      <button onClick={() => setShowLogin(true)}>Фото профиля</button>
      {showLogin && <AuthenticationModal onClose={() => setShowLogin(false)} onRegisterClick={() => {
        setShowLogin(false);
        setShowRegister(true);
      }} />}
      {showRegister && <RegistrationModal onClose={() => setShowRegister(false)} onLoginClick={() => {
        setShowRegister(false);
        setShowLogin(true);
      }} />}
    </div>
  );
};

export default Test;