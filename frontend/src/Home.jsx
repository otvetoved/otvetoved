import React, { useState, useEffect } from 'react';
import './styles/App.css'
import QuestionsList from './QuestionsList'
import QuestionCreatingPage from './components/QuestionCreatingPage'

function Home() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isUserAuthenticated, setIsUserAuthenticated] = useState(false);

  useEffect(() => {
    const sessionToken = localStorage.getItem('sessionToken');
    setIsUserAuthenticated(!!sessionToken);
  }, []);

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <>
      <div className='body'>
        {isUserAuthenticated ? (
          <button className='createQuestion' onClick={openModal}>
            Создать вопрос
          </button>
        ) : (
          <button className='createQuestion' disabled>
            Вы должны быть авторизованы
          </button>
        )}
        {isModalOpen && <QuestionCreatingPage onClose={closeModal} />}
        <QuestionsList />
      </div>
    </>
  )
}

export default Home