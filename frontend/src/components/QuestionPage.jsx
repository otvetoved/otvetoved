import React from 'react';
import './QuestionPage.css'
import user from './../assets/default-user.png'

const QuestionPage = () => {
  return (
    <div className="question-page">
        <h2 className="h2-question">Название вопроса</h2>
        <div className="date-question">Дата</div>
        <div className="author-info">
            <div className="profile">
            <img className="user-question" src={user} alt="Аватарка" />
            <div className="author-name">Автор темы</div>
            </div>
            <div className="question-info">
            <div className="question-text">Текст вопроса</div>
            </div>
          <div className="answer-actions">
            <button className="like-btn">👍 Лайк</button>
            <button className="dislike-btn">👎 Дизлайк</button>
          </div>
      </div>
      <div className="answers">
      <div className="date-question">Дата</div>
        <div className="author-info">
            <div className="profile">
            <img className="user-question" src={user} alt="Аватарка" />
            <div className="author-name">Автор ответа</div>
            </div>
            <div className="question-info">
            <div className="question-text">Текст вопроса</div>
            </div>
          <div className="answer-actions">
            <button className="like-btn">👍 Лайк</button>
            <button className="dislike-btn">👎 Дизлайк</button>
          </div>
      </div>
      </div>
      <div className="answer-form">
      <div className="author-info">
            <div className="profile">
            <img className="user-question" src={user} alt="Аватарка" />
            <div className="author-name">Вы</div>
            </div>
          <textarea placeholder="Введите ваш ответ" className="response-textarea"></textarea>
        <button className="submit-btn">Отправить</button>
      </div>
    </div>
    </div>
  );
}

export default QuestionPage;