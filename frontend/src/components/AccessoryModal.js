import React from 'react';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { X, Plus, Minus, AlertTriangle } from 'lucide-react';

const AccessoryModal = ({ 
  isOpen, 
  onClose, 
  accessories, 
  selectedAccessories, 
  onToggleAccessory, 
  onUpdateQuantity, 
  productId,
  productName 
}) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-gray-800 rounded-lg w-full max-w-4xl max-h-[80vh] overflow-y-auto">
        <div className="sticky top-0 bg-gray-800 border-b border-gray-700 p-6 flex items-center justify-between">
          <div>
            <h2 className="text-xl font-bold text-white">Zubehör für {productName}</h2>
            <p className="text-gray-400 text-sm">Wählen Sie passendes und notwendiges Zubehör</p>
          </div>
          <Button 
            onClick={onClose}
            variant="outline"
            size="sm"
            className="border-gray-600"
          >
            <X className="w-4 h-4" />
          </Button>
        </div>

        <div className="p-6">
          {accessories.length === 0 ? (
            <div className="text-center py-8">
              <p className="text-gray-400">Für dieses Produkt ist kein Zubehör verfügbar.</p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {accessories.map((accessory) => {
                const key = `${productId}_${accessory.id}`;
                const isSelected = !!selectedAccessories[key];
                const quantity = selectedAccessories[key]?.quantity || 0;
                
                return (
                  <Card 
                    key={accessory.id}
                    className={`${
                      isSelected 
                        ? 'ring-2 ring-orange-500 bg-orange-900/30' 
                        : 'bg-gray-900/50'
                    } border-gray-700 transition-all`}
                  >
                    <CardHeader className="pb-2">
                      <div className="flex items-start justify-between">
                        <div className="flex-1">
                          <CardTitle className="text-white text-base leading-tight flex items-center gap-2">
                            {accessory.name}
                            {accessory.required && (
                              <Badge variant="destructive" className="text-xs">
                                <AlertTriangle className="w-3 h-3 mr-1" />
                                Erforderlich
                              </Badge>
                            )}
                          </CardTitle>
                          {accessory.xortec_nr && (
                            <p className="text-xs text-orange-400 mt-1">
                              Xortec-Nr.: {accessory.xortec_nr}
                            </p>
                          )}
                        </div>
                      </div>
                    </CardHeader>
                    
                    <CardContent>
                      <CardDescription className="text-gray-300 text-sm mb-4">
                        {accessory.description || 'Hochwertiges Ajax Zubehör für optimale Systemintegration.'}
                      </CardDescription>

                      {/* Selection and Quantity Controls */}
                      <div className="space-y-3">
                        {!isSelected ? (
                          <Button 
                            onClick={() => onToggleAccessory(productId, accessory)}
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
                                  onClick={() => onUpdateQuantity(productId, accessory.id, quantity - 1)}
                                  size="sm"
                                  variant="outline"
                                  className="w-8 h-8 p-0 border-gray-600"
                                  disabled={quantity <= 1}
                                >
                                  <Minus className="w-3 h-3" />
                                </Button>
                                <span className="text-white min-w-[2rem] text-center">{quantity}</span>
                                <Button
                                  onClick={() => onUpdateQuantity(productId, accessory.id, quantity + 1)}
                                  size="sm"
                                  variant="outline"
                                  className="w-8 h-8 p-0 border-gray-600"
                                >
                                  <Plus className="w-3 h-3" />
                                </Button>
                              </div>
                            </div>
                            <Button 
                              onClick={() => onToggleAccessory(productId, accessory)}
                              variant="destructive"
                              size="sm"
                              className="w-full"
                            >
                              Entfernen
                            </Button>
                          </div>
                        )}

                        {accessory.required && !isSelected && (
                          <div className="bg-red-900/30 border border-red-500/50 rounded p-2">
                            <p className="text-red-300 text-xs flex items-center gap-2">
                              <AlertTriangle className="w-3 h-3" />
                              Dieses Zubehör ist für den ordnungsgemäßen Betrieb erforderlich.
                            </p>
                          </div>
                        )}
                      </div>
                    </CardContent>
                  </Card>
                );
              })}
            </div>
          )}

          {/* Summary */}
          <div className="mt-6 p-4 bg-gray-900/50 rounded-lg">
            <h3 className="text-white font-medium mb-2">Zubehör Zusammenfassung</h3>
            <div className="text-sm text-gray-300">
              {Object.keys(selectedAccessories).filter(key => key.startsWith(productId)).length > 0 ? (
                <ul className="space-y-1">
                  {Object.entries(selectedAccessories)
                    .filter(([key]) => key.startsWith(productId))
                    .map(([key, accessory]) => (
                      <li key={key} className="flex justify-between">
                        <span>{accessory.name}</span>
                        <span>{accessory.quantity}x</span>
                      </li>
                    ))
                  }
                </ul>
              ) : (
                <p>Kein Zubehör ausgewählt</p>
              )}
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex justify-end gap-3 mt-6">
            <Button 
              onClick={onClose}
              variant="outline"
              className="border-gray-600 text-white hover:bg-gray-700"
            >
              Schließen
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AccessoryModal;