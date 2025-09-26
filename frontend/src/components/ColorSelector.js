import React from 'react';
import { Button } from './ui/button';
import { Check } from 'lucide-react';

const ColorSelector = ({ selectedColor, onColorChange, availableColors = ['black', 'white'] }) => {
  const colorOptions = {
    black: { 
      name: 'Schwarz', 
      value: 'black', 
      bg: 'bg-gray-900', 
      border: 'border-gray-700',
      text: 'text-gray-900'
    },
    white: { 
      name: 'Weiß', 
      value: 'white', 
      bg: 'bg-white', 
      border: 'border-gray-300',
      text: 'text-white'
    }
  };

  if (availableColors.length <= 1) return null;

  return (
    <div className="flex items-center gap-2 mt-2">
      <span className="text-white text-sm font-medium">Farbe:</span>
      <div className="flex gap-2">
        {availableColors.map(color => {
          const option = colorOptions[color];
          const isSelected = selectedColor === color;
          
          return (
            <Button
              key={color}
              onClick={() => onColorChange(color)}
              variant="outline"
              size="sm"
              className={`relative w-8 h-8 p-0 rounded-full ${option.bg} ${option.border} ${
                isSelected ? 'ring-2 ring-orange-500 ring-offset-2 ring-offset-gray-800' : 'hover:scale-110'
              } transition-all`}
              title={option.name}
            >
              {isSelected && (
                <Check className={`w-4 h-4 ${color === 'white' ? 'text-gray-900' : 'text-white'}`} />
              )}
            </Button>
          );
        })}
      </div>
      <span className="text-gray-400 text-xs">
        {colorOptions[selectedColor]?.name}
      </span>
    </div>
  );
};

export default ColorSelector;