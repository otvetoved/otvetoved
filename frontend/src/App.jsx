import Header from './header/Header'
import Footer from './footer/Footer'
import Questions from './Questions'
import './styles/App.css'



function App() {

  return (
    <>
      <Header/>
      <div className='body'>
        <button className='createQuestion'>Создать вопрос</button>
         
        <Questions/>
        
      </div>
     
      <Footer/>
    </>
  )
}

export default App
