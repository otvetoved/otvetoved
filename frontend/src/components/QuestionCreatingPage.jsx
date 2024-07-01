import React, { useState} from 'react';
import './Modal.css';
import { sessionToken } from './AuthenticationModal.jsx';

const QuestionCreatingPage = ({ onClose }) => {
  const [brief, setBrief] = useState('');
  const [text, setText] = useState('');
  const [modalOpen, setModalOpen] = useState(false);

  const handlePublication = () => {
    console.log('Form submitted!');
    // Add logic for form submission
    onClose(); // Close the modal after submission
  };

  return (
    <div className="question-modal">
      <div className="question-content">
        <span className="close" onClick={onClose}>&times;</span>
        <h2 className="question-head">Создание вопроса</h2>
        <form>
          <p className="question-p">Заголовок</p>
          <input type="text" className="question-input" value={brief} onChange={(e) => setBrief(e.target.value)} />
          <p className="question-p">Текст вопроса</p>
          <textarea
            className="question-textarea"
            value={text}
            onChange={(e) => setText(e.target.value)}
          ></textarea>
          <button className="question-button" onClick={handlePublication}>Опубликовать</button>
        </form>
      </div>
    </div>
  );
};

export default QuestionCreatingPage;
