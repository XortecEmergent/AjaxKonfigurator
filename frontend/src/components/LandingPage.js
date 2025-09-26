import React from 'react';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { 
  ArrowRight, 
  Shield, 
  Zap, 
  Wifi, 
  Camera, 
  Home, 
  Building2, 
  Smartphone, 
  Clock,
  CheckCircle2,
  Users,
  Globe,
  Phone,
  Mail,
  MapPin,
  Award
} from 'lucide-react';

const LandingPage = ({ onStartConfigurator }) => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-orange-900 to-gray-800">
      {/* Navigation Header */}
      <nav className="bg-black/20 backdrop-blur-sm border-b border-gray-700 sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-6">
              {/* Xortec Logo */}
              <div className="flex items-center gap-3">
                <img 
                  src="https://xortec.de/media/0e/72/fc/1691537632/03Logo_linksb%C3%BCndig.png" 
                  alt="Xortec GmbH Logo"
                  className="h-10 w-auto"
                />
              </div>

              {/* Ajax Logo */}
              <div className="flex items-center gap-2 border-l border-gray-600 pl-6">
                <div className="w-8 h-8 bg-white rounded flex items-center justify-center">
                  <span className="text-gray-900 font-bold text-sm">A</span>
                </div>
                <span className="text-white font-semibold">AJAX SYSTEMS</span>
              </div>
            </div>

            <Button 
              onClick={onStartConfigurator}
              className="bg-orange-600 hover:bg-orange-700"
            >
              Konfigurator starten
              <ArrowRight className="w-4 h-4 ml-2" />
            </Button>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="space-y-8">
              <div>
                <Badge className="bg-orange-600 mb-4">
                  Professionelle Sicherheitslösungen
                </Badge>
                <h1 className="text-5xl font-bold text-white leading-tight mb-6">
                  Ajax Systems
                  <span className="text-orange-400"> Konfigurator</span>
                </h1>
                <p className="text-xl text-gray-300 mb-8">
                  Erstellen Sie Ihre maßgeschneiderte Ajax Sicherheitslösung mit unserem 
                  intelligenten Konfigurator. Von Baseline bis Superior - für jeden Anspruch 
                  die richtige Lösung.
                </p>
              </div>

              <div className="space-y-4">
                <div className="flex items-center gap-3 text-white">
                  <CheckCircle2 className="w-5 h-5 text-green-400" />
                  <span>Über 200 Ajax Produkte verfügbar</span>
                </div>
                <div className="flex items-center gap-3 text-white">
                  <CheckCircle2 className="w-5 h-5 text-green-400" />
                  <span>Automatische Kompatibilitätsprüfung</span>
                </div>
                <div className="flex items-center gap-3 text-white">
                  <CheckCircle2 className="w-5 h-5 text-green-400" />
                  <span>Sofortiger PDF-Kostenvoranschlag</span>
                </div>
                <div className="flex items-center gap-3 text-white">
                  <CheckCircle2 className="w-5 h-5 text-green-400" />
                  <span>18+ Jahre Xortec Erfahrung</span>
                </div>
              </div>

              <div className="flex flex-col sm:flex-row gap-4">
                <Button 
                  onClick={onStartConfigurator}
                  size="lg"
                  className="bg-orange-600 hover:bg-orange-700"
                >
                  Jetzt System konfigurieren
                  <ArrowRight className="w-5 h-5 ml-2" />
                </Button>
                <Button 
                  variant="outline" 
                  size="lg"
                  className="border-gray-600 text-white hover:bg-gray-700"
                >
                  Produktkatalog ansehen
                </Button>
              </div>
            </div>

            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-orange-600 to-orange-400 rounded-2xl transform rotate-3"></div>
              <img 
                src="https://customer-assets.emergentagent.com/job_smart-security-8/artifacts/2d7jgrvk_image.png"
                alt="Ajax Sicherheitssystem"
                className="relative z-10 rounded-2xl shadow-2xl w-full h-96 object-contain bg-white p-4"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Ajax Product Lines Section */}
      <section className="py-16 bg-black/20">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-white mb-4">
              Ajax Produktlinien im Überblick
            </h2>
            <p className="text-xl text-gray-300 max-w-3xl mx-auto">
              Vier spezialisierte Produktlinien für jeden Sicherheitsbedarf - 
              von einfachen Wohnanwendungen bis hin zu professionellen Sicherheitslösungen
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <Card className="bg-gray-800/50 border-gray-700 hover:border-orange-500 transition-all">
              <CardHeader>
                <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center mb-4">
                  <Home className="w-6 h-6 text-white" />
                </div>
                <CardTitle className="text-white">Baseline</CardTitle>
                <CardDescription className="text-gray-300">
                  Für einfachere Anwendungen und Wohnimmobilien
                </CardDescription>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm text-gray-400">
                  <li>• Drahtlose Jeweller-Geräte</li>
                  <li>• Einfache Installation</li>
                  <li>• Grundlegende Sicherheit</li>
                  <li>• Kostengünstig</li>
                </ul>
              </CardContent>
            </Card>

            <Card className="bg-gray-800/50 border-gray-700 hover:border-green-500 transition-all">
              <CardHeader>
                <div className="w-12 h-12 bg-green-600 rounded-lg flex items-center justify-center mb-4">
                  <Building2 className="w-6 h-6 text-white" />
                </div>
                <CardTitle className="text-white">Superior</CardTitle>
                <CardDescription className="text-gray-300">
                  Für Fachleute und anspruchsvolle Projekte
                </CardDescription>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm text-gray-400">
                  <li>• Grade 3 Zertifizierung</li>
                  <li>• Erweiterte Anti-Sabotage</li>
                  <li>• Fibra + Jeweller Support</li>
                  <li>• Professionelle Anwendung</li>
                </ul>
              </CardContent>
            </Card>

            <Card className="bg-gray-800/50 border-gray-700 hover:border-red-500 transition-all">
              <CardHeader>
                <div className="w-12 h-12 bg-red-600 rounded-lg flex items-center justify-center mb-4">
                  <Shield className="w-6 h-6 text-white" />
                </div>
                <CardTitle className="text-white">EN54</CardTitle>
                <CardDescription className="text-gray-300">
                  Spezialisiert für Brandalarmsysteme
                </CardDescription>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm text-gray-400">
                  <li>• EN 54 Zertifizierung</li>
                  <li>• Kommerzielle Gebäude</li>
                  <li>• Brandschutz + Einbruchschutz</li>
                  <li>• Touchscreen CIE</li>
                </ul>
              </CardContent>
            </Card>

            <Card className="bg-gray-800/50 border-gray-700 hover:border-purple-500 transition-all">
              <CardHeader>
                <div className="w-12 h-12 bg-purple-600 rounded-lg flex items-center justify-center mb-4">
                  <Camera className="w-6 h-6 text-white" />
                </div>
                <CardTitle className="text-white">Video</CardTitle>
                <CardDescription className="text-gray-300">
                  Ajax Videoüberwachungsprodukte
                </CardDescription>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm text-gray-400">
                  <li>• IP-Kameras mit KI</li>
                  <li>• NVR-Systeme</li>
                  <li>• Integration in Ajax Hub</li>
                  <li>• Mobile Überwachung</li>
                </ul>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Ajax Advantages Section */}
      <section className="py-16">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-white mb-4">
              Warum Ajax Systems?
            </h2>
            <p className="text-xl text-gray-300">
              Die Vorteile der weltweit führenden drahtlosen Sicherheitstechnik
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-orange-600 rounded-full flex items-center justify-center mx-auto">
                <Wifi className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-semibold text-white">Drahtlose Technologie</h3>
              <p className="text-gray-300">
                Bis zu 2000m Reichweite mit verschlüsselter Jeweller-Technologie. 
                Keine Kabelverlegung erforderlich.
              </p>
            </div>

            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-green-600 rounded-full flex items-center justify-center mx-auto">
                <Smartphone className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-semibold text-white">Mobile Kontrolle</h3>
              <p className="text-gray-300">
                Vollständige Systemkontrolle über Ajax App. Echtzeitbenachrichtigungen 
                und Fernverwaltung.
              </p>
            </div>

            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-blue-600 rounded-full flex items-center justify-center mx-auto">
                <Clock className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-semibold text-white">Langzeitbetrieb</h3>
              <p className="text-gray-300">
                Bis zu 10 Jahre Batterielaufzeit. Wartungsarmer Betrieb für 
                dauerhafte Sicherheit.
              </p>
            </div>

            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-purple-600 rounded-full flex items-center justify-center mx-auto">
                <Camera className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-semibold text-white">Fotoverifizierung</h3>
              <p className="text-gray-300">
                MotionCam Geräte liefern Fotos bei Alarmen. Visuelle Bestätigung 
                für sichere Entscheidungen.
              </p>
            </div>

            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-red-600 rounded-full flex items-center justify-center mx-auto">
                <Shield className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-semibold text-white">Grade 3 Sicherheit</h3>
              <p className="text-gray-300">
                Höchste Sicherheitsstufe nach EN 50131. Professionelle Zertifizierung 
                für kritische Anwendungen.
              </p>
            </div>

            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-yellow-600 rounded-full flex items-center justify-center mx-auto">
                <Zap className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-xl font-semibold text-white">Schnelle Installation</h3>
              <p className="text-gray-300">
                Plug & Play Installation in wenigen Minuten. Automatische Erkennung 
                und Konfiguration aller Geräte.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Xortec Advantages Section */}
      <section className="py-16 bg-black/20">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <Badge className="bg-orange-600 mb-4">
                Über 18 Jahre Erfahrung
              </Badge>
              <h2 className="text-3xl font-bold text-white mb-6">
                Warum Xortec GmbH als Ihr Ajax Partner?
              </h2>
              <p className="text-lg text-gray-300 mb-8">
                Als erfahrener Distributor für Netzwerk- und Sicherheitstechnik 
                bieten wir Ihnen nicht nur Produkte, sondern umfassende Lösungen.
              </p>

              <div className="space-y-4">
                <div className="flex items-start gap-3">
                  <Award className="w-6 h-6 text-orange-400 mt-1" />
                  <div>
                    <h4 className="text-white font-semibold">Zertifizierte Expertise</h4>
                    <p className="text-gray-300 text-sm">
                      Geschulte Ajax-Spezialisten für optimale Beratung und Support
                    </p>
                  </div>
                </div>

                <div className="flex items-start gap-3">
                  <Users className="w-6 h-6 text-orange-400 mt-1" />
                  <div>
                    <h4 className="text-white font-semibold">Persönlicher Service</h4>
                    <p className="text-gray-300 text-sm">
                      Individuelle Beratung und maßgeschneiderte Systemlösungen
                    </p>
                  </div>
                </div>

                <div className="flex items-start gap-3">
                  <Globe className="w-6 h-6 text-orange-400 mt-1" />
                  <div>
                    <h4 className="text-white font-semibold">Deutschlandweiter Support</h4>
                    <p className="text-gray-300 text-sm">
                      Lokale Präsenz mit deutschlandweitem Service-Netzwerk
                    </p>
                  </div>
                </div>

                <div className="flex items-start gap-3">
                  <Clock className="w-6 h-6 text-orange-400 mt-1" />
                  <div>
                    <h4 className="text-white font-semibold">Schnelle Lieferung</h4>
                    <p className="text-gray-300 text-sm">
                      Große Lagerbestände für sofortige Verfügbarkeit
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <div>
              <img 
                src="https://images.pexels.com/photos/60504/security-protection-anti-virus-software-60504.jpeg"
                alt="Xortec Security Solutions"
                className="rounded-2xl shadow-2xl w-full h-96 object-cover"
              />
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold text-white mb-4">
            Starten Sie jetzt mit Ihrem Ajax System
          </h2>
          <p className="text-xl text-gray-300 mb-8 max-w-3xl mx-auto">
            Nutzen Sie unseren intelligenten Konfigurator für eine maßgeschneiderte 
            Ajax Sicherheitslösung. In wenigen Schritten zum perfekten System.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button 
              onClick={onStartConfigurator}
              size="lg"
              className="bg-orange-600 hover:bg-orange-700"
            >
              Konfigurator starten
              <ArrowRight className="w-5 h-5 ml-2" />
            </Button>
            <Button 
              variant="outline" 
              size="lg"
              className="border-gray-600 text-white hover:bg-gray-700"
            >
              Beratungstermin vereinbaren
            </Button>
          </div>
        </div>
      </section>

      {/* Contact Footer */}
      <footer className="bg-black/40 border-t border-gray-700">
        <div className="container mx-auto px-4 py-12">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center gap-3 mb-4">
                <img 
                  src="https://xortec.de/media/0e/72/fc/1691537632/03Logo_linksb%C3%BCndig.png" 
                  alt="Xortec GmbH Logo"
                  className="h-8 w-auto"
                />
              </div>
              <p className="text-gray-400 text-sm">
                Ihr Partner für Netzwerk- und Sicherheitstechnik mit über 18 Jahren Erfahrung.
              </p>
            </div>

            <div>
              <h4 className="text-white font-semibold mb-4">Kontakt</h4>
              <div className="space-y-2 text-sm text-gray-400">
                <div className="flex items-center gap-2">
                  <Phone className="w-4 h-4" />
                  <span>+49 69 5069886 0</span>
                </div>
                <div className="flex items-center gap-2">
                  <Mail className="w-4 h-4" />
                  <span>home@xortec.de</span>
                </div>
                <div className="flex items-start gap-2">
                  <MapPin className="w-4 h-4 mt-1" />
                  <span>Xortec GmbH<br />Berner Str. 79<br />60437 Frankfurt am Main<br />Deutschland</span>
                </div>
              </div>
            </div>

            <div>
              <h4 className="text-white font-semibold mb-4">Produkte</h4>
              <ul className="space-y-2 text-sm text-gray-400">
                <li>Ajax Baseline</li>
                <li>Ajax Superior</li>
                <li>Ajax EN54</li>
                <li>Ajax Video</li>
              </ul>
            </div>

            <div>
              <h4 className="text-white font-semibold mb-4">Service</h4>
              <ul className="space-y-2 text-sm text-gray-400">
                <li>Systemplanung</li>
                <li>Installation</li>
                <li>Support</li>
                <li>Schulungen</li>
              </ul>
            </div>
          </div>

          <div className="border-t border-gray-700 mt-8 pt-8 text-center">
            <p className="text-gray-400 text-sm">
              © 2024 Xortec GmbH. Alle Rechte vorbehalten. 
              <span className="mx-2">|</span>
              <a href="#impressum" className="hover:text-white transition-colors">Impressum</a>
              <span className="mx-2">|</span>
              <a href="#datenschutz" className="hover:text-white transition-colors">Datenschutz</a>
              <span className="mx-2">|</span>
              <a href="#agb" className="hover:text-white transition-colors">AGB</a>
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;