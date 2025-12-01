import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Progress } from './ui/progress';
import { Tabs, TabsContent, TabsList, TabsTrigger } from './ui/tabs';
import { ArrowRight, ArrowLeft, Settings, FileSpreadsheet, Plus, Minus, AlertCircle, Info, CheckCircle2 } from 'lucide-react';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const ConfiguratorComplete = ({ onShowImpressum }) => {
  // State Management
  const [currentStep, setCurrentStep] = useState(1);
  const [productLines, setProductLines] = useState([]);
  const [categories, setCategories] = useState([]);
  const [products, setProducts] = useState([]);
  const [selectedProductLine, setSelectedProductLine] = useState('');
  const [selectedHub, setSelectedHub] = useState(null);
  const [selectedNVR, setSelectedNVR] = useState(null);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [selectedProducts, setSelectedProducts] = useState([]);
  const [productQuantities, setProductQuantities] = useState({});
  const [hubQuantities, setHubQuantities] = useState({});
  const [nvrQuantities, setNvrQuantities] = useState({});

  const steps = [
    { number: 1, title: 'Produktlinie auswählen' },
    { 
      number: 2, 
      title: selectedProductLine?.includes('video') ? 'NVR auswählen' : 'Hub auswählen'
    },
    { number: 3, title: 'Komponenten auswählen' },
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

  const fetchCategories = async (productLine = null) => {
    try {
      const url = productLine ? `${API}/categories?product_line=${productLine}` : `${API}/categories`;
      const response = await axios.get(url);
      setCategories(response.data.categories || []);
    } catch (error) {
      console.error('Error fetching categories:', error);
    }
  };

  const fetchProducts = async (productLine = '', category = '') => {
    try {
      const params = new URLSearchParams();
      if (productLine) params.append('product_line', productLine);
      if (category) params.append('category', category);
      
      const response = await axios.get(`${API}/products?${params.toString()}`);
      setProducts(Array.isArray(response.data) ? response.data : []);
    } catch (error) {
      console.error('Error fetching products:', error);
      setProducts([]);
    }
  };

  // Hub/NVR specific fetching
  const fetchHubsOrNVRs = async (productLine) => {
    try {
      const category = productLine?.includes('video') ? 'nvrs' : 'hubs';
      const response = await axios.get(`${API}/products?product_line=${productLine}&category=${category}`);
      setProducts(Array.isArray(response.data) ? response.data : []);
    } catch (error) {
      console.error(`Error fetching ${category}:`, error);
      setProducts([]);
    }
  };

  // Capacity Calculations
  const calculateHubCapacity = () => {
    if (!selectedHub) return { total: 0, used: 0 };
    
    const hubQuantity = hubQuantities[selectedHub.id] || 1;
    const devicesPerHub = selectedHub.specifications?.max_devices || 200;
    const total = devicesPerHub * hubQuantity;
    
    const used = selectedProducts.reduce((sum, product) => {
      return sum + (productQuantities[product.id] || 1);
    }, 0);
    
    return { total, used };
  };

  const calculateNVRCapacity = () => {
    if (!selectedNVR) return { total: 0, used: 0 };
    
    const nvrQuantity = nvrQuantities[selectedNVR.id] || 1;
    const camerasPerNVR = selectedNVR.specifications?.max_cameras || 8;
    const total = camerasPerNVR * nvrQuantity;
    
    const used = selectedProducts
      .filter(product => product.category === 'cameras' || product.category === 'wifi_cameras')
      .reduce((sum, product) => sum + (productQuantities[product.id] || 1), 0);
    
    return { total, used };
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

  const goToStep = (stepNumber) => {
    setCurrentStep(stepNumber);
  };

  // Product Line Selection
  const selectProductLine = (productLine) => {
    setSelectedProductLine(productLine.id);
    setSelectedHub(null);
    setSelectedNVR(null);
    setSelectedCategory('');
    setSelectedProducts([]);
    setProductQuantities({});
    setHubQuantities({});
    setNvrQuantities({});
    fetchCategories(productLine.id);
    nextStep();
  };

  // Hub/NVR Selection
  const selectHubOrNVR = (item) => {
    if (selectedProductLine?.includes('video')) {
      setSelectedNVR(item);
      setNvrQuantities({ [item.id]: 1 });
    } else {
      setSelectedHub(item);
      setHubQuantities({ [item.id]: 1 });
    }
    nextStep();
  };

  // Product Selection
  const toggleProduct = (product) => {
    const isSelected = selectedProducts.some(p => p.id === product.id);
    if (isSelected) {
      setSelectedProducts(selectedProducts.filter(p => p.id !== product.id));
      setProductQuantities(prev => {
        const updated = { ...prev };
        delete updated[product.id];
        return updated;
      });
    } else {
      setSelectedProducts([...selectedProducts, product]);
      setProductQuantities(prev => ({ ...prev, [product.id]: 1 }));
    }
  };

  const updateQuantity = (productId, delta) => {
    setProductQuantities(prev => {
      const currentQuantity = prev[productId] || 1;
      const newQuantity = Math.max(1, currentQuantity + delta);
      return { ...prev, [productId]: newQuantity };
    });
  };

  const updateHubQuantity = (hubId, delta) => {
    setHubQuantities(prev => {
      const currentQuantity = prev[hubId] || 1;
      const newQuantity = Math.max(1, currentQuantity + delta);
      return { ...prev, [hubId]: newQuantity };
    });
  };

  const updateNVRQuantity = (nvrId, delta) => {
    setNvrQuantities(prev => {
      const currentQuantity = prev[nvrId] || 1;
      const newQuantity = Math.max(1, currentQuantity + delta);
      return { ...prev, [nvrId]: newQuantity };
    });
  };

  // Effects
  useEffect(() => {
    fetchProductLines();
    fetchCategories();
  }, []);

  useEffect(() => {
    if (selectedProductLine && currentStep === 2) {
      fetchHubsOrNVRs(selectedProductLine);
    }
  }, [selectedProductLine, currentStep]);

  useEffect(() => {
    if (selectedCategory && selectedProductLine) {
      fetchProducts(selectedProductLine, selectedCategory);
    }
  }, [selectedCategory, selectedProductLine]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-white">
      {/* Header */}
      <div className="bg-white/95 backdrop-blur-sm border-b border-gray-100 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center space-x-8">
              <img
                src="https://xortec.de/media/image/c6/55/58/xortec_logo_ohne_zusatz200x34.png"
                alt="Xortec GmbH"
                className="h-8"
              />
              <div className="hidden md:flex items-center space-x-2">
                <span className="text-gray-400">×</span>
                <img
                  src="https://ajax.systems/assets/img/logo/ajax-logo.svg"
                  alt="Ajax Systems"
                  className="h-6 filter brightness-0"
                />
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
                <button
                  onClick={() => currentStep > step.number ? goToStep(step.number) : null}
                  className={`flex items-center justify-center w-8 h-8 rounded-full font-medium text-sm transition-colors ${
                    currentStep >= step.number 
                      ? 'bg-black text-white' 
                      : 'bg-gray-200 text-gray-600'
                  } ${currentStep > step.number ? 'cursor-pointer hover:bg-gray-800' : ''}`}
                  disabled={currentStep <= step.number}
                >
                  {step.number}
                </button>
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

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {productLines.map((line) => (
                <Card 
                  key={line.id} 
                  className="group cursor-pointer hover:shadow-xl transition-all duration-300 border-gray-200 hover:border-black bg-white overflow-hidden"
                  onClick={() => selectProductLine(line)}
                >
                  <div className="aspect-video overflow-hidden">
                    <img 
                      src={line.image_url} 
                      alt={line.name}
                      className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                      onError={(e) => {
                        e.target.style.display = 'none';
                      }}
                    />
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

        {/* Step 2: Hub/NVR Selection */}
        {currentStep === 2 && (
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-3xl font-bold text-gray-900 mb-4">
                {selectedProductLine?.includes('video') ? 'NVR auswählen' : 'Hub auswählen'}
              </h2>
              <p className="text-lg text-gray-600">
                {selectedProductLine?.includes('video') 
                  ? 'Netzwerk-Videorekorder für Ihre Kamera-Installation'
                  : 'Die Zentrale Ihres Ajax Security Systems'
                }
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {products.map((product) => {
                const isSelected = selectedProductLine?.includes('video') 
                  ? selectedNVR?.id === product.id
                  : selectedHub?.id === product.id;
                
                return (
                  <Card 
                    key={product.id} 
                    className={`group cursor-pointer transition-all duration-300 border-gray-200 hover:border-black hover:shadow-lg ${
                      isSelected ? 'ring-2 ring-black border-black shadow-lg' : ''
                    }`}
                    onClick={() => selectHubOrNVR(product)}
                  >
                    <div className="aspect-square p-6 bg-gray-50 group-hover:bg-gray-100 transition-colors">
                      <img 
                        src={product.image_url} 
                        alt={product.name}
                        className="w-full h-full object-contain"
                        onError={(e) => {
                          e.target.style.display = 'none';
                        }}
                      />
                    </div>
                    <CardHeader>
                      <CardTitle className="text-lg font-semibold text-gray-900">
                        {product.name}
                      </CardTitle>
                      <CardDescription className="text-sm text-gray-600">
                        {product.short_description}
                      </CardDescription>
                    </CardHeader>
                    <CardContent>
                      <div className="flex flex-wrap gap-1 mb-4">
                        {product.usps.slice(0, 4).map((usp, idx) => (
                          <Badge key={idx} variant="outline" className="text-xs">
                            {usp}
                          </Badge>
                        ))}
                      </div>
                      <div className="space-y-2 text-sm text-gray-700">
                        {selectedProductLine?.includes('video') ? (
                          <div>
                            <strong>Kanäle:</strong> {product.specifications?.max_cameras || product.specifications?.channels} Kameras
                          </div>
                        ) : (
                          <div>
                            <strong>Kapazität:</strong> {product.specifications?.max_devices} Geräte
                          </div>
                        )}
                      </div>
                    </CardContent>
                  </Card>
                );
              })}
            </div>

            <div className="flex justify-between">
              <Button onClick={prevStep} variant="outline">
                <ArrowLeft className="h-4 w-4 mr-2" />
                Zurück
              </Button>
              
              {((selectedProductLine?.includes('video') && selectedNVR) || 
                (!selectedProductLine?.includes('video') && selectedHub)) && (
                <Button onClick={nextStep}>
                  Weiter
                  <ArrowRight className="h-4 w-4 ml-2" />
                </Button>
              )}
            </div>
          </div>
        )}

        {/* Step 3: Component Selection */}
        {currentStep === 3 && (
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-3xl font-bold text-gray-900 mb-4">Komponenten auswählen</h2>
              <p className="text-lg text-gray-600">
                Wählen Sie die gewünschten Sicherheitskomponenten für Ihr System
              </p>
            </div>

            {/* Capacity Status */}
            {(selectedHub || selectedNVR) && (
              <Card className="bg-blue-50 border-blue-200">
                <CardHeader>
                  <CardTitle className="text-lg font-semibold flex items-center">
                    <Info className="h-5 w-5 mr-2 text-blue-600" />
                    {selectedProductLine?.includes('video') ? 'Kamera-Kapazität' : 'Hub-Kapazität'}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  {(() => {
                    const capacity = selectedProductLine?.includes('video') 
                      ? calculateNVRCapacity() 
                      : calculateHubCapacity();
                    const percentage = capacity.total > 0 ? (capacity.used / capacity.total) * 100 : 0;
                    
                    return (
                      <div className="space-y-3">
                        <div className="flex justify-between items-center">
                          <span>Verfügbare Kanäle/Geräte:</span>
                          <span className="font-medium">{capacity.total}</span>
                        </div>
                        <div className="flex justify-between items-center">
                          <span>Verwendete Kanäle/Geräte:</span>
                          <span className="font-medium">{capacity.used}</span>
                        </div>
                        <div className="flex justify-between items-center">
                          <span>Freie Kanäle/Geräte:</span>
                          <span className="font-medium">{capacity.total - capacity.used}</span>
                        </div>
                        <Progress value={percentage} className="h-2" />
                        {capacity.used > capacity.total && (
                          <div className="flex items-center space-x-2 text-red-600">
                            <AlertCircle className="h-4 w-4" />
                            <span className="text-sm">Warnung: Kapazität überschritten!</span>
                          </div>
                        )}
                      </div>
                    );
                  })()}
                </CardContent>
              </Card>
            )}

            {/* Category Tabs */}
            <Tabs value={selectedCategory} onValueChange={setSelectedCategory}>
              <TabsList className="grid w-full grid-cols-2 md:grid-cols-4 lg:grid-cols-5 bg-gray-100">
                {categories.map((category) => (
                  <TabsTrigger 
                    key={category.id} 
                    value={category.id}
                    className="data-[state=active]:bg-white data-[state=active]:text-black font-medium text-xs"
                  >
                    {category.name}
                  </TabsTrigger>
                ))}
              </TabsList>

              {categories.map((category) => (
                <TabsContent key={category.id} value={category.id} className="mt-6">
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {products.map((product) => {
                      const isSelected = selectedProducts.some(p => p.id === product.id);
                      const quantity = productQuantities[product.id] || 1;
                      
                      return (
                        <Card 
                          key={product.id} 
                          className={`group transition-all duration-300 border-gray-200 hover:shadow-lg ${
                            isSelected ? 'ring-2 ring-black border-black shadow-lg' : 'hover:border-gray-300'
                          }`}
                        >
                          <div className="aspect-square p-4 bg-gray-50 group-hover:bg-gray-100 transition-colors">
                            <img 
                              src={product.image_url} 
                              alt={product.name}
                              className="w-full h-full object-contain"
                              onError={(e) => {
                                e.target.style.display = 'none';
                              }}
                            />
                          </div>
                          <CardHeader className="pb-2">
                            <CardTitle className="text-lg font-semibold text-gray-900">
                              {product.name}
                            </CardTitle>
                            <CardDescription className="text-sm text-gray-600">
                              {product.short_description}
                            </CardDescription>
                          </CardHeader>
                          <CardContent className="space-y-4">
                            <div className="flex flex-wrap gap-1">
                              {product.usps.slice(0, 3).map((usp, idx) => (
                                <Badge key={idx} variant="outline" className="text-xs">
                                  {usp}
                                </Badge>
                              ))}
                            </div>
                            
                            <div className="flex items-center justify-between">
                              <Button
                                onClick={() => toggleProduct(product)}
                                variant={isSelected ? "default" : "outline"}
                                size="sm"
                                className={isSelected ? "bg-black hover:bg-gray-800" : ""}
                              >
                                {isSelected ? (
                                  <>
                                    <CheckCircle2 className="h-4 w-4 mr-2" />
                                    Ausgewählt
                                  </>
                                ) : (
                                  <>
                                    <Plus className="h-4 w-4 mr-2" />
                                    Hinzufügen
                                  </>
                                )}
                              </Button>
                              
                              {isSelected && (
                                <div className="flex items-center space-x-2">
                                  <Button
                                    size="sm"
                                    variant="outline"
                                    onClick={() => updateQuantity(product.id, -1)}
                                  >
                                    <Minus className="h-4 w-4" />
                                  </Button>
                                  <span className="font-medium min-w-[2rem] text-center">{quantity}</span>
                                  <Button
                                    size="sm"
                                    variant="outline"
                                    onClick={() => updateQuantity(product.id, 1)}
                                  >
                                    <Plus className="h-4 w-4" />
                                  </Button>
                                </div>
                              )}
                            </div>
                          </CardContent>
                        </Card>
                      );
                    })}
                  </div>
                </TabsContent>
              ))}
            </Tabs>

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
                {/* Product Line */}
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
                        {productLines.find(pl => pl.id === selectedProductLine)?.target_group}
                      </span>
                    </div>
                  </CardContent>
                </Card>

                {/* Hub/NVR */}
                {(selectedHub || selectedNVR) && (
                  <Card>
                    <CardHeader>
                      <CardTitle className="text-lg font-semibold">
                        {selectedProductLine?.includes('video') ? 'Network Video Recorder' : 'System Hub'}
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <div className="flex items-start space-x-4">
                        <img 
                          src={(selectedHub || selectedNVR)?.image_url} 
                          alt={(selectedHub || selectedNVR)?.name}
                          className="w-16 h-16 object-contain bg-gray-50 rounded p-2"
                          onError={(e) => e.target.style.display = 'none'}
                        />
                        <div className="flex-1">
                          <h4 className="font-medium text-gray-900">{(selectedHub || selectedNVR)?.name}</h4>
                          <p className="text-sm text-gray-600">{(selectedHub || selectedNVR)?.short_description}</p>
                          <div className="flex items-center space-x-2 mt-2">
                            <Button
                              size="sm"
                              variant="outline"
                              onClick={() => selectedProductLine?.includes('video') 
                                ? updateNVRQuantity(selectedNVR.id, -1)
                                : updateHubQuantity(selectedHub.id, -1)
                              }
                            >
                              <Minus className="h-4 w-4" />
                            </Button>
                            <span className="font-medium min-w-[2rem] text-center">
                              {selectedProductLine?.includes('video') 
                                ? (nvrQuantities[selectedNVR?.id] || 1)
                                : (hubQuantities[selectedHub?.id] || 1)
                              }
                            </span>
                            <Button
                              size="sm"
                              variant="outline"
                              onClick={() => selectedProductLine?.includes('video') 
                                ? updateNVRQuantity(selectedNVR.id, 1)
                                : updateHubQuantity(selectedHub.id, 1)
                              }
                            >
                              <Plus className="h-4 w-4" />
                            </Button>
                          </div>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                )}

                {/* Selected Components */}
                {selectedProducts.length > 0 && (
                  <Card>
                    <CardHeader>
                      <CardTitle className="text-lg font-semibold">Ausgewählte Komponenten</CardTitle>
                    </CardHeader>
                    <CardContent>
                      <div className="space-y-4">
                        {selectedProducts.map((product) => (
                          <div key={product.id} className="flex items-start space-x-4 p-3 bg-gray-50 rounded-lg">
                            <img 
                              src={product.image_url} 
                              alt={product.name}
                              className="w-12 h-12 object-contain bg-white rounded p-1"
                              onError={(e) => e.target.style.display = 'none'}
                            />
                            <div className="flex-1">
                              <h4 className="font-medium text-gray-900">{product.name}</h4>
                              <p className="text-sm text-gray-600">{product.short_description}</p>
                              <div className="flex flex-wrap gap-1 mt-1">
                                {product.usps.slice(0, 2).map((usp, idx) => (
                                  <Badge key={idx} variant="secondary" className="text-xs">
                                    {usp}
                                  </Badge>
                                ))}
                              </div>
                            </div>
                            <div className="text-right">
                              <div className="font-medium text-gray-900">× {productQuantities[product.id] || 1}</div>
                            </div>
                          </div>
                        ))}
                      </div>
                    </CardContent>
                  </Card>
                )}
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
                      Excel exportieren (Bald verfügbar)
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
                    <p>• Konfiguration prüfen und anpassen</p>
                    <p>• Kontaktieren Sie Xortec für ein Angebot</p>
                    <p>• Professionelle Installation durch zertifizierte Techniker</p>
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

export default ConfiguratorComplete;