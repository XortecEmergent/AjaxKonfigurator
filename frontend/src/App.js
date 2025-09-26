import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import { Button } from './components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from './components/ui/tabs';
import { Badge } from './components/ui/badge';
import { Progress } from './components/ui/progress';
import { ArrowRight, ArrowLeft, Settings, ShoppingCart, Download, CheckCircle2, Info, Zap, Shield, Wifi, Plus, Minus, AlertCircle } from 'lucide-react';
import LandingPage from './components/LandingPage';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

function App() {
  // State Management
  const [showLandingPage, setShowLandingPage] = useState(true);
  const [currentStep, setCurrentStep] = useState(1);
  const [productLines, setProductLines] = useState([]);
  const [categories, setCategories] = useState([]);
  const [products, setProducts] = useState([]);
  const [selectedProductLine, setSelectedProductLine] = useState('');
  const [selectedHub, setSelectedHub] = useState(null);
  const [selectedProducts, setSelectedProducts] = useState([]);
  const [productQuantities, setProductQuantities] = useState({});
  const [compatibleProducts, setCompatibleProducts] = useState([]);
  const [capacityWarnings, setCapacityWarnings] = useState([]);
  const [loading, setLoading] = useState(false);
  const [configuration, setConfiguration] = useState({
    name: '',
    description: ''
  });

  const totalSteps = 5;

  // API Calls
  const fetchProductLines = async () => {
    try {
      const response = await axios.get(`${API}/product-lines`);
      setProductLines(response.data.product_lines);
    } catch (error) {
      console.error('Error fetching product lines:', error);
    }
  };

  const fetchCategories = async () => {
    try {
      const response = await axios.get(`${API}/categories`);
      setCategories(response.data.categories);
    } catch (error) {
      console.error('Error fetching categories:', error);
    }
  };

  const fetchProducts = async (productLine = '', category = '') => {
    try {
      setLoading(true);
      const params = new URLSearchParams();
      if (productLine) params.append('product_line', productLine);
      if (category) params.append('category', category);
      
      const response = await axios.get(`${API}/products?${params}`);
      setProducts(response.data);
    } catch (error) {
      console.error('Error fetching products:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchCompatibleDevices = async (hubId) => {
    try {
      setLoading(true);
      const response = await axios.get(`${API}/compatibility/${hubId}`);
      setCompatibleProducts(response.data);
    } catch (error) {
      console.error('Error fetching compatible devices:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProductLines();
    fetchCategories();
  }, []);

  // Step Functions
  const nextStep = () => {
    if (currentStep < totalSteps) {
      setCurrentStep(currentStep + 1);
    }
  };

  const prevStep = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1);
    }
  };

  const selectProductLine = (productLine) => {
    setSelectedProductLine(productLine.id);
    fetchProducts(productLine.id);
    nextStep();
  };

  const selectHub = (hub) => {
    setSelectedHub(hub);
    setSelectedProducts([hub.id]);
    fetchCompatibleDevices(hub.id);
    nextStep();
  };

  const toggleProduct = (product) => {
    const isSelected = selectedProducts.includes(product.id);
    if (isSelected) {
      setSelectedProducts(selectedProducts.filter(id => id !== product.id));
    } else {
      setSelectedProducts([...selectedProducts, product.id]);
    }
  };

  const saveConfiguration = async () => {
    try {
      const configData = {
        name: configuration.name || `${selectedProductLine} System`,
        description: configuration.description || 'Ajax System Konfiguration via Xortec GmbH',
        product_line: selectedProductLine,
        selected_products: selectedProducts
      };

      const response = await axios.post(`${API}/configurations`, configData);
      console.log('Configuration saved:', response.data);
      nextStep();
    } catch (error) {
      console.error('Error saving configuration:', error);
    }
  };

  const generatePDF = async () => {
    try {
      // For now, show success message
      alert('PDF-Export erfolgreich! In einer vollständigen Implementation würde hier ein PDF heruntergeladen werden.');
      console.log('PDF Generation for configuration');
    } catch (error) {
      console.error('Error generating PDF:', error);
      alert('Fehler beim Erstellen des PDF-Exports');
    }
  };

  // Component Renderers
  const renderProductLineSelection = () => (
    <div className="space-y-6">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-white mb-4">
          Wählen Sie Ihre Ajax Produktlinie
        </h2>
        <p className="text-xl text-gray-300 mb-8">
          Jede Produktlinie ist für spezifische Anwendungsbereiche optimiert
        </p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {productLines.map((line) => (
          <Card 
            key={line.id} 
            className="cursor-pointer transition-all duration-300 hover:scale-105 hover:shadow-xl bg-gray-800/50 border-gray-700 hover:border-orange-500"
            onClick={() => selectProductLine(line)}
            data-testid={`product-line-${line.id}`}
          >
            <div className="relative overflow-hidden rounded-t-lg">
              <img 
                src={line.image} 
                alt={line.name}
                className="w-full h-48 object-cover"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
              <Badge className="absolute top-4 right-4 bg-orange-600">
                {line.name}
              </Badge>
            </div>
            
            <CardHeader>
              <CardTitle className="text-white flex items-center gap-2">
                <Shield className="w-5 h-5" />
                {line.name}
              </CardTitle>
              <CardDescription className="text-gray-300">
                {line.description}
              </CardDescription>
            </CardHeader>
            
            <CardContent>
              <div className="space-y-2 mb-4">
                <p className="text-sm text-gray-400">
                  <strong>Zielgruppe:</strong> {line.target_group}
                </p>
                <div className="flex flex-wrap gap-2">
                  {line.features.map((feature, idx) => (
                    <Badge key={idx} variant="secondary" className="text-xs">
                      {feature}
                    </Badge>
                  ))}
                </div>
              </div>
              
              <Button className="w-full bg-orange-600 hover:bg-orange-700">
                <ArrowRight className="w-4 h-4 ml-2" />
                Auswählen
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );

  const renderHubSelection = () => {
    const hubs = products.filter(p => p.category === 'hubs');
    
    return (
      <div className="space-y-6">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-white mb-4">
            Wählen Sie Ihre Hub-Zentrale
          </h2>
          <p className="text-xl text-gray-300 mb-8">
            Die Hub-Zentrale ist das Herzstück Ihres Ajax Systems
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {hubs.map((hub) => (
            <Card 
              key={hub.id}
              className="cursor-pointer transition-all duration-300 hover:scale-105 bg-gray-800/50 border-gray-700 hover:border-green-500"
              onClick={() => selectHub(hub)}
              data-testid={`hub-${hub.name.replace(/\s+/g, '-').toLowerCase()}`}
            >
              <div className="relative">
                <img 
                  src={hub.image_url} 
                  alt={hub.name}
                  className="w-full h-40 object-contain bg-gray-900 p-4"
                />
                <Badge className="absolute top-2 right-2 bg-green-600">
                  Hub
                </Badge>
              </div>
              
              <CardHeader>
                <CardTitle className="text-white text-lg">{hub.name}</CardTitle>
                <CardDescription className="text-gray-300">
                  {hub.short_description}
                </CardDescription>
              </CardHeader>
              
              <CardContent>
                <div className="space-y-3">
                  <div className="flex flex-wrap gap-1">
                    {hub.usps.slice(0, 3).map((usp, idx) => (
                      <Badge key={idx} variant="outline" className="text-xs border-gray-600">
                        {usp}
                      </Badge>
                    ))}
                  </div>
                  
                  <div className="space-y-2 text-sm text-gray-400">
                    <div className="flex items-center gap-2">
                      <Zap className="w-4 h-4" />
                      <span>Max. {hub.specifications.max_devices} Geräte</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <Wifi className="w-4 h-4" />
                      <span>{hub.specifications.frequency}</span>
                    </div>
                  </div>
                  
                  <Button className="w-full bg-green-600 hover:bg-green-700">
                    Hub auswählen
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    );
  };

  const renderProductSelection = () => {
    const productsByCategory = categories.reduce((acc, category) => {
      const categoryProducts = compatibleProducts.filter(p => p.category === category.id);
      if (categoryProducts.length > 0) {
        acc[category.id] = {
          ...category,
          products: categoryProducts
        };
      }
      return acc;
    }, {});

    return (
      <div className="space-y-6">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-white mb-4">
            Wählen Sie Ihre Sicherheitsgeräte
          </h2>
          <p className="text-xl text-gray-300 mb-8">
            Kompatible Geräte für Ihre {selectedHub?.name}
          </p>
        </div>

        <Tabs defaultValue={Object.keys(productsByCategory)[0]} className="w-full">
          <TabsList className="grid w-full grid-cols-4 lg:grid-cols-6 bg-gray-800">
            {Object.values(productsByCategory).map((category) => (
              <TabsTrigger 
                key={category.id} 
                value={category.id}
                className="data-[state=active]:bg-orange-600 text-xs"
              >
                {category.name}
              </TabsTrigger>
            ))}
          </TabsList>

          {Object.entries(productsByCategory).map(([categoryId, category]) => (
            <TabsContent key={categoryId} value={categoryId} className="mt-6">
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {category.products.map((product) => {
                  const isSelected = selectedProducts.includes(product.id);
                  return (
                    <Card 
                      key={product.id}
                      className={`cursor-pointer transition-all duration-300 ${
                        isSelected 
                          ? 'ring-2 ring-orange-500 bg-orange-900/30' 
                          : 'hover:scale-105 bg-gray-800/50'
                      } border-gray-700`}
                      onClick={() => toggleProduct(product)}
                      data-testid={`product-${product.name.replace(/\s+/g, '-').toLowerCase()}`}
                    >
                      <div className="relative">
                        <img 
                          src={product.image_url} 
                          alt={product.name}
                          className="w-full h-32 object-contain bg-gray-900 p-2"
                        />
                        {isSelected && (
                          <CheckCircle2 className="absolute top-2 right-2 w-6 h-6 text-orange-500" />
                        )}
                      </div>
                      
                      <CardHeader className="pb-2">
                        <CardTitle className="text-white text-base leading-tight">
                          {product.name}
                        </CardTitle>
                        <CardDescription className="text-gray-300 text-sm">
                          {product.short_description}
                        </CardDescription>
                      </CardHeader>
                      
                      <CardContent>
                        <div className="space-y-2">
                          <div className="flex flex-wrap gap-1">
                            {product.usps.slice(0, 2).map((usp, idx) => (
                              <Badge key={idx} variant="secondary" className="text-xs">
                                {usp}
                              </Badge>
                            ))}
                          </div>
                          
                          <div className="text-xs text-gray-400 space-y-1">
                            {product.specifications.range && (
                              <div>Reichweite: {product.specifications.range}</div>
                            )}
                            {product.specifications.battery_life && (
                              <div>Batterie: {product.specifications.battery_life}</div>
                            )}
                          </div>
                        </div>
                      </CardContent>
                    </Card>
                  );
                })}
              </div>
            </TabsContent>
          ))}
        </Tabs>

        <div className="flex justify-between items-center pt-6">
          <p className="text-gray-300">
            {selectedProducts.length - 1} Geräte ausgewählt (+ 1 Hub)
          </p>
          <Button 
            onClick={nextStep}
            disabled={selectedProducts.length < 2}
            className="bg-orange-600 hover:bg-orange-700"
            data-testid="continue-to-summary"
          >
            Weiter zur Zusammenfassung
            <ArrowRight className="w-4 h-4 ml-2" />
          </Button>
        </div>
      </div>
    );
  };

  const renderSummary = () => {
    const selectedProductsData = products.filter(p => selectedProducts.includes(p.id));
    const hubData = selectedProductsData.find(p => p.category === 'hubs');
    const devicesData = selectedProductsData.filter(p => p.category !== 'hubs');

    return (
      <div className="space-y-6">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-white mb-4">
            Ihre Ajax System Konfiguration
          </h2>
          <p className="text-xl text-gray-300 mb-8">
            Überprüfen Sie Ihre Auswahl und vervollständigen Sie die Konfiguration
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Hub Section */}
          <Card className="lg:col-span-1 bg-gray-800/50 border-gray-700">
            <CardHeader>
              <CardTitle className="text-white flex items-center gap-2">
                <Settings className="w-5 h-5" />
                Hub-Zentrale
              </CardTitle>
            </CardHeader>
            <CardContent>
              {hubData && (
                <div className="flex items-center gap-3">
                  <img 
                    src={hubData.image_url} 
                    alt={hubData.name}
                    className="w-16 h-16 object-contain bg-gray-900 rounded p-2"
                  />
                  <div>
                    <h4 className="text-white font-medium">{hubData.name}</h4>
                    <p className="text-gray-400 text-sm">{hubData.short_description}</p>
                  </div>
                </div>
              )}
            </CardContent>
          </Card>

          {/* Devices Section */}
          <Card className="lg:col-span-2 bg-gray-800/50 border-gray-700">
            <CardHeader>
              <CardTitle className="text-white flex items-center gap-2">
                <ShoppingCart className="w-5 h-5" />
                Ausgewählte Geräte ({devicesData.length})
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {devicesData.map((device) => (
                  <div key={device.id} className="flex items-center gap-3 p-3 bg-gray-900/50 rounded-lg">
                    <img 
                      src={device.image_url} 
                      alt={device.name}
                      className="w-12 h-12 object-contain bg-gray-800 rounded p-1"
                    />
                    <div className="flex-1">
                      <h5 className="text-white text-sm font-medium">{device.name}</h5>
                      <p className="text-gray-400 text-xs">{device.short_description}</p>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Configuration Details */}
        <Card className="bg-gray-800/50 border-gray-700">
          <CardHeader>
            <CardTitle className="text-white">Konfiguration benennen</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div>
              <label className="block text-white text-sm font-medium mb-2">
                Konfigurationsname
              </label>
              <input
                type="text"
                value={configuration.name}
                onChange={(e) => setConfiguration({...configuration, name: e.target.value})}
                placeholder={`${selectedProductLine} System`}
                className="w-full p-3 bg-gray-900 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:border-orange-500 focus:ring-1 focus:ring-orange-500"
                data-testid="config-name-input"
              />
            </div>
            <div>
              <label className="block text-white text-sm font-medium mb-2">
                Beschreibung (optional)
              </label>
              <textarea
                value={configuration.description}
                onChange={(e) => setConfiguration({...configuration, description: e.target.value})}
                placeholder="Beschreibung Ihres Systems..."
                rows="3"
                className="w-full p-3 bg-gray-900 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:border-orange-500 focus:ring-1 focus:ring-orange-500"
                data-testid="config-description-input"
              />
            </div>
          </CardContent>
        </Card>

        <div className="flex justify-between">
          <Button 
            onClick={prevStep} 
            variant="outline" 
            className="border-gray-600 text-white hover:bg-gray-700"
          >
            <ArrowLeft className="w-4 h-4 mr-2" />
            Zurück
          </Button>
          <Button 
            onClick={saveConfiguration}
            className="bg-green-600 hover:bg-green-700"
            data-testid="save-configuration"
          >
            Konfiguration speichern
            <CheckCircle2 className="w-4 h-4 ml-2" />
          </Button>
        </div>
      </div>
    );
  };

  const renderComplete = () => (
    <div className="text-center space-y-6">
      <div className="flex justify-center">
        <CheckCircle2 className="w-20 h-20 text-green-500" />
      </div>
      
      <h2 className="text-3xl font-bold text-white">
        Konfiguration erfolgreich erstellt!
      </h2>
      
      <p className="text-xl text-gray-300 max-w-2xl mx-auto">
        Ihre Ajax System Konfiguration wurde erfolgreich gespeichert. 
        Sie können jetzt ein PDF-Angebot generieren oder eine neue Konfiguration erstellen.
      </p>

      <div className="flex flex-col sm:flex-row gap-4 justify-center">
        <Button 
          onClick={generatePDF}
          className="bg-orange-600 hover:bg-orange-700"
          data-testid="generate-pdf"
        >
          <Download className="w-4 h-4 mr-2" />
          PDF-Angebot generieren
        </Button>
        <Button 
          onClick={() => window.location.reload()}
          variant="outline"
          className="border-gray-600 text-white hover:bg-gray-700"
        >
          Neue Konfiguration
        </Button>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-orange-900 to-gray-800">
      {/* Header */}
      <header className="bg-black/20 backdrop-blur-sm border-b border-gray-700">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="w-10 h-10 bg-orange-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-lg">X</span>
              </div>
              <div>
                <h1 className="text-2xl font-bold text-white">
                  Ajax Systemkonfigurator
                </h1>
                <p className="text-sm text-orange-200">by Xortec GmbH</p>
              </div>
            </div>
            <Badge className="bg-orange-600">
              Schritt {currentStep} von {totalSteps}
            </Badge>
          </div>
          
          {/* Progress Bar */}
          <div className="mt-4">
            <Progress 
              value={(currentStep / totalSteps) * 100} 
              className="h-2 bg-gray-700"
            />
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-6xl mx-auto">
          {loading && (
            <div className="text-center py-12">
              <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-white"></div>
              <p className="text-white mt-4">Lade Produkte...</p>
            </div>
          )}

          {!loading && (
            <>
              {currentStep === 1 && renderProductLineSelection()}
              {currentStep === 2 && renderHubSelection()}
              {currentStep === 3 && renderProductSelection()}
              {currentStep === 4 && renderSummary()}
              {currentStep === 5 && renderComplete()}
            </>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-black/20 border-t border-gray-700 mt-12">
        <div className="container mx-auto px-4 py-6">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-gray-400 text-sm">
              © 2024 Xortec GmbH. Alle Rechte vorbehalten. Ajax Systems Konfigurator.
            </p>
            <div className="flex items-center gap-4 text-sm text-gray-400">
              <a href="#" className="hover:text-white transition-colors">
                <Info className="w-4 h-4 inline mr-1" />
                Produktkatalog
              </a>
              <a href="#" className="hover:text-white transition-colors">
                Support
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;