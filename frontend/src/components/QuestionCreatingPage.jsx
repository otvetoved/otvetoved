import React, { useState} from 'react';
import './Modal.css';
import { sessionToken } from './AuthenticationModal.jsx';

const QuestionCreatingPage = ({ onClose }) => {
  const [brief, setBrief] = useState('');
  const [text, setText] = useState('');
  const [modalOpen, setModalOpen] = useState(false);

  const handlePublication = () => {
    const data = {
      brief,
      text,
      session_token: sessionToken, 
    };

    fetch('https://otvetoved.ru/api/v1/questions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then(response => {
        if (response.ok) {
          console.log('Question successfully submitted');
          alert("Вопрос успешно создан!");
          onClose();
        } else {
          console.error('Failed to submit the question');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };


  return (
    <div className="question-modal">
      <div className="question-content">
        <span className="close" onClick={onClose}>&times;</span>
        <h2 className="question-head">Создание вопроса</h2>
        <form onSubmit={e => {
          e.preventDefault();
          handlePublication(); 
        }}>
          <p className="question-p">Заголовок</p>
          <input type="text" className="question-input" value={brief} onChange={(e) => setBrief(e.target.value)} />
          <p className="question-p">Текст вопроса</p>
          <textarea
            className="question-textarea"
            value={text}
            onChange={(e) => setText(e.target.value)}
          ></textarea>
          <button type="submit" className="question-button">Опубликовать</button>
        </form>
      </div>
    </div>
  );
};

export default QuestionCreatingPage;
