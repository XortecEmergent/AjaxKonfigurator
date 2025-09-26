// Excel Export Utility für Ajax Konfigurator

export const generateExcelData = (selectedProducts, productQuantities, products, selectedHub, configuration) => {
  // Filter selected products data
  const selectedProductsData = products.filter(p => selectedProducts.includes(p.id));
  
  // Prepare Excel data
  const excelData = selectedProductsData.map(product => {
    const quantity = productQuantities[product.id] || 1;
    return {
      'Pos.': selectedProductsData.indexOf(product) + 1,
      'Artikelnummer Xortec': product.specifications.xortec_nr || 'N/A',
      'Hersteller-Nr.': product.specifications.hersteller_nr || 'N/A',
      'Produktname': product.name,
      'Beschreibung': product.short_description || product.description,
      'Menge': quantity,
      'Kategorie': getCategoryName(product.category),
      'Produktlinie': getProductLineName(product.product_line),
      'Spezifikationen': formatSpecifications(product.specifications),
      'USPs': product.usps.join(', '),
      'Kompatibel mit Hub': product.compatible_hubs.includes(selectedHub?.name) ? 'Ja' : 'Nein'
    };
  });

  return excelData;
};

const getCategoryName = (categoryId) => {
  const categoryMap = {
    'hubs': 'Hub-Zentralen',
    'motion_detectors': 'Bewegungsmelder',
    'opening_detectors': 'Öffnungsmelder', 
    'glass_break_detectors': 'Glasbruchmelder',
    'fire_detectors': 'Brandmelder',
    'keypads': 'Bedienteile',
    'sirens': 'Sirenen',
    'buttons_keyfobs': 'Bedienelemente',
    'wired_cameras': 'IP-Kameras',
    'wifi_cameras': 'WLAN-Kameras',
    'range_extenders': 'Funk-Repeater'
  };
  return categoryMap[categoryId] || categoryId;
};

const getProductLineName = (productLine) => {
  const lineMap = {
    'baseline': 'Ajax Baseline',
    'superiorline': 'Ajax Superior',
    'en54': 'Ajax EN54',
    'video': 'Ajax Video'
  };
  return lineMap[productLine] || productLine;
};

const formatSpecifications = (specs) => {
  const specItems = [];
  if (specs.frequency) specItems.push(`Frequenz: ${specs.frequency}`);
  if (specs.range) specItems.push(`Reichweite: ${specs.range}`);
  if (specs.battery_life) specItems.push(`Batterie: ${specs.battery_life}`);
  if (specs.max_devices) specItems.push(`Max. Geräte: ${specs.max_devices}`);
  if (specs.operating_temp) specItems.push(`Betriebstemperatur: ${specs.operating_temp}`);
  return specItems.join(' | ');
};

