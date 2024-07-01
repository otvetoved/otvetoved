import React, { useState } from 'react';
import './styles/App.css'
import QuestionsList from './QuestionsList'
import QuestionCreatingPage from './components/QuestionCreatingPage'



function Home() {

    const [isModalOpen, setIsModalOpen] = useState(false);

    const openModal = () => {
      setIsModalOpen(true);
    };
    
    const closeModal = () => {
      setIsModalOpen(false);
    };
    

  return (
    <>
      <div className='body'>
      <button className='createQuestion' onClick={openModal}>Создать вопрос</button>
      {isModalOpen && <QuestionCreatingPage onClose={closeModal} />}
        <QuestionsList/>
      </div>
    </>
  )
}

export default Home
