import React from 'react';
import { Button } from './ui/button';
import { CheckCircle2, Circle } from 'lucide-react';

const StepNavigation = ({ currentStep, totalSteps, onStepClick, completedSteps = [] }) => {
  const steps = [
    { id: 1, name: 'Produktlinie', description: 'Ajax Produktlinie wählen' },
    { id: 2, name: 'Hub', description: 'Hub-Zentrale auswählen' },
    { id: 3, name: 'Produkte', description: 'Geräte konfigurieren' },
    { id: 4, name: 'Zusammenfassung', description: 'Konfiguration prüfen' },
    { id: 5, name: 'Abschluss', description: 'Export & Fertigstellung' }
  ];

  return (
    <div className="bg-gray-900/50 rounded-lg p-6 mb-8 border border-gray-700">
      <div className="flex items-center justify-between">
        {steps.map((step, index) => (
          <React.Fragment key={step.id}>
            <div 
              className={`flex flex-col items-center cursor-pointer transition-all ${
                step.id <= currentStep ? 'cursor-pointer' : 'cursor-not-allowed'
              }`}
              onClick={() => step.id <= currentStep && onStepClick(step.id)}
            >
              <div className={`flex items-center justify-center w-10 h-10 rounded-full mb-2 transition-all ${
                step.id === currentStep 
                  ? 'bg-orange-600 text-white ring-2 ring-orange-300' 
                  : step.id < currentStep || completedSteps.includes(step.id)
                    ? 'bg-green-600 text-white' 
                    : 'bg-gray-700 text-gray-400 border-2 border-gray-600'
              }`}>
                {step.id < currentStep || completedSteps.includes(step.id) ? (
                  <CheckCircle2 className="w-5 h-5" />
                ) : (
                  <span className="text-sm font-bold">{step.id}</span>
                )}
              </div>
              
              <div className="text-center">
                <div className={`text-sm font-medium ${
                  step.id === currentStep 
                    ? 'text-orange-400' 
                    : step.id < currentStep || completedSteps.includes(step.id)
                      ? 'text-green-400'
                      : 'text-gray-400'
                }`}>
                  {step.name}
                </div>
                <div className="text-xs text-gray-500 mt-1 hidden md:block">
                  {step.description}
                </div>
              </div>
            </div>
            
            {/* Connection Line */}
            {index < steps.length - 1 && (
              <div className={`flex-1 h-0.5 mx-4 transition-all ${
                step.id < currentStep || completedSteps.includes(step.id)
                  ? 'bg-green-600' 
                  : step.id === currentStep
                    ? 'bg-orange-600'
                    : 'bg-gray-700'
              }`} />
            )}
          </React.Fragment>
        ))}
      </div>
      
      {/* Mobile Step Indicator */}
      <div className="md:hidden mt-4 text-center">
        <div className="text-white text-sm">
          Schritt {currentStep} von {totalSteps}: {steps[currentStep - 1]?.name}
        </div>
        <div className="text-gray-400 text-xs mt-1">
          {steps[currentStep - 1]?.description}
        </div>
      </div>
    </div>
  );
};

export default StepNavigation;