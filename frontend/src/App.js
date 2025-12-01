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
        <div className="min-h-screen bg-white flex items-center justify-center">
          <div className="text-center">
            <h1 className="text-3xl font-bold mb-4">Ajax Konfigurator</h1>
            <p>Konfigurator wird geladen...</p>
            <button 
              onClick={() => setShowImpressum(true)}
              className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
            >
              Impressum
            </button>
          </div>
        </div>
      )}
    </>
  );
}

export default App;