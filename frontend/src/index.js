import React from 'react';
import ReactDOM from 'react-dom/client';
// import * as serviceWorker from './serviceWorker';
import { Route, BrowserRouter, Routes} from 'react-router-dom';
import './index.css';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';


const routing = ReactDOM.createRoot(document.getElementById('root'));
routing.render(
  <React.StrictMode>
    <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/acc" element={<App />} />
        </Routes>
        <Footer />
    </BrowserRouter>
  </React.StrictMode>
);
