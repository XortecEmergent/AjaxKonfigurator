import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { ArrowLeft, Building2, Mail, Phone, Globe } from 'lucide-react';

const Impressum = ({ onClose }) => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-orange-900 to-gray-800 p-4">
      <div className="container mx-auto max-w-4xl">
        <div className="mb-6">
          <Button 
            onClick={onClose}
            variant="outline"
            className="border-gray-600 text-white hover:bg-gray-700"
          >
            <ArrowLeft className="w-4 h-4 mr-2" />
            Zurück zum Konfigurator
          </Button>
        </div>

        <Card className="bg-gray-800/50 border-gray-700">
          <CardHeader>
            <CardTitle className="text-3xl font-bold text-white text-center">
              Impressum
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-8 text-white">
            {/* Unternehmensangaben */}
            <div className="space-y-4">
              <h2 className="text-xl font-semibold text-orange-400 flex items-center gap-2">
                <Building2 className="w-5 h-5" />
                Angaben gemäß § 5 TMG
              </h2>
              
              <div className="bg-gray-900/50 p-6 rounded-lg">
                <h3 className="text-lg font-semibold mb-4">Xortec GmbH</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <p className="text-gray-300 mb-2">
                      <strong>Geschäftsführer:</strong><br />
                      [Name des Geschäftsführers]
                    </p>
                    <p className="text-gray-300 mb-2">
                      <strong>Adresse:</strong><br />
                      [Straße und Hausnummer]<br />
                      [PLZ] [Stadt]<br />
                      Deutschland
                    </p>
                  </div>
                  <div>
                    <p className="text-gray-300 mb-2 flex items-center gap-2">
                      <Phone className="w-4 h-4" />
                      <strong>Telefon:</strong> +49 (0) XXX XXXXXXX
                    </p>
                    <p className="text-gray-300 mb-2 flex items-center gap-2">
                      <Mail className="w-4 h-4" />
                      <strong>E-Mail:</strong> info@xortec.de
                    </p>
                    <p className="text-gray-300 flex items-center gap-2">
                      <Globe className="w-4 h-4" />
                      <strong>Internet:</strong> www.xortec.de
                    </p>
                  </div>
                </div>
              </div>
            </div>

            {/* Registereintrag */}
            <div className="space-y-4">
              <h2 className="text-xl font-semibold text-orange-400">
                Registereintrag
              </h2>
              <div className="bg-gray-900/50 p-6 rounded-lg">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <p className="text-gray-300">
                    <strong>Eintragung im Handelsregister:</strong><br />
                    Registergericht: [Amtsgericht]<br />
                    Registernummer: HRB XXXXX
                  </p>
                  <p className="text-gray-300">
                    <strong>Umsatzsteuer-ID:</strong><br />
                    Umsatzsteuer-Identifikationsnummer<br />
                    gemäß §27a Umsatzsteuergesetz:<br />
                    DE XXXXXXXXX
                  </p>
                </div>
              </div>
            </div>

            {/* Verantwortlicher Inhalt */}
            <div className="space-y-4">
              <h2 className="text-xl font-semibold text-orange-400">
                Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV
              </h2>
              <div className="bg-gray-900/50 p-6 rounded-lg">
                <p className="text-gray-300">
                  [Name]<br />
                  [Straße und Hausnummer]<br />
                  [PLZ] [Stadt]
                </p>
              </div>
            </div>

            {/* Haftungsausschluss */}
            <div className="space-y-4">
              <h2 className="text-xl font-semibold text-orange-400">
                Haftungsausschluss (Disclaimer)
              </h2>
              
              <div className="space-y-4">
                <div className="bg-gray-900/50 p-6 rounded-lg">
                  <h3 className="text-lg font-semibold mb-3">Haftung für Inhalte</h3>
                  <p className="text-gray-300 text-sm leading-relaxed">
                    Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den 
                    allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht 
                    unter der Verpflichtung, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach 
                    Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.
                  </p>
                </div>

                <div className="bg-gray-900/50 p-6 rounded-lg">
                  <h3 className="text-lg font-semibold mb-3">Haftung für Links</h3>
                  <p className="text-gray-300 text-sm leading-relaxed">
                    Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. 
                    Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten 
                    Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich.
                  </p>
                </div>

                <div className="bg-gray-900/50 p-6 rounded-lg">
                  <h3 className="text-lg font-semibold mb-3">Urheberrecht</h3>
                  <p className="text-gray-300 text-sm leading-relaxed">
                    Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen 
                    Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der 
                    Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.
                  </p>
                </div>
              </div>
            </div>

            {/* Ajax Systems Hinweis */}
            <div className="space-y-4">
              <h2 className="text-xl font-semibold text-orange-400">
                Hinweis zu Ajax Systems
              </h2>
              <div className="bg-gray-900/50 p-6 rounded-lg">
                <p className="text-gray-300 text-sm leading-relaxed">
                  Xortec GmbH ist autorisierter Distributor für Ajax Systems Produkte in Deutschland. 
                  Ajax Systems ist eine eingetragene Marke der Ajax Systems LLC. Alle Produktinformationen, 
                  Bilder und Spezifikationen werden mit freundlicher Genehmigung von Ajax Systems verwendet. 
                  Dieser Konfigurator dient der vereinfachten Produktauswahl und ersetzt nicht die 
                  professionelle Beratung durch unsere Experten.
                </p>
              </div>
            </div>

            {/* Online-Streitbeilegung */}
            <div className="space-y-4">
              <h2 className="text-xl font-semibold text-orange-400">
                Online-Streitbeilegung
              </h2>
              <div className="bg-gray-900/50 p-6 rounded-lg">
                <p className="text-gray-300 text-sm leading-relaxed">
                  Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: 
                  <a 
                    href="https://ec.europa.eu/consumers/odr/" 
                    className="text-orange-400 hover:text-orange-300 ml-1"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    https://ec.europa.eu/consumers/odr/
                  </a>
                  <br /><br />
                  Unsere E-Mail-Adresse finden Sie oben im Impressum. Wir sind nicht bereit oder verpflichtet, 
                  an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.
                </p>
              </div>
            </div>

            {/* Letzte Aktualisierung */}
            <div className="text-center pt-6 border-t border-gray-600">
              <p className="text-gray-400 text-sm">
                Letzte Aktualisierung: {new Date().toLocaleDateString('de-DE')}
              </p>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Impressum;