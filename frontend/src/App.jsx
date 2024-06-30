import Header from './header/Header'
import Footer from './footer/Footer'
import './styles/App.css'

import QuestionsList from './QuestionsList'


function App() {



  return (
    <>
      <Header/>
      <div className='body'>
        <button className='createQuestion'>Создать вопрос</button>
        <QuestionsList/>
      </div>
      <Footer/>
    </>
  )
}

export default App
