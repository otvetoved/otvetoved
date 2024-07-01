import React, { useState } from 'react';
import Header from './header/Header'
import Footer from './footer/Footer'
import './styles/App.css'
import QuestionCreatingPage from './components/QuestionCreatingPage'

import QuestionsList from './QuestionsList'


function App() {

  const [isModalOpen, setIsModalOpen] = useState(false);

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <>
      <Header/>
      <div className='body'>
      <button className='createQuestion' onClick={openModal}>Создать вопрос</button>
      {isModalOpen && <QuestionCreatingPage onClose={closeModal} />}
        <QuestionsList/>
      </div>
      <Footer/>
    </>
  )
}

export default App
