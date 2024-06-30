import React, { useState, useEffect } from 'react';
import './styles/QuestionsList.css';
import arrow from './assets/arrow.png';
//import {sessionToken} from './AuthenticationModal.jsx'


const QuestionsList = () => {
    const [questions, setQuestions] = useState([]);
    useEffect(() => {
      fetch('https://otvetoved.ru/api/v1/questions')
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          console.log(data);
          setQuestions(data);
        });
    }, []);
  
  return (
    <div>
      {questions && (
        <div className="questionsList">
          {questions.map(question => (
            <div key={question.id} className="question">
                <img src={arrow} className="arrow" alt='стрелка'/>
                <p className='briefText'>{question.brief}</p>
                <div className='questionInfo'>
                  <p>
                    {new Intl.DateTimeFormat("ru-RU", {
                          year: "numeric",
                          month: "2-digit",
                          day: "2-digit"
                      }).format(question.created_at*1000)} Автор вопроса</p>
                </div>   
            </div>
          ))}
        </div>
      )}
      </div>
  );
};

export default QuestionsList;
