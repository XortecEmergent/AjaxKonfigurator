import React, { useState } from 'react';
import './App.css';
import LandingPageNew from './components/LandingPageNew';
import ConfiguratorComplete from './components/ConfiguratorComplete';
import Impressum from './components/Impressum';

function App() {
  const [showLandingPage, setShowLandingPage] = useState(true);
  const [showImpressum, setShowImpressum] = useState(false);

  return (
    <>
      {showImpressum ? (
        <Impressum onClose={() => setShowImpressum(false)} />
      ) : showLandingPage ? (
        <LandingPageNew onStart={() => setShowLandingPage(false)} />
      ) : (
        <ConfiguratorComplete onShowImpressum={() => setShowImpressum(true)} />
      )}
    </>
  );
}

export default App;