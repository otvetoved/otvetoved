import React, { useState, useEffect } from 'react';
import './styles/App.css'
import QuestionsList from './QuestionsList'
import QuestionCreatingPage from './components/QuestionCreatingPage'
import {Helmet} from 'react-helmet'
import arrow from './assets/arrow.png'

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

    <Helmet>
      <title>Ответовед</title>
      <meta name="description" content="Ответовед место для вопросов"/>
      <meta property="og:title" content="Ответовед.ру"/>
      <meta property="og:description" content="Задайте вопрос и получите ответ от пользователей!"/>
      <meta property="og:image" content={arrow}/>
    </Helmet>

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