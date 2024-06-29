import React from 'react'
import "./Header.css"
import userLogo from '../assets/user.png';
 


export default function Header() {
  return (
    <div className='header'>
        <h1 className='siteName'>Ответовед</h1>
        <div className='user'>
            <h1 className='userText'>Account name</h1>
            <img src={userLogo}
                 alt="Фото пользователя"
                 className='userLogo'
                 />
        </div>
    </div>
  )
}