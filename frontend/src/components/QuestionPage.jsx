import React, { useState, useEffect } from 'react';
import './QuestionPage.css';
import user from './../assets/default-user.png';
import {useParams} from "react-router-dom";


const QuestionPage = () => {
  const { id } = useParams();
  const question_id = id;
  const [question, setQuestion] = useState(null);
  const [answers, setAnswers] = useState([]);
  const [newAnswer, setNewAnswer] = useState('');
  const sessionToken = localStorage.getItem('sessionToken');


  useEffect(() => {
    const fetchData = async () => {
      try {
       // Нужно заменить {question_id} на конкретный ID, который мы будем откуда-то получать
       const questionResponse = await fetch(
        `https://otvetoved.ru/api/v1/questions/${question_id}`,
        {
          headers: {
            Authorization: `Bearer ${sessionToken}`
          }
        }
      );
        const questionData = await questionResponse.json();
        setQuestion(questionData);

        //  Нужно заменить {question_id} на конкретный ID, который мы будем откуда-то получать
        const answersResponse = await fetch(
            `https://otvetoved.ru/api/v1/questions/${question_id}/answers`,
            {
              headers: {
                Authorization: `Bearer ${sessionToken}`
              }
            }
          );
        const answersData = await answersResponse.json();
        console.log(answersData);
        setAnswers(answersData);
      } catch (error) {
        console.error('Failed to fetch question and answers:', error);
      }
    };

    fetchData();
  },[sessionToken]);



  const handleAnswerSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch(`https://otvetoved.ru/api/v1/questions/${question_id}/answers`, { //  Нужно заменить {question_id} на конкретный ID, который мы будем откуда-то получать
        method: 'POST',
        headers: {
           Authorization: `Bearer ${sessionToken}`,            
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: newAnswer,
          session_token: sessionToken
          //created_by_user_id: 1, //  Нужно заменить {created_by_user_id} на конкретный ID, который мы будем получать после входа пользователя
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

//   const handleLike = async (id, type, action) => {
//     try {
//       let url;
  
//       if (type === 'questions') {
//         url = `/v1/questions/${id}/${action}`;
//       } else if (type === 'answers') {
//         const questionId = question.id;
//         url = `/v1/questions/${questionId}/answers/${id}/${action}`;
//       }
  
//       const response = await fetch(url, {
//         method: 'PUT',
//       });
  
//       if (response.ok) {
//         const updatedData = await response.json();
//         if (type === 'questions') {
//           setQuestion({ ...question, likes: updatedData.likes, dislikes: updatedData.dislikes });
//         } else {
//           const updatedAnswers = answers.map(answer => {
//             if (answer.id === id) {
//               return { ...answer, likes: updatedData.likes, dislikes: updatedData.dislikes };
//             }
//             return answer;
//           });
//           setAnswers(updatedAnswers);
//         }
//       } else {
//         console.error(`Failed to update ${type} ${id}: ${response.statusText}`);
//       }
//     } catch (error) {
//       console.error(`Failed to update ${type} ${id}: ${error}`);
//     }
//   };
  
  return (
    <div className="question-page">
      {question && (
        <>
          <h2 className="h2-question">Вопрос: {question.brief}</h2>
          <div className="date-question">{
                new Intl.DateTimeFormat("ru-RU", {
                  year: "numeric",
                  month: "2-digit",
                  day: "2-digit",
                  hour: "2-digit",
                  minute: "2-digit",
                  second: "2-digit",
                }).format(question.created_at*1000)
              }</div>
          <div className="author-info">
            <div className="profile">
              <img className="user-question" src={user} alt="Аватарка" />
              <div className="author-name">{question.created_by_user.username}</div>
            </div>
            <div className="question-info">
              <div className="question-text">{question.text}</div>
            </div>
            <div className="question-actions">
            {/* <button onClick={() => handleLike(question.id, 'questions', 'like')} className="like-btn">👍 Лайк {question.likes}</button>
            <button onClick={() => handleLike(question.id, 'questions', 'dislike')} className="dislike-btn">👎 Дизлайк {question.dislikes}</button> */}
             {/* <button className="like-btn">👍 Лайк</button>
             <button className="dislike-btn">👎 Дизлайк</button> */}
          </div>
          </div>
        </>
      )}
          <h2 className="h2-answers">Ответы</h2>
      {answers.length > 0 && (
        <div className="answers">
          {answers.map(answer => (
            <div key={answer.id} className="answer" style={{wordWrap:'break-word'}}>
              <div className="date-question">{
                new Intl.DateTimeFormat("ru-RU", {
                  year: "numeric",
                  month: "2-digit",
                  day: "2-digit",
                  hour: "2-digit",
                  minute: "2-digit",
                  second: "2-digit",
                }).format(question.created_at*1000)
              }</div>
              <div className="author-info">
                <div className="profile">
                  <img className="user-question" src={user} alt="Аватарка" />
                  <div className="author-name">{answer.created_by_user.username}</div>
                </div>
                <div className="answer-info">
                  <div className="answer-text">{answer.text}</div>
                </div>
              </div>
              <div className="answer-actions">
              {/* <button onClick={() => handleLike(answer.id, 'answers', 'like')} className="like-btn">👍 Лайк {answer.likes}</button>
                <button onClick={() => handleLike(answer.id, 'answers', 'dislike')} className="dislike-btn">👎 Дизлайк {answer.dislikes}</button> */}
               <button className="like-btn">👍 Лайк</button>
               <button className="dislike-btn">👎 Дизлайк</button>               
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
