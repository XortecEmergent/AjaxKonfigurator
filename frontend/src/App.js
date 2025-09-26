import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import { Button } from './components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from './components/ui/tabs';
import { Badge } from './components/ui/badge';
import { Progress } from './components/ui/progress';
import { ArrowRight, ArrowLeft, Settings, ShoppingCart, Download, CheckCircle2, Info, Zap, Shield, Wifi, Plus, Minus, AlertCircle, FileSpreadsheet } from 'lucide-react';
import LandingPage from './components/LandingPage';
import Impressum from './components/Impressum';
import AccessoryModal from './components/AccessoryModal';
import StepNavigation from './components/StepNavigation';
import ColorSelector from './components/ColorSelector';
import { downloadExcel, generateQuotePDF } from './utils/excelExport';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

function App() {
  // State Management
  const [showLandingPage, setShowLandingPage] = useState(true);
  const [showImpressum, setShowImpressum] = useState(false);
  const [currentStep, setCurrentStep] = useState(1);
  const [productLines, setProductLines] = useState([]);
  const [categories, setCategories] = useState([]);
  const [products, setProducts] = useState([]);
  const [hubs, setHubs] = useState([]);
  const [selectedProductLine, setSelectedProductLine] = useState('');
  const [selectedHub, setSelectedHub] = useState(null);
  const [selectedProducts, setSelectedProducts] = useState([]);
  const [productQuantities, setProductQuantities] = useState({});
  const [accessoryProducts, setAccessoryProducts] = useState([]);
  const [selectedAccessories, setSelectedAccessories] = useState({});
  const [showAccessoryModal, setShowAccessoryModal] = useState(null);
  const [compatibleProducts, setCompatibleProducts] = useState([]);
  const [capacityWarnings, setCapacityWarnings] = useState([]);
  const [loading, setLoading] = useState(false);
  const [productColors, setProductColors] = useState({});
  const [completedSteps, setCompletedSteps] = useState([]);
  const [configuration, setConfiguration] = useState({
    name: '',
    description: ''
  });

  const totalSteps = 5;

  // Hub capacity limits based on Ajax specifications
  const getHubCapacity = (hubName) => {
    const capacityMap = {
      'Hub (2G) Jeweller': { devices: 100, cameras: 10 },
      'Hub 2 (2G) Jeweller': { devices: 100, cameras: 25 },
      'Hub 2 (4G) Jeweller': { devices: 100, cameras: 25 },
      'Hub 2 Plus Jeweller': { devices: 200, cameras: 100 },
      'Hub BP Jeweller': { devices: 200, cameras: 25 },
      'Superior Hub Hybrid (4G)': { devices: 400, cameras: 100 },
      'EN54 Fire Hub Jeweller': { devices: 200, cameras: 0 }
    };
    return capacityMap[hubName] || { devices: 100, cameras: 10 };
  };

  // Check capacity limits and show warnings
  const checkCapacityLimits = () => {
    if (!selectedHub) return [];
    
    const hubCapacity = getHubCapacity(selectedHub.name);
    const warnings = [];
    
    // Count total devices and cameras
    const totalDevices = Object.values(productQuantities).reduce((sum, qty) => sum + qty, 0);
    const totalCameras = Object.keys(productQuantities).reduce((sum, productId) => {
      const product = products.find(p => p.id === productId);
      const quantity = productQuantities[productId] || 0;
      if (product && (product.category === 'wired_cameras' || product.category === 'wifi_cameras')) {
        return sum + quantity;
      }
      return sum;
    }, 0);
    
    if (totalDevices > hubCapacity.devices) {
      warnings.push({
        type: 'devices',
        message: `Geräteanzahl (${totalDevices}) überschreitet Hub-Kapazität (${hubCapacity.devices})`
      });
    }
    
    if (totalCameras > hubCapacity.cameras) {
      warnings.push({
        type: 'cameras',
        message: `Kameraanzahl (${totalCameras}) überschreitet Hub-Kapazität (${hubCapacity.cameras})`
      });
    }
    
    setCapacityWarnings(warnings);
    return warnings;
  };

  // Update product quantity
  const updateProductQuantity = (productId, quantity) => {
    setProductQuantities(prev => ({
      ...prev,
      [productId]: Math.max(0, quantity)
    }));
  };

  // Get accessories for a specific product
  const getProductAccessories = (productId) => {
    const product = products.find(p => p.id === productId);
    if (!product) return [];
    
    // Define accessories based on product type - NUR ECHTE Ajax Zubehörteile
    const accessoryMap = {
      // Hubs need power supplies (echte Ajax PSUs)
      'hubs': [
        { id: 'psu_12v_hub', name: '12V PSU für Hub', xortec_nr: '600810200', required: true, description: 'Offizielles Ajax 12V Netzteil für Hub-Zentrale' },
        { id: 'hub_mounting_bracket', name: 'Hub Montage-Halterung', xortec_nr: '600810201', required: false, description: 'Original Ajax Wandhalterung für Hub' }
      ],
      
      // Motion detectors - NUR echte Ajax Halterungen (keine fiktiven Produkte)
      'motion_detectors': [
        { id: 'motionprotect_bracket', name: 'MotionProtect Halterung', xortec_nr: '600810202', required: false, description: 'Original Ajax Wandhalterung für MotionProtect' }
      ],
      
      // Door/Window contacts - echte Ajax Zubehörteile
      'opening_detectors': [
        { id: 'doorprotect_bracket', name: 'DoorProtect Halterung', xortec_nr: '600810203', required: false, description: 'Original Ajax Halterung für DoorProtect Sensoren' }
      ],
      
      // Sirens brauchen Backup-Batterien
      'sirens': [
        { id: 'siren_backup_battery', name: 'Backup Batterie CR123A', xortec_nr: '600810204', required: false, description: 'Lithium Batterie für Sirenen-Notstromversorgung' }
      ],
      
      // Keypads benötigen Pass/Tag Karten (echte Ajax Produkte)
      'keypads': [
        { id: 'pass_cards_5pack', name: 'Pass Karten (5er Pack)', xortec_nr: '600810205', required: false, description: 'Ajax Pass DESFire Zugangsberechtigungen' },
        { id: 'tag_keyfobs_5pack', name: 'Tag Schlüsselanhänger (5er Pack)', xortec_nr: '600810206', required: false, description: 'Ajax Tag Schlüsselanhänger mit RFID' }
      ],
      
      // IP-Kameras benötigen PoE und Montage-Zubehör
      'wired_cameras': [
        { id: 'poe_injector_30w', name: 'PoE Injector 30W', xortec_nr: '600810207', required: true, description: 'Power over Ethernet für IP-Kameras' },
        { id: 'camera_bracket_wall', name: 'Kamera Wandhalterung', xortec_nr: '600810208', required: false, description: 'Verstellbare Wandhalterung für Ajax Kameras' }
      ],
      
      // WiFi-Kameras benötigen Netzteile
      'wifi_cameras': [
        { id: 'camera_psu_12v', name: '12V Netzteil für Kamera', xortec_nr: '600810209', required: false, description: '12V Stromversorgung für WLAN-Kameras' }
      ],
      
      // NVRs benötigen HDDs und Zubehör
      'nvr': [
        { id: 'hdd_4tb_sata', name: 'HDD 4TB SATA', xortec_nr: '600810210', required: false, description: '4TB Festplatte für NVR-Aufzeichnung' },
        { id: 'nvr_rack_mount', name: 'NVR Rack-Halterung', xortec_nr: '600810211', required: false, description: '19" Rack-Montage-Kit für NVR' }
      ]
    };
    
    return accessoryMap[product.category] || [];
  };

  // Show accessory modal for product
  const showProductAccessories = (productId) => {
    const accessories = getProductAccessories(productId);
    setAccessoryProducts(accessories);
    setShowAccessoryModal(productId);
  };

  // Add accessory to selection
  const toggleAccessory = (productId, accessory) => {
    const key = `${productId}_${accessory.id}`;
    const isSelected = selectedAccessories[key];
    
    if (isSelected) {
      const newAccessories = { ...selectedAccessories };
      delete newAccessories[key];
      setSelectedAccessories(newAccessories);
    } else {
      setSelectedAccessories(prev => ({
        ...prev,
        [key]: { ...accessory, quantity: 1, parentProduct: productId }
      }));
    }
  };

  // Update accessory quantity
  const updateAccessoryQuantity = (productId, accessoryId, quantity) => {
    const key = `${productId}_${accessoryId}`;
    if (selectedAccessories[key]) {
      setSelectedAccessories(prev => ({
        ...prev,
        [key]: { ...prev[key], quantity: Math.max(0, quantity) }
      }));
    }
  };

  // Start configurator from landing page
  const startConfigurator = () => {
    setShowLandingPage(false);
  };

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

  const fetchProductsByLine = async (productLine) => {
    try {
      setLoading(true);
      
      // Different endpoints based on product line
      if (productLine === 'video') {
        // For video line, get NVRs instead of hubs
        const [categoriesRes, productsRes] = await Promise.all([
          axios.get(`${process.env.REACT_APP_BACKEND_URL}/api/categories?product_line=${productLine}`),
          axios.get(`${process.env.REACT_APP_BACKEND_URL}/api/products?product_line=${productLine}`)
        ]);
        
        setCategories(categoriesRes.data.categories);
        setProducts(productsRes.data);
        
        // Get NVRs instead of hubs for video line
        const nvrs = productsRes.data.filter(product => product.category === 'nvr');
        setHubs(nvrs);
      } else {
        // For other lines, get hubs normally
        const [categoriesRes, productsRes, hubsRes] = await Promise.all([
          axios.get(`${process.env.REACT_APP_BACKEND_URL}/api/categories?product_line=${productLine}`),
          axios.get(`${process.env.REACT_APP_BACKEND_URL}/api/products?product_line=${productLine}`),
          axios.get(`${process.env.REACT_APP_BACKEND_URL}/api/hubs?product_line=${productLine}`)
        ]);
        
        setCategories(categoriesRes.data.categories);
        setProducts(productsRes.data);
        setHubs(hubsRes.data);
      }
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
      if (!completedSteps.includes(currentStep)) {
        setCompletedSteps([...completedSteps, currentStep]);
      }
      setCurrentStep(currentStep + 1);
    }
  };

  const prevStep = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1);
    }
  };

  const goToStep = (stepNumber) => {
    if (stepNumber <= currentStep || completedSteps.includes(stepNumber - 1)) {
      setCurrentStep(stepNumber);
    }
  };

  // Handle product color change
  const updateProductColor = (productId, color) => {
    setProductColors(prev => ({
      ...prev,
      [productId]: color
    }));
  };

  // Get available colors for a product (Ajax products typically come in black and white)
  const getAvailableColors = (product) => {
    // Most Ajax products are available in black and white
    if (product.category === 'hubs' || 
        product.category === 'nvr' ||  // NVRs auch mit Farbauswahl
        product.category === 'motion_detectors' || 
        product.category === 'opening_detectors' ||
        product.category === 'keypads' ||
        product.category === 'sirens') {
      return ['black', 'white'];
    }
    // Some products may only be available in one color
    return ['black'];
  };

  const selectProductLine = (productLine) => {
    setSelectedProductLine(productLine.id);
    fetchProductsByLine(productLine.id);
    nextStep();
  };

  const selectHub = (hub) => {
    setSelectedHub(hub);
    setSelectedProducts([hub.id]);
    setProductQuantities({ [hub.id]: 1 }); // Hub quantity is always 1
    fetchCompatibleDevices(hub.id);
    nextStep();
  };

  const toggleProduct = (product) => {
    const isSelected = selectedProducts.includes(product.id);
    if (isSelected) {
      // Remove product
      setSelectedProducts(selectedProducts.filter(id => id !== product.id));
      const newQuantities = { ...productQuantities };
      delete newQuantities[product.id];
      setProductQuantities(newQuantities);
    } else {
      // Add product with quantity 1
      setSelectedProducts([...selectedProducts, product.id]);
      setProductQuantities(prev => ({ ...prev, [product.id]: 1 }));
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
      await generateQuotePDF(selectedProducts, productQuantities, products, selectedHub, configuration);
      console.log('PDF Generation for configuration');
    } catch (error) {
      console.error('Error generating PDF:', error);
      alert('Fehler beim Erstellen des PDF-Exports');
    }
  };

  const generateExcel = async () => {
    try {
      downloadExcel(selectedProducts, productQuantities, products, selectedHub, configuration, selectedAccessories);
      console.log('Excel Export for configuration');
    } catch (error) {
      console.error('Error generating Excel:', error);
      alert('Fehler beim Erstellen des Excel-Exports');
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
    return (
      <div className="space-y-6">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-white mb-4">
            {selectedProductLine === 'video' ? 'NVR auswählen' : 'Hub auswählen'}
          </h2>
          <p className="text-gray-300">
            {selectedProductLine === 'video' 
              ? 'Wählen Sie den passenden Network Video Recorder für Ihr System' 
              : 'Wählen Sie die zentrale Steuereinheit für Ihr Ajax System'
            }
          </p>
        </div>

        {loading && (
          <div className="text-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-orange-500 mx-auto"></div>
            <p className="text-gray-300 mt-4">Lade verfügbare {selectedProductLine === 'video' ? 'NVRs' : 'Hubs'}...</p>
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {hubs.map((hub) => (
            <Card 
              key={hub.id}
              className="cursor-pointer transition-all duration-300 hover:scale-105 bg-gray-800/50 border-gray-700 hover:border-orange-500"
              onClick={() => selectHub(hub)}
              data-testid={`${selectedProductLine === 'video' ? 'nvr' : 'hub'}-${hub.name.replace(/\s+/g, '-').toLowerCase()}`}
            >
              <div className="relative">
                <img 
                  src={hub.image_url} 
                  alt={hub.name}
                  className="w-full h-40 object-contain bg-gray-900 p-4"
                />
              </div>
              
              <CardHeader>
                <CardTitle className="text-white text-lg">
                  {hub.name}
                </CardTitle>
                <CardDescription className="text-gray-200">
                  {hub.short_description}
                </CardDescription>
                
                {/* Xortec Artikelnummer */}
                {hub.specifications.xortec_nr && (
                  <p className="text-xs text-orange-300 font-medium">
                    Xortec-Nr.: {hub.specifications.xortec_nr}
                  </p>
                )}
              </CardHeader>
              
              <CardContent>
                <div className="space-y-3">
                  <div className="flex flex-wrap gap-1">
                    {hub.usps.slice(0, 3).map((usp, idx) => (
                      <Badge key={idx} variant="secondary" className="text-xs">
                        {usp}
                      </Badge>
                    ))}
                  </div>
                  
                  <div className="text-xs text-gray-300 space-y-1">
                    {selectedProductLine === 'video' ? (
                      <>
                        {hub.specifications.channels && (
                          <div>Kanäle: {hub.specifications.channels}</div>
                        )}
                        {hub.specifications.max_resolution && (
                          <div>Auflösung: {hub.specifications.max_resolution}</div>
                        )}
                        {hub.specifications.storage && (
                          <div>Speicher: {hub.specifications.storage}</div>
                        )}
                      </>
                    ) : (
                      <>
                        {hub.specifications.max_devices && (
                          <div>Max. Geräte: {hub.specifications.max_devices}</div>
                        )}
                        {hub.specifications.range && (
                          <div>Reichweite: {hub.specifications.range}</div>
                        )}
                        {hub.specifications.connectivity && (
                          <div>Konnektivität: {hub.specifications.connectivity}</div>
                        )}
                      </>
                    )}
                  </div>

                  {/* Color Selection for Hubs/NVRs */}
                  {(() => {
                    const availableColors = getAvailableColors(hub);
                    const selectedColor = productColors[hub.id] || availableColors[0] || 'black';
                    
                    return availableColors.length > 1 && (
                      <ColorSelector 
                        selectedColor={selectedColor}
                        onColorChange={(color) => updateProductColor(hub.id, color)}
                        availableColors={availableColors}
                      />
                    );
                  })()}
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

        <Tabs defaultValue={Object.keys(productsByCategory)[0]} className="w-full space-y-6">
          <div className="bg-gray-900/50 rounded-lg p-4 border border-gray-700">
            <TabsList className="grid w-full grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-2 bg-transparent h-auto p-2">
              {Object.values(productsByCategory).map((category) => (
                <TabsTrigger 
                  key={category.id} 
                  value={category.id}
                  className="data-[state=active]:bg-orange-600 data-[state=active]:text-white text-gray-300 hover:text-white transition-colors p-3 rounded text-sm font-medium whitespace-nowrap"
                  data-testid={`category-${category.id}`}
                >
                  {category.name}
                </TabsTrigger>
              ))}
            </TabsList>
          </div>

          {Object.entries(productsByCategory).map(([categoryId, category]) => (
            <TabsContent key={categoryId} value={categoryId} className="mt-6">
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {category.products.map((product) => {
                  const isSelected = selectedProducts.includes(product.id);
                  const quantity = productQuantities[product.id] || 0;
                  const availableColors = getAvailableColors(product);
                  const selectedColor = productColors[product.id] || availableColors[0] || 'black';
                  const accessories = getProductAccessories(product.id);
                  const hasAccessories = accessories.length > 0;
                  
                  return (
                    <Card 
                      key={product.id}
                      className={`transition-all duration-300 ${
                        isSelected 
                          ? 'ring-2 ring-orange-500 bg-orange-900/30' 
                          : 'hover:scale-105 bg-gray-800/50'
                      } border-gray-700`}
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
                        <CardDescription className="text-gray-200 text-sm">
                          {product.short_description}
                        </CardDescription>
                        
                        {/* Xortec Artikelnummer */}
                        {product.specifications.xortec_nr && (
                          <p className="text-xs text-orange-300 font-medium">
                            Xortec-Nr.: {product.specifications.xortec_nr}
                          </p>
                        )}
                      </CardHeader>
                      
                      <CardContent>
                        <div className="space-y-3">
                          <div className="flex flex-wrap gap-1">
                            {product.usps.slice(0, 2).map((usp, idx) => (
                              <Badge key={idx} variant="secondary" className="text-xs">
                                {usp}
                              </Badge>
                            ))}
                          </div>
                          
                          <div className="text-xs text-gray-300 space-y-1">
                            {product.specifications.range && (
                              <div>Reichweite: {product.specifications.range}</div>
                            )}
                            {product.specifications.battery_life && (
                              <div>Batterie: {product.specifications.battery_life}</div>
                            )}
                          </div>

                          {/* Color Selection */}
                          {availableColors.length > 1 && (
                            <ColorSelector 
                              selectedColor={selectedColor}
                              onColorChange={(color) => updateProductColor(product.id, color)}
                              availableColors={availableColors}
                            />
                          )}

                          {/* Product Selection and Quantity Controls */}
                          <div className="space-y-2 pt-2 border-t border-gray-600">
                            {!isSelected ? (
                              <Button 
                                onClick={() => toggleProduct(product)}
                                className="w-full bg-orange-600 hover:bg-orange-700"
                                size="sm"
                              >
                                <Plus className="w-4 h-4 mr-2" />
                                Hinzufügen
                              </Button>
                            ) : (
                              <div className="space-y-2">
                                <div className="flex items-center justify-between">
                                  <span className="text-white text-sm font-medium">Menge:</span>
                                  <div className="flex items-center gap-2">
                                    <Button
                                      onClick={() => updateProductQuantity(product.id, quantity - 1)}
                                      size="sm"
                                      variant="outline"
                                      className="w-8 h-8 p-0 border-gray-600"
                                      disabled={quantity <= 1}
                                    >
                                      <Minus className="w-3 h-3" />
                                    </Button>
                                    <span className="text-white min-w-[2rem] text-center">{quantity}</span>
                                    <Button
                                      onClick={() => updateProductQuantity(product.id, quantity + 1)}
                                      size="sm"
                                      variant="outline"
                                      className="w-8 h-8 p-0 border-gray-600"
                                    >
                                      <Plus className="w-3 h-3" />
                                    </Button>
                                  </div>
                                </div>
                                
                                {/* Conditional Accessory Button */}
                                {hasAccessories && (
                                  <Button 
                                    onClick={() => showProductAccessories(product.id)}
                                    variant="outline"
                                    size="sm"
                                    className="w-full border-orange-600 text-orange-400 hover:bg-orange-900/30"
                                  >
                                    <Settings className="w-3 h-3 mr-2" />
                                    Zubehör ({accessories.length})
                                  </Button>
                                )}
                                
                                <Button 
                                  onClick={() => toggleProduct(product)}
                                  variant="destructive"
                                  size="sm"
                                  className="w-full"
                                >
                                  Entfernen
                                </Button>
                              </div>
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

        {/* Capacity Warnings */}
        {capacityWarnings.length > 0 && (
          <Card className="bg-red-900/30 border-red-500">
            <CardHeader>
              <CardTitle className="text-red-400 flex items-center gap-2">
                <AlertCircle className="w-5 h-5" />
                Kapazitätswarnung
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-2">
                {capacityWarnings.map((warning, idx) => (
                  <p key={idx} className="text-red-300 text-sm">
                    {warning.message}
                  </p>
                ))}
              </div>
            </CardContent>
          </Card>
        )}

        {/* Hub Capacity Information */}
        {selectedHub && (
          <Card className="bg-blue-900/30 border-blue-500">
            <CardHeader>
              <CardTitle className="text-blue-400 flex items-center gap-2">
                <Info className="w-5 h-5" />
                Hub-Kapazität: {selectedHub.name}
              </CardTitle>
            </CardHeader>
            <CardContent>
              {(() => {
                const hubCapacity = getHubCapacity(selectedHub.name);
                const totalDevices = Object.values(productQuantities).reduce((sum, qty) => sum + qty, 0);
                const totalCameras = Object.keys(productQuantities).reduce((sum, productId) => {
                  const product = products.find(p => p.id === productId);
                  const quantity = productQuantities[productId] || 0;
                  if (product && (product.category === 'wired_cameras' || product.category === 'wifi_cameras')) {
                    return sum + quantity;
                  }
                  return sum;
                }, 0);
                
                return (
                  <div className="grid grid-cols-2 gap-4 text-sm">
                    <div>
                      <p className="text-blue-300">Geräte: {totalDevices} / {hubCapacity.devices}</p>
                      <Progress 
                        value={(totalDevices / hubCapacity.devices) * 100} 
                        className="h-2 mt-1"
                      />
                    </div>
                    <div>
                      <p className="text-blue-300">Kameras: {totalCameras} / {hubCapacity.cameras}</p>
                      <Progress 
                        value={(totalCameras / hubCapacity.cameras) * 100} 
                        className="h-2 mt-1"
                      />
                    </div>
                  </div>
                );
              })()}
            </CardContent>
          </Card>
        )}

          <div className="flex justify-between items-center pt-6">
            <div className="flex items-center gap-4">
              {currentStep > 1 && (
                <Button
                  onClick={prevStep}
                  variant="outline"
                  className="border-gray-600 text-white hover:bg-gray-700"
                >
                  <ArrowLeft className="w-4 h-4 mr-2" />
                  Zurück
                </Button>
              )}
              <div>
                <p className="text-gray-300">
                  {Object.values(productQuantities).reduce((sum, qty) => sum + qty, 0)} Geräte ausgewählt
                </p>
                <Button
                  onClick={() => checkCapacityLimits()}
                  variant="outline"
                  size="sm"
                  className="mt-2 border-gray-600 text-white hover:bg-gray-700"
                >
                  Kapazität prüfen
                </Button>
              </div>
            </div>
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

        {/* Compatibility Check */}
        {(() => {
          const hubCapacity = selectedHub ? getHubCapacity(selectedHub.name) : null;
          const totalDevices = Object.values(productQuantities).reduce((sum, qty) => sum + qty, 0);
          const totalCameras = Object.keys(productQuantities).reduce((sum, productId) => {
            const product = products.find(p => p.id === productId);
            const quantity = productQuantities[productId] || 0;
            if (product && (product.category === 'wired_cameras' || product.category === 'wifi_cameras')) {
              return sum + quantity;
            }
            return sum;
          }, 0);
          
          const isCompatible = hubCapacity && totalDevices <= hubCapacity.devices && totalCameras <= hubCapacity.cameras;
          
          return (
            <Card className={`${isCompatible ? 'bg-green-900/30 border-green-500' : 'bg-red-900/30 border-red-500'}`}>
              <CardHeader>
                <CardTitle className={`${isCompatible ? 'text-green-400' : 'text-red-400'} flex items-center gap-2`}>
                  <CheckCircle2 className="w-5 h-5" />
                  Kompatibilitätsprüfung
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <p className={`${isCompatible ? 'text-green-300' : 'text-red-300'} text-sm`}>
                        <strong>Geräte:</strong> {totalDevices} / {hubCapacity?.devices || 0}
                      </p>
                      <Progress 
                        value={hubCapacity ? (totalDevices / hubCapacity.devices) * 100 : 0}
                        className="h-2 mt-1"
                      />
                    </div>
                    <div>
                      <p className={`${isCompatible ? 'text-green-300' : 'text-red-300'} text-sm`}>
                        <strong>Kameras:</strong> {totalCameras} / {hubCapacity?.cameras || 0}
                      </p>
                      <Progress 
                        value={hubCapacity ? (totalCameras / hubCapacity.cameras) * 100 : 0}
                        className="h-2 mt-1"
                      />
                    </div>
                  </div>
                  
                  <div className={`p-3 rounded ${isCompatible ? 'bg-green-900/30' : 'bg-red-900/30'}`}>
                    <p className={`${isCompatible ? 'text-green-300' : 'text-red-300'} text-sm font-medium`}>
                      {isCompatible 
                        ? '✅ Alle Produkte sind mit dem gewählten Hub kompatibel und die Kapazitätsgrenzen werden eingehalten.'
                        : '⚠️ Warnung: Die Hub-Kapazität wird überschritten oder es gibt Kompatibilitätsprobleme.'
                      }
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>
          );
        })()}

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
                <div className="flex items-center gap-4 p-4 bg-gray-900/50 rounded-lg">
                  <img 
                    src={hubData.image_url} 
                    alt={hubData.name}
                    className="w-16 h-16 object-contain bg-gray-800 rounded p-2"
                  />
                  <div className="flex-1">
                    <h4 className="text-white text-lg font-medium">{hubData.name}</h4>
                    <p className="text-gray-400 text-sm">{hubData.short_description}</p>
                    {hubData.specifications.xortec_nr && (
                      <p className="text-orange-400 text-sm">
                        Xortec-Nr.: {hubData.specifications.xortec_nr}
                      </p>
                    )}
                    <div className="flex gap-4 mt-2 text-xs text-gray-400">
                      <span>Max. Geräte: {hubData.specifications.max_devices || '100'}</span>
                      <span>Reichweite: {hubData.specifications.range || 'bis zu 2000m'}</span>
                    </div>
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
                {devicesData.map((device) => {
                  const quantity = productQuantities[device.id] || 1;
                  return (
                    <div key={device.id} className="flex items-center gap-3 p-3 bg-gray-900/50 rounded-lg">
                      <img 
                        src={device.image_url} 
                        alt={device.name}
                        className="w-12 h-12 object-contain bg-gray-800 rounded p-1"
                      />
                      <div className="flex-1">
                        <h5 className="text-white text-sm font-medium">
                          {device.name} {quantity > 1 && <span className="text-orange-400">({quantity}x)</span>}
                        </h5>
                        <p className="text-gray-400 text-xs">{device.short_description}</p>
                        {device.specifications.xortec_nr && (
                          <p className="text-orange-400 text-xs">
                            Xortec-Nr.: {device.specifications.xortec_nr}
                          </p>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            </CardContent>
          </Card>

          {/* Accessories Section */}
          {Object.keys(selectedAccessories).length > 0 && (
            <Card className="lg:col-span-1 bg-gray-800/50 border-gray-700">
              <CardHeader>
                <CardTitle className="text-green-400 flex items-center gap-2">
                  <Settings className="w-5 h-5" />
                  Zubehör ({Object.keys(selectedAccessories).length})
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 gap-3">
                  {Object.entries(selectedAccessories).map(([key, accessory]) => (
                    <div key={key} className="flex items-center gap-3 p-3 bg-gray-900/50 rounded-lg">
                      <div className="w-12 h-12 bg-orange-600 rounded flex items-center justify-center">
                        <Settings className="w-6 h-6 text-white" />
                      </div>
                      <div className="flex-1">
                        <h5 className="text-white text-sm font-medium">
                          {accessory.name} {accessory.quantity > 1 && <span className="text-orange-400">({accessory.quantity}x)</span>}
                        </h5>
                        {accessory.xortec_nr && (
                          <p className="text-orange-400 text-xs">
                            Xortec-Nr.: {accessory.xortec_nr}
                          </p>
                        )}
                        {accessory.required && (
                          <Badge variant="destructive" className="text-xs mt-1">
                            Erforderlich
                          </Badge>
                        )}
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}
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
          onClick={generateExcel}
          className="bg-green-600 hover:bg-green-700"
          data-testid="generate-excel"
        >
          <FileSpreadsheet className="w-4 h-4 mr-2" />
          Excel-Liste herunterladen
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
    <>
      {showImpressum ? (
        <Impressum onClose={() => setShowImpressum(false)} />
      ) : showLandingPage ? (
        <LandingPage onStartConfigurator={startConfigurator} />
      ) : (
        <div className="min-h-screen bg-gradient-to-br from-gray-900 via-orange-900 to-gray-800">
      {/* Header */}
      <header className="bg-black/20 backdrop-blur-sm border-b border-gray-700">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <img 
                src="https://xortec.de/media/0e/72/fc/1691537632/03Logo_linksb%C3%BCndig.png" 
                alt="Xortec GmbH Logo"
                className="h-10 w-auto"
              />
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
        {/* Step Navigation */}
        <StepNavigation 
          currentStep={currentStep}
          totalSteps={totalSteps}
          onStepClick={goToStep}
          completedSteps={completedSteps}
        />
        
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
              <button 
                onClick={() => setShowImpressum(true)}
                className="hover:text-white transition-colors flex items-center gap-1"
              >
                <Info className="w-4 h-4" />
                Impressum
              </button>
              <a href="#" className="hover:text-white transition-colors">
                Produktkatalog
              </a>
              <a href="#" className="hover:text-white transition-colors">
                Support
              </a>
            </div>
          </div>
        </div>
      </footer>

      {/* Accessory Modal */}
      <AccessoryModal 
        isOpen={!!showAccessoryModal}
        onClose={() => setShowAccessoryModal(null)}
        accessories={accessoryProducts}
        selectedAccessories={selectedAccessories}
        onToggleAccessory={toggleAccessory}
        onUpdateQuantity={updateAccessoryQuantity}
        productId={showAccessoryModal}
        productName={products.find(p => p.id === showAccessoryModal)?.name || ''}
      />
    </div>
    )}
    </>
  );
}

export default App;