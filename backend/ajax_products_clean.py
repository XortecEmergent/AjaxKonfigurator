"""
Neue Ajax Produkt-Datenbank basierend auf aktuellen ajax.systems Daten (2025)
Alle Produktlinien: Superior, Baseline, Video, Fire & Life Safety, Comfort & Automation
"""

def get_new_ajax_products():
    return [
        # ================== HUBS - BASELINE ==================
        {
            "name": "Hub 2 Plus Jeweller",
            "category": "hubs",
            "product_line": "baseline",
            "description": "Kabellose Alarmzentrale mit Unterstützung für Foto-Verifikation. Verbindung über Wi-Fi, Ethernet und zwei SIM-Karten (2G/3G/LTE)",
            "short_description": "Kabellose Alarmzentrale mit Foto-Verifikation",
            "usps": ["Foto-Verifikation", "4 Kommunikationswege", "200 Geräte", "Grade 2"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078",
            "specifications": {
                "frequency": "868 MHz (Jeweller), 433 MHz (Wings)",
                "range": "bis zu 2000m",
                "communication": ["Wi-Fi", "Ethernet", "2G/3G/LTE (2x SIM)"],
                "max_devices": 200,
                "operating_temp": "0°C bis +50°C",
                "xortec_nr": "600810057/600810058",
                "hersteller_nr": "25338.52.BL1/25338.52.WH1"
            },
            "features": [
                {"name": "Foto-Verifikation", "description": "Visuelle Alarmbestätigung über Wings-Protokoll"},
                {"name": "Redundante Kommunikation", "description": "4 unabhängige Kommunikationswege"},
                {"name": "Große Kapazität", "description": "Bis zu 200 Ajax-Geräte verwaltbar"}
            ],
            "accessories": ["PSU (12V/1.5A)", "Backup-Batterie", "Externe Antenne"]
        },
        {
            "name": "Hub BP Jeweller",
            "category": "hubs",
            "product_line": "baseline",
            "description": "Kabellose batteriebetriebene Alarmzentrale. Unterstützt Foto-Verifikation. Verbindung über zwei SIM-Karten (2G/3G/LTE)",
            "short_description": "Batteriebetriebene Alarmzentrale",
            "usps": ["Batteriebetrieben", "Mobil einsetzbar", "Foto-Verifikation", "200 Geräte"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_bp_jeweller_black_1760739e4c%402.png&1732115997",
            "specifications": {
                "frequency": "868 MHz (Jeweller), 433 MHz (Wings)",
                "range": "bis zu 2000m",
                "communication": ["2G/3G/LTE (2x SIM)"],
                "max_devices": 200,
                "battery_life": "bis zu 16 Stunden",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP65",
                "xortec_nr": "600810735/600810736",
                "hersteller_nr": "25338.55.BL1/25338.55.WH1"
            },
            "features": [
                {"name": "Batteriebetrieb", "description": "Unabhängig von Stromnetz, ideal für mobile Einsätze"},
                {"name": "Robust", "description": "IP65 Schutzklasse für raue Umgebungen"},
                {"name": "Foto-Verifikation", "description": "Visuelle Alarmbestätigung"}
            ],
            "accessories": ["Internal Battery NB (7.2V/95Ah)", "Internal Battery RB (6.4V/36Ah)", "External Antenna"]
        },

        # ================== BASELINE BEWEGUNGSMELDER ==================
        {
            "name": "MotionProtect Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "Kabelloser IR-Bewegungsmelder für zuverlässige Erkennung von Eindringlingen",
            "short_description": "Standard PIR-Bewegungsmelder",
            "usps": ["12m Erfassung", "Grade 2", "7 Jahre Batterie", "Haustierimmun"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_7e25a60ef8%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "ip_rating": "IP50",
                "xortec_nr": "600810025/600810026",
                "hersteller_nr": "8010.52.BL1/8010.52.WH1"
            },
            "features": [
                {"name": "Haustierimmunität", "description": "Ignoriert Tiere bis 20kg und 50cm Höhe"},
                {"name": "Temperaturkompensation", "description": "Stabile Erkennung bei verschiedenen Temperaturen"},
                {"name": "Anti-Sabotage", "description": "Schutz gegen Manipulation"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MotionCam Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "Kabelloser IR-Bewegungsmelder mit Foto-bei-Alarm-Funktion",
            "short_description": "PIR-Bewegungsmelder mit Kamera",
            "usps": ["Foto-Verifikation", "Grade 2", "Anti-Sabotage", "Haustierimmun"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotion_cam_jeweller_black_50c00ca247%402.png&1727442738",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 4 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810029/600810030",
                "hersteller_nr": "8020.52.BL1/8020.52.WH1"
            },
            "features": [
                {"name": "Foto-Verifikation", "description": "Macht Fotos bei Alarmen zur visuellen Bestätigung"},
                {"name": "Haustierimmunität", "description": "Ignoriert Haustiere bis 20kg"},
                {"name": "Nachtsicht", "description": "IR-Beleuchtung für Aufnahmen bei Dunkelheit"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        }
    ]

if __name__ == "__main__":
    products = get_new_ajax_products()
    print(f"Anzahl Produkte: {len(products)}")
    
    # Kategorien zählen
    categories = {}
    for product in products:
        cat = product['category']
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += 1
    
    print("\nKategorien:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")
    
    # Produktlinien zählen
    lines = {}
    for product in products:
        line = product['product_line']
        if line not in lines:
            lines[line] = 0
        lines[line] += 1
        
    print("\nProduktlinien:")
    for line, count in sorted(lines.items()):
        print(f"  {line}: {count}")