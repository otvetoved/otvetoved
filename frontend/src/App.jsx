import React, { useState } from 'react';
import main from "./main"
import './styles/App.css'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import Header from './header/Header'
import Footer from './footer/Footer'
import QuestionPage from './components/QuestionPage';


function App() {

  return (
    <>
      <Header />
      <Router>
        <Switch>
          <Route path="/" element={<Home />} />
          <Route path="/questions/:id">
            <QuestionPage question_id={id}/>
          </Route>
        </Switch>
      </Router>
      <Footer />
    </>
  )
}

export default App
