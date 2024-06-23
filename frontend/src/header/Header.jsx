import React from 'react'
import "./Header.css"
 


export default function Header() {
  return (
    <div className='header'>
        <h1 className='siteName'>Ответовед</h1>
        <div className='user'>
            <h1 className='userText'>Account name</h1>
            <img src=""
                 alt="Фото пользователя"
                 width="56"
                 height="56"/>
        </div>
    </div>
  )
}