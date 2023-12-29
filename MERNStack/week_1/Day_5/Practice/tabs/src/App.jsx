import React from 'react';
import './App.css'; 
import Tabs from './components/Tabs'; 

function App() {
  const tabItems = [
    {
      label: 'Tab 1',
      content: <p>Content for Tab 1</p>,
      callback: () => console.log('Tab 1 clicked'), 
    },
    {
      label: 'Tab 2',
      content: <p>Content for Tab 2</p>,
      callback: () => console.log('Tab 2 clicked'), 
    },
  
  ];

  return (
    <div className="App">
      <h1>Tabs Component 📑</h1>
      <Tabs items={tabItems} />
    </div>
  );
}

export default App;
