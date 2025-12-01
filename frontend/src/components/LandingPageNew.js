import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';

const LandingPageNew = ({ onStart }) => {
  const features = [
    {
      title: "Intrusion Protection",
      description: "Wired and wireless intrusion protection devices",
      image: "https://ajax.systems/api/cdn-img/?img=%2Findex%2Ffirst-block%2Fintrusion-protection%2Fintrusion-protection.xl.jpg&1764237252"
    },
    {
      title: "Video Surveillance", 
      description: "Professional video surveillance solutions",
      image: "https://ajax.systems/api/cdn-img/?img=%2Findex%2Ffirst-block%2Fvideo-surveillance%2Fvideo-surveillance.xl.jpg&1764152916"
    },
    {
      title: "Fire and Life Safety",
      description: "Complete fire detection and safety systems", 
      image: "https://ajax.systems/api/cdn-img/?img=%2Findex%2Ffirst-block%2Ffire-detection%2Ffire.xl.jpg&1764152890"
    },
    {
      title: "Comfort and Automation",
      description: "Smart home automation solutions",
      image: "https://ajax.systems/api/cdn-img/?img=%2Findex%2Ffirst-block%2Fcomfort-automation%2Fcomfort-automation.xl.jpg&1764152878"
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-white">
      {/* Header */}
      <div className="border-b border-gray-100 bg-white/80 backdrop-blur-sm">
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
            <div className="text-right text-sm text-gray-600">
              <div className="font-medium">Xortec GmbH</div>
              <div>18+ Jahre Erfahrung</div>
            </div>
          </div>
        </div>
      </div>

      {/* Hero Section */}
      <div className="relative overflow-hidden">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <div className="text-center">
            <div className="mb-6">
              <span className="inline-block px-4 py-2 rounded-full bg-black text-white text-sm font-medium">
                Ajax Systems Konfigurator
              </span>
            </div>
            <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6 leading-tight">
              Rule your space
            </h1>
            <p className="text-xl text-gray-600 mb-12 max-w-3xl mx-auto">
              Erstellen Sie Ihr maßgeschneidertes Ajax Security System. Integrierte Lösungen für 
              Einbruchschutz, Videoüberwachung, Brandschutz und Komfort-Automatisierung.
            </p>
            <Button 
              onClick={onStart}
              className="bg-black hover:bg-gray-800 text-white px-8 py-4 text-lg font-medium rounded-lg transition-all transform hover:scale-105"
            >
              Konfigurator starten
            </Button>
          </div>
        </div>
        
        {/* Background Pattern */}
        <div className="absolute inset-0 -z-10">
          <div className="absolute inset-y-0 right-0 w-1/2 bg-gradient-to-l from-gray-50 to-transparent"></div>
          <div className="absolute top-20 right-20 w-72 h-72 bg-black/5 rounded-full blur-3xl"></div>
          <div className="absolute bottom-20 left-20 w-96 h-96 bg-gray-900/5 rounded-full blur-3xl"></div>
        </div>
      </div>

      {/* Features Grid */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">
            Komplette Sicherheitslösungen
          </h2>
          <p className="text-lg text-gray-600">
            Ajax Systems deckt alle Bereiche der professionellen Sicherheitstechnik ab
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, index) => (
            <Card key={index} className="group hover:shadow-xl transition-all duration-300 border-gray-100 hover:border-gray-200 bg-white">
              <div className="aspect-video overflow-hidden rounded-t-lg">
                <img 
                  src={feature.image} 
                  alt={feature.title}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                  onError={(e) => {
                    e.target.style.display = 'none';
                  }}
                />
              </div>
              <CardHeader className="pb-2">
                <CardTitle className="text-lg font-semibold text-gray-900">
                  {feature.title}
                </CardTitle>
              </CardHeader>
              <CardContent>
                <CardDescription className="text-gray-600">
                  {feature.description}
                </CardDescription>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>

      {/* Benefits Section */}
      <div className="bg-gray-50 py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6">
                Warum Ajax Systems?
              </h2>
              <div className="space-y-6">
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-black rounded-full mt-3 flex-shrink-0"></div>
                  <div>
                    <h3 className="font-semibold text-gray-900 mb-1">Wireless Grade 3 Lösung</h3>
                    <p className="text-gray-600">Weltweit erste kabellose Einbruchschutzlösung für Hochsicherheitsbereiche</p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-black rounded-full mt-3 flex-shrink-0"></div>
                  <div>
                    <h3 className="font-semibold text-gray-900 mb-1">Professionelle Installation</h3>
                    <p className="text-gray-600">Zertifizierte Xortec-Techniker für optimale Systemkonfiguration</p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-black rounded-full mt-3 flex-shrink-0"></div>
                  <div>
                    <h3 className="font-semibold text-gray-900 mb-1">Integrierte Verwaltung</h3>
                    <p className="text-gray-600">Alle Sicherheitsbereiche in einer einzigen Benutzeroberfläche</p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-black rounded-full mt-3 flex-shrink-0"></div>
                  <div>
                    <h3 className="font-semibold text-gray-900 mb-1">Zukunftssicher</h3>
                    <p className="text-gray-600">Regelmäßige Updates und neue Funktionen über die gesamte Lebensdauer</p>
                  </div>
                </div>
              </div>
            </div>
            <div className="relative">
              <div className="aspect-square bg-gradient-to-br from-gray-900 to-black rounded-2xl p-8 text-white">
                <div className="h-full flex flex-col justify-center">
                  <div className="mb-8">
                    <div className="h-8 px-4 py-2 bg-white text-black font-bold text-lg rounded inline-block">
                      AJAX SYSTEMS
                    </div>
                  </div>
                  <h3 className="text-2xl font-bold mb-4">Vertrauenswürdig weltweit</h3>
                  <p className="text-gray-300 mb-6">
                    Ajax Systems wird von Millionen von Benutzern weltweit vertraut und bietet 
                    zuverlässige Sicherheitslösungen für Wohn- und Gewerbeobjekte.
                  </p>
                  <div className="flex items-center space-x-4 text-sm">
                    <div className="flex items-center space-x-2">
                      <div className="w-2 h-2 bg-green-400 rounded-full"></div>
                      <span>EN 50131 Grade 3</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <div className="w-2 h-2 bg-green-400 rounded-full"></div>
                      <span>NDAA Compliant</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="py-16">
        <div className="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">
            Starten Sie jetzt Ihr Ajax System
          </h2>
          <p className="text-lg text-gray-600 mb-8">
            Konfigurieren Sie in wenigen Minuten Ihr individuelles Ajax Security System 
            mit professioneller Beratung von Xortec.
          </p>
          <Button 
            onClick={onStart}
            size="lg"
            className="bg-black hover:bg-gray-800 text-white px-12 py-4 text-lg font-medium rounded-lg transition-all transform hover:scale-105"
          >
            Konfigurator starten
          </Button>
        </div>
      </div>

      {/* Footer */}
      <div className="border-t border-gray-100 py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center space-x-6 mb-4 md:mb-0">
              <div className="h-6 px-3 py-1 bg-orange-500 text-white font-bold text-sm rounded">
                XORTEC
              </div>
              <span className="text-gray-400">×</span>
              <div className="h-5 px-2 py-1 bg-black text-white font-bold text-xs rounded">
                AJAX
              </div>
            </div>
            <div className="text-sm text-gray-600">
              © 2024 Xortec GmbH · Ajax Systems Authorized Partner
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LandingPageNew;