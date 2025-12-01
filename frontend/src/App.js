import React, { useState } from 'react';
import './App.css';
import LandingPageNew from './components/LandingPageNew';
import ConfiguratorNew from './components/ConfiguratorNew';
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
        <ConfiguratorNew onShowImpressum={() => setShowImpressum(true)} />
      )}
    </>
  );
}

export default App;