export const downloadExcel = (selectedProducts, productQuantities, products, selectedHub, configuration) => {
  const excelData = generateExcelData(selectedProducts, productQuantities, products, selectedHub, configuration);
  
  // Create CSV content (simple Excel-compatible format)
  const csvHeaders = [
    'Pos.',
    'Artikelnummer Xortec', 
    'Hersteller-Nr.',
    'Produktname',
    'Beschreibung',
    'Menge',
    'Kategorie',
    'Produktlinie',
    'Spezifikationen',
    'USPs',
    'Kompatibel mit Hub'
  ];
  
  const csvContent = [
    // Header with configuration info
    [`Ajax System Konfiguration - ${configuration.name || 'Unbenannt'}`],
    [`Erstellt von: Xortec GmbH`],
    [`Datum: ${new Date().toLocaleDateString('de-DE')}`],
    [`Hub: ${selectedHub?.name || 'Nicht ausgewählt'}`],
    [`Beschreibung: ${configuration.description || 'Keine Beschreibung'}`],
    [],
    // Column headers
    csvHeaders,
    // Data rows
    ...excelData.map(row => csvHeaders.map(header => row[header] || ''))
  ];
  
  const csvString = csvContent
    .map(row => row.map(cell => `"${cell}"`).join(';'))
    .join('\n');
  
  // Add BOM for proper UTF-8 encoding in Excel
  const BOM = '\uFEFF';
  const blob = new Blob([BOM + csvString], { type: 'text/csv;charset=utf-8;' });
  
  // Download file
  const link = document.createElement('a');
  const url = URL.createObjectURL(blob);
  link.setAttribute('href', url);
  link.setAttribute('download', `Ajax_Konfiguration_${configuration.name || 'System'}_${new Date().toISOString().split('T')[0]}.csv`);
  link.style.visibility = 'hidden';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

export const generateQuotePDF = async (selectedProducts, productQuantities, products, selectedHub, configuration) => {
  // This would integrate with a PDF generation service
  // For now, we'll create a simple HTML-based PDF generation
  
  const selectedProductsData = products.filter(p => selectedProducts.includes(p.id));
  const totalDevices = Object.values(productQuantities).reduce((sum, qty) => sum + qty, 0);
  
  const htmlContent = `
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Ajax System Angebot - Xortec GmbH</title>
      <style>
        body { font-family: Arial, sans-serif; margin: 20px; color: #333; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #f97316; padding-bottom: 20px; margin-bottom: 30px; }
        .logo { font-size: 24px; font-weight: bold; color: #f97316; }
        .company-info { text-align: right; font-size: 12px; color: #666; }
        .title { color: #f97316; font-size: 28px; font-weight: bold; margin-bottom: 20px; }
        .system-info { background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
        .products-table { width: 100%; border-collapse: collapse; margin-bottom: 30px; }
        .products-table th, .products-table td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        .products-table th { background: #f97316; color: white; }
        .summary { background: #f8f9fa; padding: 20px; border-radius: 8px; }
        .footer { margin-top: 50px; font-size: 12px; color: #666; border-top: 1px solid #ddd; padding-top: 20px; }
      </style>
    </head>
    <body>
      <div class="header">
        <div class="logo">XORTEC GmbH</div>
        <div class="company-info">
          Ajax Systems Partner<br>
          Datum: ${new Date().toLocaleDateString('de-DE')}<br>
          Angebot-Nr: XRT-${Date.now().toString().slice(-6)}
        </div>
      </div>
      
      <h1 class="title">Ajax System Konfiguration</h1>
      
      <div class="system-info">
        <h3>System Übersicht</h3>
        <p><strong>Konfiguration:</strong> ${configuration.name || 'Ajax System'}</p>
        <p><strong>Beschreibung:</strong> ${configuration.description || 'Individuelle Ajax Sicherheitslösung'}</p>
        <p><strong>Hub-Zentrale:</strong> ${selectedHub?.name || 'Nicht ausgewählt'}</p>
        <p><strong>Anzahl Geräte:</strong> ${totalDevices}</p>
        <p><strong>Produktlinie:</strong> ${getProductLineName(selectedHub?.product_line || '')}</p>
      </div>
      
      <h3>Produktliste</h3>
      <table class="products-table">
        <thead>
          <tr>
            <th>Pos.</th>
            <th>Xortec Artikel-Nr.</th>
            <th>Produktname</th>
            <th>Beschreibung</th>
            <th>Menge</th>
            <th>Kategorie</th>
          </tr>
        </thead>
        <tbody>
          ${selectedProductsData.map((product, index) => `
            <tr>
              <td>${index + 1}</td>
              <td>${product.specifications.xortec_nr || 'N/A'}</td>
              <td>${product.name}</td>
              <td>${product.short_description || product.description}</td>
              <td>${productQuantities[product.id] || 1}</td>
              <td>${getCategoryName(product.category)}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
      
      <div class="summary">
        <h3>Zusammenfassung</h3>
        <p><strong>Gesamt Artikel:</strong> ${selectedProductsData.length}</p>
        <p><strong>Gesamt Menge:</strong> ${totalDevices} Stück</p>
        <p><strong>Hub-Kapazität:</strong> Ausreichend für gewählte Konfiguration</p>
      </div>
      
      <div class="footer">
        <p><strong>Xortec GmbH</strong> - Ihr Partner für Netzwerk- und Sicherheitstechnik</p>
        <p>Über 30 Jahre Erfahrung | Zertifizierter Ajax Partner | Deutschlandweiter Service</p>
        <p>Dieses Angebot wurde automatisch durch den Ajax Konfigurator erstellt.</p>
      </div>
    </body>
    </html>
  `;
  
  // Open print dialog for PDF generation
  const printWindow = window.open('', '_blank');
  printWindow.document.write(htmlContent);
  printWindow.document.close();
  
  // Auto-trigger print dialog after content loads
  printWindow.onload = () => {
    printWindow.print();
  };
};