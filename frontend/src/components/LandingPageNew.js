import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';

const LandingPageNew = ({ onStart }) => {
  const features = [
    {
      title: "Intrusion Protection",
      description: "Wired and wireless intrusion protection devices",
      image: "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 300'%3E%3Cdefs%3E%3ClinearGradient id='grad1' x1='0%25' y1='0%25' x2='100%25' y2='100%25'%3E%3Cstop offset='0%25' stop-color='%23374151'/%3E%3Cstop offset='100%25' stop-color='%236B7280'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='400' height='300' fill='url(%23grad1)'/%3E%3Cg transform='translate(200,150)'%3E%3Ccircle cx='0' cy='-30' r='40' fill='%23fff' opacity='0.9'/%3E%3Cpath d='M -15 -30 L 15 -30 L 15 -10 L -15 -10 Z' fill='%23000'/%3E%3Ccircle cx='0' cy='30' r='20' fill='%23fff' opacity='0.8'/%3E%3C/g%3E%3C/svg%3E"
    },
    {
      title: "Video Surveillance", 
      description: "Professional video surveillance solutions",
      image: "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 300'%3E%3Cdefs%3E%3ClinearGradient id='grad2' x1='0%25' y1='0%25' x2='100%25' y2='100%25'%3E%3Cstop offset='0%25' stop-color='%231F2937'/%3E%3Cstop offset='100%25' stop-color='%23374151'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='400' height='300' fill='url(%23grad2)'/%3E%3Cg transform='translate(200,150)'%3E%3Crect x='-50' y='-30' width='100' height='60' rx='5' fill='%23fff' opacity='0.9'/%3E%3Ccircle cx='20' cy='0' r='25' fill='%23000' opacity='0.8'/%3E%3Ccircle cx='20' cy='0' r='15' fill='%23fff'/%3E%3C/g%3E%3C/svg%3E"
    },
    {
      title: "Fire and Life Safety",
      description: "Complete fire detection and safety systems", 
      image: "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 300'%3E%3Cdefs%3E%3ClinearGradient id='grad3' x1='0%25' y1='0%25' x2='100%25' y2='100%25'%3E%3Cstop offset='0%25' stop-color='%23DC2626'/%3E%3Cstop offset='100%25' stop-color='%23EF4444'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='400' height='300' fill='url(%23grad3)'/%3E%3Cg transform='translate(200,150)'%3E%3Cpath d='M -20 20 Q -30 0 -20 -20 Q 0 -30 20 -20 Q 30 0 20 20 Q 0 30 -20 20' fill='%23fff' opacity='0.9'/%3E%3C/g%3E%3C/svg%3E"
    },
    {
      title: "Comfort and Automation",
      description: "Smart home automation solutions",
      image: "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 300'%3E%3Cdefs%3E%3ClinearGradient id='grad4' x1='0%25' y1='0%25' x2='100%25' y2='100%25'%3E%3Cstop offset='0%25' stop-color='%23059669'/%3E%3Cstop offset='100%25' stop-color='%2310B981'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='400' height='300' fill='url(%23grad4)'/%3E%3Cg transform='translate(200,150)'%3E%3Crect x='-40' y='-40' width='80' height='80' rx='10' fill='%23fff' opacity='0.9'/%3E%3Ccircle cx='-15' cy='-15' r='8' fill='%23000'/%3E%3Ccircle cx='15' cy='-15' r='8' fill='%23000'/%3E%3Ccircle cx='-15' cy='15' r='8' fill='%23000'/%3E%3Ccircle cx='15' cy='15' r='8' fill='%23000'/%3E%3C/g%3E%3C/svg%3E"
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