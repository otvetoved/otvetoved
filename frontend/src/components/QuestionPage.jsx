import React, { useState, useEffect } from 'react';
import './QuestionPage.css';
import user from './../assets/default-user.png';
import questionData from './../../public/fakeApi/questionData.json';
import answersData from './../../public/fakeApi/answersData.json';


const QuestionPage = () => {
  const [question, setQuestion] = useState(null);
  const [answers, setAnswers] = useState([]);
  const [newAnswer, setNewAnswer] = useState('');

//   useEffect(() => {
//     const fetchData = async () => {
//       try {
//         const questionResponse = await fetch(`${import.meta.env.VITE_BACKEND_URL}/v1/questions/1`); // Нужно заменить {question_id} на конкретный ID, который мы будем откуда-то получать
//         const questionData = await questionResponse.json();
//         setQuestion(questionData);

//         const answersResponse = await fetch(`${import.meta.env.VITE_BACKEND_URL}/v1/questions/1/answers`); //  Нужно заменить {question_id} на конкретный ID, который мы будем откуда-то получать
//         const answersData = await answersResponse.json();
//         setAnswers(answersData);
//       } catch (error) {
//         console.error('Failed to fetch question and answers:', error);
//       }
//     };

//     fetchData();
//   }, []);

useEffect(() => {
    // Использование данных из JSON файлов вместо fetch запросов
    setQuestion(questionData);
    setAnswers(answersData);
  }, []);

  const handleAnswerSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/v1/questions/1/answers`, { //  Нужно заменить {question_id} на конкретный ID, который мы будем откуда-то получать
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: newAnswer,
          created_by_user_id: 1, //  Нужно заменить {created_by_user_id} на конкретный ID, который мы будем получать после входа пользователя
        }),
      });

      if (response.ok) {
        const newAnswerData = await response.json();
        setAnswers([...answers, newAnswerData]);
        setNewAnswer('');
      } else {
        console.error('Failed to submit answer:', response.statusText);
      }
    } catch (error) {
      console.error('Failed to submit answer:', error);
    }
  };

  const handleLike = async (id, type, action) => {
    try {
      const response = await fetch(`/v1/${type}/${id}/${action}`, {
        method: 'PUT',
      });

      if (response.ok) {
        const updatedData = await response.json();
        if (type === 'questions') {
          setQuestion({ ...question, likes: updatedData.likes, dislikes: updatedData.dislikes });
        } else {
          const updatedAnswers = answers.map(answer => {
            if (answer.id === id) {
              return { ...answer, likes: updatedData.likes, dislikes: updatedData.dislikes };
            }
            return answer;
          });
          setAnswers(updatedAnswers);
        }
      } else {
        console.error(`Failed to update ${type} ${id}: ${response.statusText}`);
      }
    } catch (error) {
      console.error(`Failed to update ${type} ${id}: ${error}`);
    }
  };

  return (
    <div className="question-page">
      {question && (
        <>
          <h2 className="h2-question">{question.brief}</h2>
          <div className="date-question">{question.create_time}</div>
          <div className="author-info">
            <div className="profile">
              <img className="user-question" src={user} alt="Аватарка" />
              <div className="author-name">{question.author}</div>
            </div>
            <div className="question-info">
              <div className="question-text">{question.text}</div>
            </div>
            <div className="question-actions">
            <button onClick={() => handleLike(question.id, 'questions', 'like')} className="like-btn">👍 Лайк {question.likes}</button>
            <button onClick={() => handleLike(question.id, 'questions', 'dislike')} className="dislike-btn">👎 Дизлайк {question.dislikes}</button>
          </div>
          </div>
        </>
      )}

      {answers.length > 0 && (
        <div className="answers">
          {answers.map(answer => (
            <div key={answer.id} className="answer">
              <div className="date-question">{answer.create_time}</div>
              <div className="author-info">
                <div className="profile">
                  <img className="user-question" src={user} alt="Аватарка" />
                  <div className="author-name">{answer.author}</div>
                </div>
                <div className="answer-info">
                  <div className="answer-text">{answer.text}</div>
                </div>
              </div>
              <div className="answer-actions">
              <button onClick={() => handleLike(answer.id, 'answers', 'like')} className="like-btn">👍 Лайк {answer.likes}</button>
                <button onClick={() => handleLike(answer.id, 'answers', 'dislike')} className="dislike-btn">👎 Дизлайк {answer.dislikes}</button>
              </div>
            </div>
          ))}
        </div>
      )}


      <form className="answer-form" onSubmit={handleAnswerSubmit}>
        <div className="author-info">
          <div className="profile">
            <img className="user-question" src={user} alt="Аватарка" />
            <div className="author-name">Вы</div>
          </div>
          <textarea
            placeholder="Введите ваш ответ"
            className="response-textarea"
            value={newAnswer}
            onChange={(e) => setNewAnswer(e.target.value)}
          ></textarea>
          <button className="submit-btn" type="submit">Отправить</button>
        </div>
      </form>
    </div>
  );
};

export default QuestionPage;
