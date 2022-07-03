import React from 'react';
import ReactDOM from 'react-dom';
// import * as serviceWorker from './serviceWorker';
import { Route, BrowserRouter as Router, Routes as Switch} from 'react-router-dom';
import './index.css';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';

const routing = (
  <Router>
    <React.StrictMode>
      <Header />
      <Switch>
        <Route exact path="/" component={App} />
      </Switch>
      <Footer />
    </React.StrictMode>
  </Router>
);

ReactDOM.render(routing, document.getElementById('root'));

import React from 'react';
import ReactDOM from 'react-dom';
// import * as serviceWorker from './serviceWorker';
// import { Route, BrowserRouter as Router, Switch} from 'react-router-dom';
import './index.css';
import App from './App';
// import Header from './components/Header';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

