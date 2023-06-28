import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from "./auth-context/auth.context";


const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

// let user = localStorage.getItem("user");
let userdata = JSON.parse(localStorage.getItem("user") || '{}');

root.render(
  // <React.StrictMode>
    <BrowserRouter>
    <AuthProvider userData={userdata}>
        <App />
      </AuthProvider>
    </BrowserRouter>
  // </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
