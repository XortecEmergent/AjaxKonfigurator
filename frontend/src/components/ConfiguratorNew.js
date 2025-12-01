import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { ArrowRight, ArrowLeft, Settings, FileSpreadsheet } from 'lucide-react';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const ConfiguratorNew = ({ onShowImpressum }) => {
  // State Management
  const [currentStep, setCurrentStep] = useState(1);
  const [productLines, setProductLines] = useState([]);
  const [selectedProductLine, setSelectedProductLine] = useState('');

  const steps = [
    { number: 1, title: 'Produktlinie auswählen' },
    { number: 2, title: 'Hub/NVR auswählen' },
    { number: 3, title: 'Komponenten' },
    { number: 4, title: 'Zusammenfassung' }
  ];

  // API Functions
  const fetchProductLines = async () => {
    try {
      const response = await axios.get(`${API}/product-lines`);
      setProductLines(response.data.product_lines || []);
    } catch (error) {
      console.error('Error fetching product lines:', error);
    }
  };

  // Step Navigation
  const nextStep = () => {
    if (currentStep < steps.length) {
      setCurrentStep(currentStep + 1);
    }
  };

  const prevStep = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1);
    }
  };

  // Product Line Selection
  const selectProductLine = (productLine) => {
    setSelectedProductLine(productLine.id);
    nextStep();
  };

  // Effects
  useEffect(() => {
    fetchProductLines();
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-white">
      {/* Header */}
      <div className="bg-white/95 backdrop-blur-sm border-b border-gray-100 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center space-x-8">
              <div className="h-8 px-4 py-2 bg-orange-500 text-white font-bold rounded">
                XORTEC
              </div>
              <div className="hidden md:flex items-center space-x-2">
                <span className="text-gray-400">×</span>
                <div className="h-6 px-3 py-1 bg-black text-white font-bold text-sm rounded">
                  AJAX
                </div>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Button 
                variant="ghost" 
                onClick={onShowImpressum}
                className="text-gray-600 hover:text-gray-900"
              >
                Impressum
              </Button>
            </div>
          </div>
        </div>
      </div>

      {/* Step Navigation */}
      <div className="bg-white border-b border-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-center space-x-4">
            {steps.map((step, index) => (
              <div key={step.number} className="flex items-center">
                <div 
                  className={`flex items-center justify-center w-8 h-8 rounded-full font-medium text-sm ${
                    currentStep >= step.number 
                      ? 'bg-black text-white' 
                      : 'bg-gray-200 text-gray-600'
                  }`}
                >
                  {step.number}
                </div>
                <div className="ml-2 hidden sm:block">
                  <span className={`text-sm font-medium ${
                    currentStep >= step.number ? 'text-gray-900' : 'text-gray-500'
                  }`}>
                    {step.title}
                  </span>
                </div>
                {index < steps.length - 1 && (
                  <ArrowRight className="w-4 h-4 mx-4 text-gray-400" />
                )}
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Step 1: Product Line Selection */}
        {currentStep === 1 && (
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-3xl font-bold text-gray-900 mb-4">Produktlinie wählen</h2>
              <p className="text-lg text-gray-600 max-w-3xl mx-auto">
                Ajax Systems bietet verschiedene Produktlinien für unterschiedliche Sicherheitsanforderungen
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {productLines.map((line) => (
                <Card 
                  key={line.id} 
                  className="group cursor-pointer hover:shadow-xl transition-all duration-300 border-gray-200 hover:border-black bg-white overflow-hidden"
                  onClick={() => selectProductLine(line)}
                >
                  <div className="aspect-video bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center">
                    <div className="text-2xl font-bold text-gray-600">{line.name}</div>
                  </div>
                  <CardHeader className="pb-2">
                    <CardTitle className="text-xl font-bold text-gray-900 group-hover:text-black">
                      {line.name}
                    </CardTitle>
                    <CardDescription className="text-sm text-gray-600">
                      {line.target_group}
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    <p className="text-gray-700 text-sm mb-4">{line.description}</p>
                    <div className="flex flex-wrap gap-1 mb-4">
                      {line.features && line.features.slice(0, 3).map((feature, idx) => (
                        <Badge key={idx} variant="secondary" className="text-xs px-2 py-1">
                          {feature}
                        </Badge>
                      ))}
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-gray-500">Auswählen</span>
                      <ArrowRight className="h-4 w-4 text-gray-400 group-hover:text-black transition-colors" />
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        )}

        {/* Step 2: Coming Soon */}
        {currentStep === 2 && (
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-3xl font-bold text-gray-900 mb-4">
                {selectedProductLine === 'video' ? 'NVR auswählen' : 'Hub auswählen'}
              </h2>
              <p className="text-lg text-gray-600">
                Auswahl wird geladen...
              </p>
            </div>

            <div className="flex justify-between">
              <Button onClick={prevStep} variant="outline">
                <ArrowLeft className="h-4 w-4 mr-2" />
                Zurück
              </Button>
              
              <Button onClick={nextStep}>
                Weiter (Demo)
                <ArrowRight className="h-4 w-4 ml-2" />
              </Button>
            </div>
          </div>
        )}

        {/* Step 3: Coming Soon */}
        {currentStep === 3 && (
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-3xl font-bold text-gray-900 mb-4">Komponenten auswählen</h2>
              <p className="text-lg text-gray-600">
                Komponenten werden geladen...
              </p>
            </div>

            <div className="flex justify-between">
              <Button onClick={prevStep} variant="outline">
                <ArrowLeft className="h-4 w-4 mr-2" />
                Zurück
              </Button>
              
              <Button onClick={nextStep} className="bg-black hover:bg-gray-800">
                Zur Zusammenfassung
                <ArrowRight className="h-4 w-4 ml-2" />
              </Button>
            </div>
          </div>
        )}

        {/* Step 4: Summary */}
        {currentStep === 4 && (
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-3xl font-bold text-gray-900 mb-4">System-Zusammenfassung</h2>
              <p className="text-lg text-gray-600">
                Übersicht Ihrer Ajax Security System-Konfiguration
              </p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
              {/* System Configuration */}
              <div className="lg:col-span-2 space-y-6">
                <Card>
                  <CardHeader>
                    <CardTitle className="text-lg font-semibold">Gewählte Produktlinie</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="flex items-center space-x-3">
                      <Badge variant="default" className="bg-black text-white">
                        {productLines.find(pl => pl.id === selectedProductLine)?.name || selectedProductLine}
                      </Badge>
                      <span className="text-sm text-gray-600">
                        Ajax Systems Produktlinie
                      </span>
                    </div>
                  </CardContent>
                </Card>

                <Card>
                  <CardHeader>
                    <CardTitle className="text-lg font-semibold">Konfiguration</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-gray-600">
                      Die Konfiguration ist in Entwicklung. Alle neuen 2025 Ajax-Produkte sind bereits im Backend verfügbar.
                    </p>
                  </CardContent>
                </Card>
              </div>

              {/* Actions */}
              <div className="space-y-6">
                <Card>
                  <CardHeader>
                    <CardTitle className="text-lg font-semibold">Aktionen</CardTitle>
                  </CardHeader>
                  <CardContent className="space-y-3">
                    <Button 
                      disabled
                      className="w-full bg-gray-300 cursor-not-allowed"
                    >
                      <FileSpreadsheet className="h-4 w-4 mr-2" />
                      Excel exportieren (Demo)
                    </Button>
                    
                    <Button 
                      onClick={() => setCurrentStep(1)} 
                      variant="outline"
                      className="w-full"
                    >
                      <Settings className="h-4 w-4 mr-2" />
                      Neue Konfiguration
                    </Button>
                  </CardContent>
                </Card>

                <Card className="bg-gray-50">
                  <CardHeader>
                    <CardTitle className="text-lg font-semibold">Nächste Schritte</CardTitle>
                  </CardHeader>
                  <CardContent className="text-sm text-gray-600 space-y-2">
                    <p>• Backend mit 2025 Ajax-Daten ist vollständig implementiert</p>
                    <p>• Frontend-Konfiguration in Entwicklung</p>
                    <p>• Kontaktieren Sie Xortec für ein Angebot</p>
                  </CardContent>
                </Card>
              </div>
            </div>

            <div className="flex justify-between">
              <Button onClick={prevStep} variant="outline">
                <ArrowLeft className="h-4 w-4 mr-2" />
                Zurück
              </Button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ConfiguratorNew;