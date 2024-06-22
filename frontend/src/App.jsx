import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [title, setTitle] = useState('');
  const [question, setQuestion] = useState('');

  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  };

  const handleQuestionChange = (e) => {
    setQuestion(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    //обработать данные формы
    console.log('Title:', title);
    console.log('Question:', question);
  };

  return (
    <div className='App'>
      <header className='App-header'>
        <div className='site-name'>Ответовед</div>
        <div className='user-info'>
          <span className='user-name'></span>
          <img className='user-avatar' alt='User Avatar'/>
        </div>
      </header>

      <div className="form-container">
        <div className='form-container-heading'>Создание вопроса</div>
          <form onSubmit={handleSubmit}>
            <div className='form-group'>
              <label htmlFor="title">Заголовок вопроса</label>
              <input type="text" id='title' value={title} onChange={handleTitleChange} required />
            </div>
            <div className='form-group'>
              <label htmlFor="question">Текст вопроса</label>
              <textarea id='question' value={question} onChange={handleQuestionChange} required></textarea>
            </div>
            <button type="submit">Опубликовать</button>
          </form>
      </div>

    </div>
    /*
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>*/
  )
}

export default App
