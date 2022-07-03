import React, { useEffect, useState } from 'react';
import './App.css';
import Accomplishment from './components/Accomplishment';
import LoadingComponent from './components/DataLoading';

function App() {
  const DataLoading = LoadingComponent(Accomplishment);
  const [appState, setAppState] = useState({
    loading: false,
    accomplishments: null,
  });
  useEffect(() => {
    setAppState({ loading: true });
    const apiUrl = 'http://127.0.0.1:8000/acc/';
    fetch(apiUrl)
      .then((data) => data.json())
      .then((accomplishments) => {
        setAppState({ loading:false, accomplishments: accomplishments.data });
      });
  }, [setAppState]);
  return (
    <div className='App'>
      <h1>Expected Accomplishments</h1>
      <DataLoading isLoading={appState.loading} accomplishments={appState.accomplishments} />
    </div>
  )
}

export default App;
