"""
Ajax Systems Produkt-Datenbank 2025 - ERWEITERT & VOLLSTÄNDIG
Basierend auf ajax.systems offizielle Daten (Stand: Dezember 2025)
Mit Farboptionen und allen Baseline/Superior Komponenten

Erstellt von: Xortec GmbH
Letzte Aktualisierung: Dezember 2025
"""

def get_ajax_products_complete():
    return [
        # ========================================================================
        # INTRUSION BASELINE - HUBS
        # ========================================================================
        {
            "name": "Hub 2 Plus Jeweller",
            "category": "hubs",
            "product_line": "intrusion_baseline",
            "description": "Advanced control panel with alarm photo verification support and 4 communication channels. Manages up to 200 devices with LTE support",
            "short_description": "Alarmzentrale mit Foto-Verifikation und 4 Kommunikationswegen",
            "usps": ["Foto-Verifikation", "4 Kommunikationswege", "Bis zu 200 Geräte", "LTE Support"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller), 433 MHz (Wings)",
                "range": "bis zu 2000m (Jeweller)",
                "communication": ["Wi-Fi", "Ethernet", "2G/3G/LTE (2x SIM)"],
                "max_devices": 200,
                "max_cameras": 100,
                "operating_temp": "0°C bis +50°C",
                "battery_life": "bis zu 15 Stunden",
                "xortec_nr": "600810057/600810058",
                "hersteller_nr": "25338.52.BL1/25338.52.WH1"
            },
            "features": [
                {"name": "Foto-Verifikation in 9 Sekunden", "description": "Visuelle Alarmbestätigung über Wings-Protokoll"},
                {"name": "Redundante Kommunikation", "description": "4 unabhängige Kommunikationswege"},
                {"name": "Große Kapazität", "description": "Bis zu 200 Ajax-Geräte und 100 Kameras verwaltbar"}
            ],
            "accessories": ["PSU (12V/1.5A)", "Backup-Batterie", "Externe Antenne"]
        },
        {
            "name": "Hub 2 (2G) Jeweller",
            "category": "hubs",
            "product_line": "intrusion_baseline",
            "description": "Intelligent security control panel supporting detectors with photo verification. 3 communication channels with 2G support",
            "short_description": "Alarmzentrale mit Foto-Verifikation (2G)",
            "usps": ["Foto-Verifikation", "3 Kommunikationswege", "Bis zu 100 Geräte", "2G Support"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller), 433 MHz (Wings)",
                "range": "bis zu 2000m (Jeweller)",
                "communication": ["Ethernet", "2G (2x SIM)"],
                "max_devices": 100,
                "max_cameras": 25,
                "operating_temp": "0°C bis +50°C",
                "battery_life": "bis zu 16 Stunden",
                "xortec_nr": "600810001/600810002",
                "hersteller_nr": "7561.52.BL1/7561.52.WH1"
            },
            "features": [
                {"name": "Foto-Verifikation", "description": "Visuelle Alarmbestätigung"},
                {"name": "3 Kommunikationswege", "description": "Ethernet + 2x 2G SIM"},
                {"name": "9 Sicherheitsgruppen", "description": "Flexible Zonenverwaltung"}
            ],
            "accessories": ["PSU", "Backup-Batterie"]
        },
        {
            "name": "Hub 2 (4G) Jeweller",
            "category": "hubs",
            "product_line": "intrusion_baseline",
            "description": "Intelligent security control panel supporting detectors with photo verification. 3 communication channels with 4G/LTE support",
            "short_description": "Alarmzentrale mit Foto-Verifikation (4G)",
            "usps": ["Foto-Verifikation", "3 Kommunikationswege", "Bis zu 100 Geräte", "4G/LTE Support"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller), 433 MHz (Wings)",
                "range": "bis zu 2000m (Jeweller)",
                "communication": ["Ethernet", "2G/3G/LTE (2x SIM)"],
                "max_devices": 100,
                "max_cameras": 25,
                "operating_temp": "0°C bis +50°C",
                "battery_life": "bis zu 15 Stunden",
                "xortec_nr": "600810003/600810004",
                "hersteller_nr": "7562.52.BL1/7562.52.WH1"
            },
            "features": [
                {"name": "Foto-Verifikation in 9 Sekunden", "description": "Mit LTE-Unterstützung"},
                {"name": "3 Kommunikationswege", "description": "Ethernet + 2x LTE SIM"},
                {"name": "9 Sicherheitsgruppen", "description": "Flexible Zonenverwaltung"}
            ],
            "accessories": ["PSU", "Backup-Batterie"]
        },
        {
            "name": "Hub BP Jeweller",
            "category": "hubs", 
            "product_line": "intrusion_baseline",
            "description": "Wireless battery-powered control panel for off-grid locations. Supports photo verification. Connectable via two SIM cards (2G/3G/LTE)",
            "short_description": "Batteriebetriebene Alarmzentrale für netzferne Standorte",
            "usps": ["NEU", "Batteriebetrieben", "Mobil einsetzbar", "Bis zu 100 Geräte"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_bp_jeweller_black_1760739e4c%402.png&1732115997",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller), 433 MHz (Wings)",
                "range": "bis zu 2000m (Jeweller)",
                "communication": ["2G/3G/LTE (2x SIM)"],
                "max_devices": 100,
                "max_cameras": 25,
                "battery_life": "bis zu 46 Monate (Battery Saver Mode)",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP65",
                "xortec_nr": "600810735/600810736",
                "hersteller_nr": "25338.55.BL1/25338.55.WH1"
            },
            "features": [
                {"name": "Batteriebetrieb", "description": "Unabhängig von Stromnetz, bis zu 46 Monate Laufzeit"},
                {"name": "Robust", "description": "IP65 Schutzklasse für raue Umgebungen"},
                {"name": "Foto-Verifikation", "description": "Visuelle Alarmbestätigung"}
            ],
            "accessories": ["Internal Battery NB (7.2V/95Ah)", "Internal Battery RB (6.4V/36Ah)", "External Antenna"]
        },

        # ========================================================================
        # INTRUSION BASELINE - RANGE EXTENDERS
        # ========================================================================
        {
            "name": "ReX 2 Jeweller",
            "category": "range_extenders",
            "product_line": "intrusion_baseline",
            "description": "Wireless radio signal range extender supporting Jeweller and Wings protocols",
            "short_description": "Funk-Reichweitenverlängerer mit Jeweller & Wings",
            "usps": ["Jeweller + Wings", "2000m Reichweite", "85 Geräte pro ReX", "Extern gespeist"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Frex_2_ca92ad0fe2%402.png&1689158367",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller + Wings)",
                "range": "bis zu 2000m",
                "max_devices": 85,
                "operating_temp": "-10°C bis +40°C",
                "power": "5V DC (Micro-USB)",
                "xortec_nr": "600810045/600810046",
                "hersteller_nr": "16778.52.BL1/16778.52.WH1"
            },
            "features": [
                {"name": "Dual-Protokoll", "description": "Unterstützt Jeweller und Wings gleichzeitig"},
                {"name": "Große Reichweite", "description": "Erweitert Funknetz um bis zu 2000m"},
                {"name": "85 Geräte", "description": "Kann bis zu 85 Geräte verwalten"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION BASELINE - OPENING DETECTORS
        # ========================================================================
        {
            "name": "DoorProtect Jeweller",
            "category": "opening_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless opening detector with surface mount design",
            "short_description": "Kompakter Tür-/Fenstersensor",
            "usps": ["Kompakt", "7 Jahre Batterie", "Grade 2", "Einfache Montage"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_e1d51a9c9a%402.png&1689152842",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "ip_rating": "IP50",
                "xortec_nr": "600810031/600810032",
                "hersteller_nr": "8011.52.BL1/8011.52.WH1"
            },
            "features": [
                {"name": "Kompaktes Design", "description": "Unauffällige Installation an Türen und Fenstern"},
                {"name": "Lange Batterielaufzeit", "description": "Bis zu 7 Jahre ohne Batteriewechsel"},
                {"name": "Anti-Sabotage", "description": "Meldet Manipulationsversuche"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "DoorProtect Plus Jeweller",
            "category": "opening_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless opening detector with additional tilt and shock sensors",
            "short_description": "Erweiteter Tür-/Fenstersensor mit Neigung & Erschütterung",
            "usps": ["3-in-1 Sensor", "Grade 2", "Neigung & Erschütterung", "7 Jahre Batterie"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_plus_1d3ec6085c%402.png&1689152842",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "ip_rating": "IP50",
                "xortec_nr": "600810033/600810034",
                "hersteller_nr": "8012.52.BL1/8012.52.WH1"
            },
            "features": [
                {"name": "3-in-1 Sensor", "description": "Öffnung, Neigung und Erschütterung in einem Gerät"},
                {"name": "Rollladen-Schutz", "description": "Erkennt Manipulationsversuche an Rollläden"},
                {"name": "Garage/Tor-Überwachung", "description": "Ideal für Garagen und Tore"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION BASELINE - GLASS BREAK DETECTORS
        # ========================================================================
        {
            "name": "GlassProtect Jeweller",
            "category": "glass_break_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless acoustic glass break detector",
            "short_description": "Akustischer Glasbruchmelder",
            "usps": ["9m Reichweite", "Grade 2", "7 Jahre Batterie", "Akustische Erkennung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fglassprotect_4ce0c53a8f%402.png&1689152842",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "detection_range": "9m Radius",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "ip_rating": "IP50",
                "xortec_nr": "600810035/600810036",
                "hersteller_nr": "8014.52.BL1/8014.52.WH1"
            },
            "features": [
                {"name": "Akustische Erkennung", "description": "Erkennt Glasbruch durch Schallanalyse"},
                {"name": "Falschalarmsicher", "description": "Intelligente Algorithmen gegen Fehlalarme"},
                {"name": "Große Abdeckung", "description": "Überwacht mehrere Fenster in 9m Radius"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION BASELINE - MOTION DETECTORS
        # ========================================================================
        {
            "name": "MotionProtect Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless IR motion detector",
            "short_description": "Standard PIR-Bewegungsmelder",
            "usps": ["12m Erfassung", "Grade 2", "7 Jahre Batterie", "Haustierimmun"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmp_xl_93d1779d25%402.jpg&1714486620",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "detection_range": "12m",
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MotionProtect Plus Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless IR motion detector with an additional K-band microwave sensor",
            "short_description": "Dual-Technologie Bewegungsmelder",
            "usps": ["Duale Sensorik", "Grade 2", "Anti-Masking", "Falschalarmsicher"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmp_xl_93d1779d25%402.jpg&1714486620",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "detection_range": "12m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "ip_rating": "IP50",
                "xortec_nr": "600810027/600810028",
                "hersteller_nr": "8011.52.BL1/8011.52.WH1"
            },
            "features": [
                {"name": "Dual-Technologie", "description": "PIR + Mikrowellen-Sensor für höchste Zuverlässigkeit"},
                {"name": "Anti-Masking", "description": "Erkennt Versuche der Sensorabdeckung"},
                {"name": "Adaptive Empfindlichkeit", "description": "Automatische Anpassung an Umgebung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MotionCam Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless IR motion detector supporting photo by alarm feature",
            "short_description": "PIR-Bewegungsmelder mit Kamera",
            "usps": ["Foto-Verifikation", "Grade 2", "Anti-Sabotage", "Haustierimmun"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmc_j_xl_c08a42c711%402.jpg&1721123433",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "detection_range": "12m",
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MotionProtect Curtain Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless curtain motion detector for perimeter protection",
            "short_description": "Vorhang-Bewegungsmelder für Perimeterüberwachung",
            "usps": ["Schmaler Erfassungsbereich", "15m Reichweite", "Haustierimmun", "7 Jahre Batterie"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotion_protect_curtain_xl_a58f136c0b%402.jpg&1755768877",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "detection_range": "15m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810037/600810038",
                "hersteller_nr": "12034.52.BL1/12034.52.WH1"
            },
            "features": [
                {"name": "Schmaler Erfassungsbereich", "description": "Idealer Vorhang-Schutz für Fenster und Türen"},
                {"name": "Haustierimmunität", "description": "Ignoriert Haustiere"},
                {"name": "Perimeterschutz", "description": "Perfekt für Außenbereichsüberwachung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "CombiProtect Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless combined motion and glass break detector",
            "short_description": "NEU: Kombi-Melder Bewegung + Glasbruch",
            "usps": ["NEU", "2-in-1 Sensor", "Bewegung + Glasbruch", "Grade 2"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fcp_j_xl_ea6b727647%402.jpg&1718012539",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "detection_range": "12m (PIR), 9m (Glasbruch)",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810039/600810040",
                "hersteller_nr": "12045.52.BL1/12045.52.WH1"
            },
            "features": [
                {"name": "2-in-1 Sensor", "description": "Bewegung und Glasbruch in einem Gerät"},
                {"name": "Kosteneffizient", "description": "Ein Gerät statt zwei"},
                {"name": "Haustierimmun", "description": "PIR ignoriert Haustiere bis 20kg"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MotionProtect Outdoor Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless outdoor motion detector with dual PIR sensors and anti-masking",
            "short_description": "Outdoor Bewegungsmelder mit Dual-PIR",
            "usps": ["Outdoor", "Dual-PIR", "Anti-Masking", "IP55"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_outdoor_black_f8b5c7d4e2%402.png&1689152842",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "detection_range": "15m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-25°C bis +60°C",
                "ip_rating": "IP55",
                "xortec_nr": "600810041/600810042",
                "hersteller_nr": "12050.52.BL1/12050.52.WH1"
            },
            "features": [
                {"name": "Dual-PIR Technologie", "description": "Zwei unabhängige PIR-Sensoren für höchste Zuverlässigkeit"},
                {"name": "Wetterfest", "description": "IP55 Schutz für raue Außenbedingungen"},
                {"name": "Anti-Masking", "description": "Erkennt Verdeckungsversuche"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "DualCurtain Outdoor Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless dual-tech outdoor curtain motion detector with PIR and microwave",
            "short_description": "NEU: Dual-Tech Outdoor Vorhang-Melder",
            "usps": ["NEU", "Dual-Tech", "PIR + Mikrowelle", "Outdoor IP54"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdualcurtain_outdoor_black_7f5a8c9b21%402.png&1689152842",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "detection_range": "30m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-25°C bis +60°C",
                "ip_rating": "IP54",
                "xortec_nr": "600810043/600810044",
                "hersteller_nr": "12055.52.BL1/12055.52.WH1"
            },
            "features": [
                {"name": "Dual-Technologie", "description": "PIR + Mikrowelle für maximale Zuverlässigkeit"},
                {"name": "30m Reichweite", "description": "Große Abdeckung für Perimeter"},
                {"name": "Outdoor", "description": "IP54 Schutz für Außeneinsatz"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION BASELINE - KEYPADS
        # ========================================================================
        {
            "name": "KeyPad Plus Jeweller",
            "category": "keypads",
            "product_line": "intrusion_baseline",
            "description": "Wireless control keypad with RFID card reader and touch buttons",
            "short_description": "NEU: Tastatur mit RFID und Touch",
            "usps": ["NEU", "Touch-Tasten", "RFID-Leser", "Code & Karten"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_plus_jeweller_black_25cf406a42%402.png&1732188086",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 4.5 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810737/600810738",
                "hersteller_nr": "8001.52.BL1/8001.52.WH1"
            },
            "features": [
                {"name": "Touch-Tasten", "description": "Moderne kapazitive Touch-Oberfläche"},
                {"name": "RFID-Leser", "description": "Unterstützt Pass und Tag für schnelle Bedienung"},
                {"name": "Duress-Funktion", "description": "Stiller Alarm bei Zwangssituationen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"],
            "accessories": ["Pass", "Tag", "Holder"]
        },
        {
            "name": "KeyPad Jeweller",
            "category": "keypads",
            "product_line": "intrusion_baseline",
            "description": "Wireless control keypad with touch buttons",
            "short_description": "Touch-Tastatur zur Systemsteuerung",
            "usps": ["Touch-Tasten", "Codes", "4.5 Jahre Batterie", "Grade 2"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_cb76223961%402.png&1689152843",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 4.5 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810047/600810048",
                "hersteller_nr": "8000.52.BL1/8000.52.WH1"
            },
            "features": [
                {"name": "Touch-Tasten", "description": "Kapazitive Touch-Oberfläche"},
                {"name": "Duress-Funktion", "description": "Stiller Alarm"},
                {"name": "LED-Anzeige", "description": "Klare Statusanzeige"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "KeyPad TouchScreen Jeweller",
            "category": "keypads",
            "product_line": "intrusion_baseline",
            "description": "Wireless control keypad with color touchscreen display and RFID",
            "short_description": "NEU: Touchscreen-Tastatur mit Farb-Display",
            "usps": ["NEU", "Farb-Touchscreen", "RFID", "Smart Home Control"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_touchscreen_black_7c5d8a9f32%402.png&1689152843",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 2 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "display": "2.4\" Farb-Touchscreen",
                "xortec_nr": "600810049/600810050",
                "hersteller_nr": "8002.52.BL1/8002.52.WH1"
            },
            "features": [
                {"name": "Farb-Touchscreen", "description": "2.4\" Display mit intuitivem Interface"},
                {"name": "Smart Home Control", "description": "Steuerung von Szenarien und Geräten"},
                {"name": "RFID + Code", "description": "Mehrere Authentifizierungsmethoden"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION BASELINE - BUTTONS
        # ========================================================================
        {
            "name": "Button Jeweller",
            "category": "buttons",
            "product_line": "intrusion_baseline",
            "description": "Wireless panic button / smart button with programmable actions",
            "short_description": "Panik-Button / Smart Button",
            "usps": ["Panik-Alarm", "Szenarien", "5 Jahre Batterie", "Kompakt"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbutton_0e53cdc0b2%402.png&1689152841",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810051/600810052",
                "hersteller_nr": "7628.52.BL1/7628.52.WH1"
            },
            "features": [
                {"name": "Panik-Alarm", "description": "Sofortiger stiller oder lauter Alarm"},
                {"name": "Szenarien", "description": "Steuerung von Smart-Home-Geräten"},
                {"name": "Kompakt", "description": "Klein und tragbar"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"],
            "accessories": ["Holder"]
        },
        {
            "name": "DoubleButton Jeweller",
            "category": "buttons",
            "product_line": "intrusion_baseline",
            "description": "Wireless panic button with two buttons for different actions",
            "short_description": "Doppel-Panik-Button",
            "usps": ["2 Buttons", "2 Aktionen", "5 Jahre Batterie", "Szenarien"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoublebutton_black_8f7a9c5d21%402.png&1689152841",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810053/600810054",
                "hersteller_nr": "7629.52.BL1/7629.52.WH1"
            },
            "features": [
                {"name": "2 unabhängige Buttons", "description": "Zwei verschiedene Aktionen möglich"},
                {"name": "Flexibel", "description": "Für Panik, Hilfe oder Smart Home"},
                {"name": "LED-Feedback", "description": "Bestätigung der Aktion"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "SpaceControl Jeweller",
            "category": "buttons",
            "product_line": "intrusion_baseline",
            "description": "Wireless key fob with 4 buttons for arming/disarming and panic",
            "short_description": "Funk-Fernbedienung mit 4 Tasten",
            "usps": ["4 Tasten", "Arm/Disarm", "Panik", "Kompakt"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fspacecontrol_black_6d8f9a7c43%402.png&1689152841",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m",
                "battery_life": "bis zu 2 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810055/600810056",
                "hersteller_nr": "7630.52.BL1/7630.52.WH1"
            },
            "features": [
                {"name": "4 Tasten", "description": "Arm/Disarm/Night Mode/Panik"},
                {"name": "Kompakt", "description": "Passt an jeden Schlüsselbund"},
                {"name": "LED-Feedback", "description": "Status-Rückmeldung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION BASELINE - SIRENS
        # ========================================================================
        {
            "name": "HomeSiren Jeweller",
            "category": "sirens",
            "product_line": "intrusion_baseline",
            "description": "Wireless indoor siren with LED indicator",
            "short_description": "Innensirene mit LED",
            "usps": ["105 dB", "LED-Anzeige", "5 Jahre Batterie", "Kompakt"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhomesiren_90d4c3023b%402.png&1689152842",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 2000m",
                "sound_level": "105 dB",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810059/600810060",
                "hersteller_nr": "11885.52.BL1/11885.52.WH1"
            },
            "features": [
                {"name": "105 dB laut", "description": "Effektive Abschreckung"},
                {"name": "LED-Anzeige", "description": "Visuelle Alarmanzeige"},
                {"name": "Lange Batterie", "description": "Bis zu 5 Jahre Laufzeit"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "StreetSiren Jeweller",
            "category": "sirens",
            "product_line": "intrusion_baseline",
            "description": "Wireless outdoor siren with LED frame and tamper",
            "short_description": "Außensirene mit LED-Rahmen",
            "usps": ["113 dB", "LED-Rahmen", "IP54", "Batterie"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstreetsiren_black_7f8a9c6d54%402.png&1689152842",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 2000m",
                "sound_level": "113 dB",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-25°C bis +60°C",
                "ip_rating": "IP54",
                "xortec_nr": "600810061/600810062",
                "hersteller_nr": "11889.52.BL1/11889.52.WH1"
            },
            "features": [
                {"name": "113 dB", "description": "Sehr lauter Alarm für draußen"},
                {"name": "LED-Rahmen", "description": "Visuelle Warnung weithin sichtbar"},
                {"name": "Wetterfest", "description": "IP54 für Außeneinsatz"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "StreetSiren DoubleDeck Jeweller",
            "category": "sirens",
            "product_line": "intrusion_baseline",
            "description": "Wireless outdoor siren with dual LED frames and powerful sound",
            "short_description": "NEU: Doppel-LED Außensirene",
            "usps": ["NEU", "113 dB", "Doppel-LED", "IP54"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstreetsiren_doubledeck_black_8c9a7f6d21%402.png&1689152842",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 2000m",
                "sound_level": "113 dB",
                "battery_life": "bis zu 3 Jahre",
                "operating_temp": "-25°C bis +60°C",
                "ip_rating": "IP54",
                "xortec_nr": "600810063/600810064",
                "hersteller_nr": "11890.52.BL1/11890.52.WH1"
            },
            "features": [
                {"name": "Doppel-LED-Rahmen", "description": "Noch auffälligere visuelle Warnung"},
                {"name": "113 dB", "description": "Maximale Abschreckung"},
                {"name": "Premium-Design", "description": "Hochwertige Verarbeitung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION SUPERIOR - HUBS
        # ========================================================================
        {
            "name": "Superior Hub Hybrid (4G)",
            "category": "hubs",
            "product_line": "intrusion_superior",
            "description": "Professional control panel for high-security applications with Jeweller and Fibra protocol support. Grade 3 certified",
            "short_description": "Grade 3 Hub für höchste Sicherheitsanforderungen",
            "usps": ["Grade 3", "Fibra + Jeweller", "Bis zu 400 Geräte", "Professional"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_hub_hybrid%402.png",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller + Fibra)",
                "range": "bis zu 2000m (Jeweller), 2000m (Fibra)",
                "communication": ["Wi-Fi", "Ethernet", "2G/3G/LTE (2x SIM)"],
                "max_devices": 400,
                "max_cameras": 200,
                "operating_temp": "-25°C bis +70°C",
                "xortec_nr": "600810701",
                "hersteller_nr": "25338.70.WH1"
            },
            "features": [
                {"name": "Grade 3 Zertifizierung", "description": "Höchste Sicherheitsstufe nach EN 50131"},
                {"name": "Dual-Protokoll", "description": "Unterstützt sowohl Jeweller als auch Fibra"},
                {"name": "Maximale Kapazität", "description": "Bis zu 400 Geräte verwaltbar"}
            ],
            "accessories": ["PSU Professional", "UPS Module", "Fibra Splitter"]
        },
        {
            "name": "Superior Hub Hybrid 2",
            "category": "hubs",
            "product_line": "intrusion_superior",
            "description": "Hybrid control panel for medium to large setups. Works with up to 250 Fibra and Jeweller devices. Grade 3 certified",
            "short_description": "NEU: Grade 3 Hybrid-Hub für mittlere bis große Anlagen",
            "usps": ["NEU", "Grade 3", "Bis zu 250 Geräte", "Fibra + Jeweller"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_hybrid_2_xl_953608b81a%402.jpg&1761295315",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller + Fibra)",
                "range": "bis zu 11,450 ft (wireless), 6,550 ft (wired)",
                "communication": ["Ethernet", "2G/3G/LTE (2x SIM)"],
                "max_devices": 250,
                "max_cameras": 250,
                "operating_temp": "-25°C bis +70°C",
                "security_groups": 25,
                "automation_scenarios": 64,
                "xortec_nr": "600810702",
                "hersteller_nr": "SUP.HH2.WH"
            },
            "features": [
                {"name": "Grade 3 Zertifizierung", "description": "EN 50131 Grade 3 zertifiziert"},
                {"name": "250 Geräte", "description": "Unterstützt bis zu 250 verdrahtete oder kabellose Geräte"},
                {"name": "25 Sicherheitsgruppen", "description": "Flexible Zugangsverwaltung"}
            ],
            "accessories": ["Backup Battery", "External Antenna"]
        },
        {
            "name": "Superior Hub G3 Jeweller",
            "category": "hubs",
            "product_line": "intrusion_superior",
            "description": "Wireless control panel with support for photo verification. Connectable via Ethernet, Wi-Fi, and two SIM cards (2G/LTE). Grade 3 certified",
            "short_description": "NEU: Weltweit erste kabellose Grade 3 Zentrale",
            "usps": ["NEU", "Grade 3", "Wireless", "Bis zu 250 Geräte"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_hub_g3_j_xl_74cd3c8c40%402.jpg&1763225615",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Superior Jeweller)",
                "range": "bis zu 11,450 ft",
                "communication": ["Ethernet", "Wi-Fi", "2G/LTE (2x SIM)"],
                "max_devices": 250,
                "max_cameras": 528,
                "operating_temp": "-10°C bis +40°C",
                "security_groups": 25,
                "automation_scenarios": 64,
                "xortec_nr": "600810703",
                "hersteller_nr": "SUP.HG3J.WH"
            },
            "features": [
                {"name": "Weltweit erste wireless Grade 3", "description": "Erste komplett kabellose Grade 3 Sicherheitszentrale"},
                {"name": "4 Kommunikationswege", "description": "Ethernet, Wi-Fi, 2x LTE SIM"},
                {"name": "250 Geräte", "description": "Bis zu 250 kabellose Ajax-Geräte"}
            ],
            "accessories": ["Superior Internal Battery", "External Antenna"]
        },
        {
            "name": "Superior MegaHub",
            "category": "hubs",
            "product_line": "intrusion_superior",
            "description": "Hybrid control panel for the biggest projects. Works with up to 999 Fibra and Jeweller devices. Grade 3 certified",
            "short_description": "NEU: Enterprise Hub für bis zu 999 Geräte",
            "usps": ["NEU", "Grade 3", "Bis zu 999 Geräte", "Enterprise"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmega_hub1_xl_cdf9412ceb%402.jpg&1763040650",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller + Fibra)",
                "range": "bis zu 6,550 ft",
                "communication": ["Ethernet", "Wi-Fi", "2G/LTE (2x SIM)"],
                "max_devices": 999,
                "max_cameras": 999,
                "operating_temp": "-10°C bis +40°C",
                "security_groups": 100,
                "automation_scenarios": 100,
                "xortec_nr": "600810704",
                "hersteller_nr": "SUP.MH.WH"
            },
            "features": [
                {"name": "999 Geräte", "description": "Unübertroffene Kapazität für Enterprise-Projekte"},
                {"name": "100 Sicherheitsgruppen", "description": "Flexible Zugangsverwaltung für große Anlagen"},
                {"name": "100 Szenarien", "description": "Umfassende Automation"}
            ],
            "accessories": ["18 Ah Backup Battery", "External Antenna", "Fibra Accessories"]
        },

        # ========================================================================
        # INTRUSION SUPERIOR - MOTION DETECTORS
        # ========================================================================
        {
            "name": "Superior MotionProtect Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_superior",
            "description": "Wireless IR motion detector. Superior edition with Grade 3 certification",
            "short_description": "Professional PIR-Bewegungsmelder Grade 3",
            "usps": ["Grade 3", "Erweiterte Anti-Sabotage", "Professional", "12m Erfassung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmpsj_s_34e8d588e9%402.png&1688046986",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "detection_range": "12m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP50",
                "xortec_nr": "600810625",
                "hersteller_nr": "108010.52.WH1"
            },
            "features": [
                {"name": "Grade 3 Zertifizierung", "description": "Höchste Sicherheitsstufe nach EN 50131"},
                {"name": "Erweiterte Anti-Sabotage", "description": "Professioneller Manipulationsschutz"},
                {"name": "Temperaturkompensation", "description": "Stabile Erkennung bei Temperaturschwankungen"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },

        # ========================================================================
        # EN54 FIRE & LIFE SAFETY
        # ========================================================================
        {
            "name": "FireProtect 2 RB (Heat/Smoke/CO) UL Jeweller",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Wireless combined heat, smoke, and CO detector with replaceable batteries. UL certified",
            "short_description": "Kombimelder: Hitze, Rauch & CO",
            "usps": ["3-in-1 Sensor", "UL-zertifiziert", "Austauschbare Batterien", "Sirene integriert"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffireprotect2_smoke_028348da8d%402.png&1689152843",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 4 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810801",
                "hersteller_nr": "FP2-RB-HSC-UL"
            },
            "features": [
                {"name": "3-Sensor-Kombination", "description": "Hitze + Rauch + CO in einem Gerät"},
                {"name": "UL-zertifiziert", "description": "Erfüllt US-Brandschutznormen"},
                {"name": "Integrierte Sirene", "description": "85dB Alarm bei Gefahrenerkennung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "FireProtect 2 RB (Heat/Smoke) UL Jeweller",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Wireless combined heat and smoke detector with replaceable batteries",
            "short_description": "Kombimelder: Hitze & Rauch",
            "usps": ["2-in-1 Sensor", "UL-zertifiziert", "Austauschbare Batterien", "Sirene integriert"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffireprotect2_smoke_028348da8d%402.png&1689152843",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 4 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810802",
                "hersteller_nr": "FP2-RB-HS-UL"
            },
            "features": [
                {"name": "2-Sensor-Kombination", "description": "Hitze + Rauch für zuverlässige Erkennung"},
                {"name": "UL-zertifiziert", "description": "Erfüllt US-Brandschutznormen"},
                {"name": "HazeFlow Algorithmus", "description": "Reduziert Fehlalarme"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "FireProtect 2 RB (Heat) UL Jeweller",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Wireless fire detector with a heat sensor. Version with replaceable batteries",
            "short_description": "NEU: Hitzemelder",
            "usps": ["NEU", "Hitzesensor", "UL-zertifiziert", "Batteriebetrieben"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffire_protect_2_ul_black_7620cda5e6%402.png&1732126298",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810803",
                "hersteller_nr": "FP2-RB-H-UL"
            },
            "features": [
                {"name": "Hitzeerkennung", "description": "Ideal für Küchen und staubige Bereiche"},
                {"name": "Lange Laufzeit", "description": "Bis zu 7 Jahre Batteriebetrieb"},
                {"name": "UL-zertifiziert", "description": "Erfüllt internationale Standards"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "FireProtect 2 RB (CO) UL Jeweller",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Wireless fire detector with a CO sensor. Version with replaceable batteries",
            "short_description": "NEU: CO-Melder",
            "usps": ["NEU", "CO-Sensor", "UL-zertifiziert", "Batteriebetrieben"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffire_protect_2_ul_black_7620cda5e6%402.png&1732126298",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810804",
                "hersteller_nr": "FP2-RB-CO-UL"
            },
            "features": [
                {"name": "CO-Erkennung", "description": "Warnt vor tödlichem Kohlenmonoxid"},
                {"name": "Lange Laufzeit", "description": "Bis zu 7 Jahre Batteriebetrieb"},
                {"name": "UL-zertifiziert", "description": "Erfüllt internationale Standards"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # VIDEO BASELINE - NVRs
        # ========================================================================
        {
            "name": "NVR (8-ch)",
            "category": "nvrs", 
            "product_line": "video_baseline",
            "description": "Network video recorder for 8 channels",
            "short_description": "Standard 8-Kanal NVR",
            "usps": ["8 Kanäle", "Standard Features", "Zuverlässig", "Kosteneffizient"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fnvr_black_453b202dae%402.png&1696595007",
            "colors": ["Black"],
            "specifications": {
                "channels": 8,
                "max_cameras": 8,
                "resolution": "bis zu 4K",
                "storage": "2x SATA HDD",
                "network": "Ethernet",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600810771",
                "hersteller_nr": "NVR-8CH"
            },
            "features": [
                {"name": "8 Kamera-Kanäle", "description": "Unterstützt bis zu 8 IP-Kameras"},
                {"name": "4K-Aufzeichnung", "description": "Hochauflösende Videoaufzeichnung"},
                {"name": "RAID-Unterstützung", "description": "Datensicherheit durch redundante Speicherung"}
            ],
            "accessories": ["HDD (Festplatte)", "HDMI-Kabel", "Netzwerkkabel"]
        },
        {
            "name": "NVR (16-ch)",
            "category": "nvrs",
            "product_line": "video_baseline",
            "description": "Network video recorder for 16 channels",
            "short_description": "Standard 16-Kanal NVR",
            "usps": ["16 Kanäle", "Erweiterte Kapazität", "4K Recording", "RAID Support"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fnvr_black_453b202dae%402.png&1696595007",
            "colors": ["Black"],
            "specifications": {
                "channels": 16,
                "max_cameras": 16,
                "resolution": "bis zu 4K",
                "storage": "4x SATA HDD",
                "network": "Ethernet",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600810772",
                "hersteller_nr": "NVR-16CH"
            },
            "features": [
                {"name": "16 Kamera-Kanäle", "description": "Unterstützt bis zu 16 IP-Kameras"},
                {"name": "4K-Aufzeichnung", "description": "Hochauflösende Videoaufzeichnung"},
                {"name": "Erweiterte Speicherung", "description": "Bis zu 4 Festplatten für große Kapazität"}
            ],
            "accessories": ["HDD (Festplatte)", "HDMI-Kabel", "Netzwerkkabel"]
        },
        {
            "name": "NVR DC (8-ch)",
            "category": "nvrs",
            "product_line": "video_baseline",
            "description": "Network video recorder for 8 channels powered by a low-voltage power supply",
            "short_description": "NEU: DC-betriebener 8-Kanal NVR",
            "usps": ["NEU", "DC-Betrieb", "8 Kanäle", "Niederspannung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fnvr_black_453b202dae%402.png&1696595007",
            "colors": ["Black"],
            "specifications": {
                "channels": 8,
                "max_cameras": 8,
                "resolution": "bis zu 4K", 
                "power": "12V DC",
                "storage": "2x SATA HDD",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600810773",
                "hersteller_nr": "NVR-DC-8CH"
            },
            "features": [
                {"name": "DC-Versorgung", "description": "12V DC-Betrieb für flexible Installation"},
                {"name": "8 Kamera-Kanäle", "description": "Unterstützt bis zu 8 IP-Kameras"},
                {"name": "Energieeffizient", "description": "Niedrigerer Stromverbrauch"}
            ],
            "accessories": ["12V PSU for NVR", "HDD (Festplatte)", "HDMI-Kabel"]
        },
        {
            "name": "NVR DC (16-ch)",
            "category": "nvrs",
            "product_line": "video_baseline",
            "description": "Network video recorder for 16 channels powered by a low-voltage power supply",
            "short_description": "NEU: DC-betriebener 16-Kanal NVR",
            "usps": ["NEU", "DC-Betrieb", "16 Kanäle", "Erweiterte Kapazität"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fnvr_black_453b202dae%402.png&1696595007",
            "colors": ["Black"],
            "specifications": {
                "channels": 16,
                "max_cameras": 16,
                "resolution": "bis zu 4K",
                "power": "12V DC", 
                "storage": "4x SATA HDD",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600810774",
                "hersteller_nr": "NVR-DC-16CH"
            },
            "features": [
                {"name": "DC-Versorgung", "description": "12V DC-Betrieb für flexible Installation"},
                {"name": "16 Kamera-Kanäle", "description": "Unterstützt bis zu 16 IP-Kameras"},
                {"name": "Große Kapazität", "description": "Bis zu 4 Festplatten für erweiterte Speicherung"}
            ],
            "accessories": ["12V PSU for NVR", "HDD (Festplatte)", "HDMI-Kabel"]
        },

        # ========================================================================
        # VIDEO BASELINE - CAMERAS
        # ========================================================================
        {
            "name": "BulletCam HL 5Mp",
            "category": "cameras",
            "product_line": "video_baseline",
            "description": "5MP outdoor bullet camera with hybrid lighting",
            "short_description": "5MP Außenkamera mit Hybrid-Beleuchtung",
            "usps": ["5MP Auflösung", "Hybrid-Beleuchtung", "IP67", "Smart Motion AI"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbulletcam_hl_5mp_white_98769dc066%402.png&1724409002",
            "colors": ["Black", "White"],
            "specifications": {
                "resolution": "5MP (2592x1944)",
                "night_vision": "Hybrid Lighting (IR + Weißlicht)",
                "viewing_angle": "103° (H), 54° (V)",
                "operating_temp": "-30°C bis +60°C",
                "ip_rating": "IP67",
                "xortec_nr": "600810451/600810452",
                "hersteller_nr": "BC-HL-5MP-BL/BC-HL-5MP-WH"
            },
            "features": [
                {"name": "Hybrid-Beleuchtung", "description": "Kombiniert IR und Weißlicht für optimale Nachtsicht"},
                {"name": "Smart Motion AI", "description": "KI-gestützte Bewegungserkennung"},
                {"name": "Wetterfest", "description": "IP67 für extremes Wetter"}
            ],
            "compatible_nvrs": ["NVR (8-ch)", "NVR (16-ch)", "NVR DC (8-ch)", "NVR DC (16-ch)"]
        },
        {
            "name": "BulletCam HL 8Mp",
            "category": "cameras",
            "product_line": "video_baseline",
            "description": "8MP outdoor bullet camera with hybrid lighting",
            "short_description": "8MP Außenkamera mit Hybrid-Beleuchtung",
            "usps": ["8MP 4K", "Hybrid-Beleuchtung", "IP67", "Smart Motion AI"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbulletcam_hl_5mp_white_98769dc066%402.png&1724409002",
            "colors": ["Black", "White"],
            "specifications": {
                "resolution": "8MP (3840x2160)",
                "night_vision": "Hybrid Lighting (IR + Weißlicht)",
                "viewing_angle": "106° (H), 56° (V)",
                "operating_temp": "-30°C bis +60°C",
                "ip_rating": "IP67",
                "xortec_nr": "600810453/600810454",
                "hersteller_nr": "BC-HL-8MP-BL/BC-HL-8MP-WH"
            },
            "features": [
                {"name": "4K Ultra HD", "description": "8MP Auflösung für kristallklare Bilder"},
                {"name": "Hybrid-Beleuchtung", "description": "Kombiniert IR und Weißlicht"},
                {"name": "Smart Motion AI", "description": "KI-gestützte Bewegungserkennung"}
            ],
            "compatible_nvrs": ["NVR (8-ch)", "NVR (16-ch)", "NVR DC (8-ch)", "NVR DC (16-ch)"]
        },
        {
            "name": "TurretCam HL 5Mp",
            "category": "cameras",
            "product_line": "video_baseline",
            "description": "5MP outdoor turret camera with hybrid lighting",
            "short_description": "5MP Turret-Kamera mit Hybrid-Beleuchtung",
            "usps": ["5MP Auflösung", "Kompakt", "Hybrid-Beleuchtung", "Vandalismusschutz"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fturretcam_hl_5mp_white_7ffbadaf31%402.png&1724409002",
            "colors": ["Black", "White"],
            "specifications": {
                "resolution": "5MP (2592x1944)",
                "night_vision": "Hybrid Lighting (IR + Weißlicht)",
                "viewing_angle": "103° (H), 54° (V)",
                "operating_temp": "-30°C bis +60°C",
                "ip_rating": "IP67",
                "ik_rating": "IK10",
                "xortec_nr": "600810455/600810456",
                "hersteller_nr": "TC-HL-5MP-BL/TC-HL-5MP-WH"
            },
            "features": [
                {"name": "Vandalismusschutz", "description": "IK10 Schutz gegen mechanische Einwirkung"},
                {"name": "Kompaktes Design", "description": "Dezente Turret-Bauform"},
                {"name": "Hybrid-Beleuchtung", "description": "Optimale Nachtsicht"}
            ],
            "compatible_nvrs": ["NVR (8-ch)", "NVR (16-ch)", "NVR DC (8-ch)", "NVR DC (16-ch)"]
        },
        {
            "name": "DomeCam Mini HL 5Mp",
            "category": "cameras",
            "product_line": "video_baseline",
            "description": "5MP compact indoor/outdoor dome camera with hybrid lighting",
            "short_description": "Kompakte 5MP Dome-Kamera",
            "usps": ["NEU", "Kompakt", "5MP", "Innen & Außen"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdomecam_mini_hl_5mp_white_5a5f31adbb%402.png&1732117253",
            "colors": ["White"],
            "specifications": {
                "resolution": "5MP (2592x1944)",
                "night_vision": "Hybrid Lighting (IR + Weißlicht)",
                "viewing_angle": "103° (H), 54° (V)",
                "operating_temp": "-30°C bis +60°C",
                "ip_rating": "IP67",
                "xortec_nr": "600810749",
                "hersteller_nr": "DMC-MINI-HL-5MP"
            },
            "features": [
                {"name": "Kompakte Bauweise", "description": "Unauffällige Mini-Dome"},
                {"name": "Vielseitig einsetzbar", "description": "Für Innen- und Außenbereiche"},
                {"name": "Hybrid-Beleuchtung", "description": "Optimale Nachtsicht"}
            ],
            "compatible_nvrs": ["NVR (8-ch)", "NVR (16-ch)", "NVR DC (8-ch)", "NVR DC (16-ch)"]
        },

        # ========================================================================
        # VIDEO BASELINE - WI-FI CAMERAS
        # ========================================================================
        {
            "name": "IndoorCam",
            "category": "wifi_cameras",
            "product_line": "video_baseline",
            "description": "Wi-Fi security camera with AI motion detection",
            "short_description": "Wi-Fi Innenkamera mit KI",
            "usps": ["Wi-Fi", "KI-Erkennung", "2MP Full HD", "Cloud-Recording"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Findoor_cam_white_de88ac1cdb%402.png&1689152843",
            "colors": ["White"],
            "specifications": {
                "resolution": "2MP (1920x1080)",
                "night_vision": "IR Night Vision",
                "viewing_angle": "113° (H)",
                "connectivity": "Wi-Fi (2.4 GHz)",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600810901",
                "hersteller_nr": "IC-2MP-WIFI"
            },
            "features": [
                {"name": "KI-Bewegungserkennung", "description": "Unterscheidet zwischen Personen und Objekten"},
                {"name": "Cloud-Recording", "description": "Automatische Aufzeichnung in der Cloud"},
                {"name": "Zwei-Wege-Audio", "description": "Integriertes Mikrofon und Lautsprecher"}
            ],
            "compatible_nvrs": []
        },

        # ========================================================================
        # VIDEO BASELINE - DOORBELLS
        # ========================================================================
        {
            "name": "DoorBell",
            "category": "doorbells",
            "product_line": "video_baseline",
            "description": "Wi-Fi video doorbell with AI motion detection",
            "short_description": "Video-Türklingel mit KI",
            "usps": ["Wi-Fi", "KI-Erkennung", "2-Wege-Audio", "Cloud-Recording"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorbell_black_5a5f31adbb%402.png&1689152843",
            "colors": ["Black"],
            "specifications": {
                "resolution": "2MP (1920x1080)",
                "night_vision": "IR Night Vision",
                "viewing_angle": "160° (V)",
                "connectivity": "Wi-Fi (2.4 GHz)",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP65",
                "xortec_nr": "600810902",
                "hersteller_nr": "DB-2MP-WIFI"
            },
            "features": [
                {"name": "KI-Personenerkennung", "description": "Unterscheidet zwischen Personen und Objekten"},
                {"name": "2-Wege-Audio", "description": "Sprechen Sie mit Besuchern"},
                {"name": "Cloud-Recording", "description": "Automatische Aufzeichnung in der Cloud"}
            ],
            "compatible_nvrs": []
        },

        # ========================================================================
        # COMFORT & AUTOMATION
        # ========================================================================
        {
            "name": "WallSwitch Jeweller",
            "category": "relays",
            "product_line": "comfort_automation",
            "description": "Wireless power relay to control 110/230 V~ power supply remotely",
            "short_description": "Kabelloses Schaltrelais für 110/230V",
            "usps": ["110/230V", "Fernsteuerung", "Szenarien", "DIN-Montage"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fwallswitch_6f717abe66%402.png&1689152843",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "max_load": "3kW (110V) / 3.5kW (230V)",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600811001",
                "hersteller_nr": "WS-JW"
            },
            "features": [
                {"name": "Fernsteuerung", "description": "Schalten Sie Geräte per App"},
                {"name": "Szenarien", "description": "Automatisierung durch Szenarien"},
                {"name": "Energiemessung", "description": "Überwachen Sie den Stromverbrauch"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"],
            "accessories": ["DIN Holder"]
        },
        {
            "name": "Relay Jeweller",
            "category": "relays",
            "product_line": "comfort_automation",
            "description": "Wireless dry contact relay",
            "short_description": "Kabelloses Trockenrelais",
            "usps": ["Dry Contact", "Universell", "Szenarien", "DIN-Montage"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Frelay_a81e255a8b%402.png&1689152843",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "contact_type": "Dry Contact (NO/NC)",
                "max_voltage": "110V",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600811002",
                "hersteller_nr": "REL-JW"
            },
            "features": [
                {"name": "Dry Contact", "description": "Universell einsetzbar für verschiedene Geräte"},
                {"name": "Szenarien", "description": "Automatisierung durch Szenarien"},
                {"name": "Flexible Montage", "description": "DIN-Schiene oder Wandmontage"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"],
            "accessories": ["DIN Holder"]
        },
        {
            "name": "Socket (type B) Jeweller",
            "category": "sockets",
            "product_line": "comfort_automation",
            "description": "Smart plug with power consumption monitoring",
            "short_description": "NEU: Smarte Steckdose mit Verbrauchsmessung",
            "usps": ["NEU", "Verbrauchsmessung", "Fernsteuerung", "Kompakt"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsocket_type_b_black_12090b6794%402.png&1716796195",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1000m",
                "max_load": "1.8kW (110-120V)",
                "plug_type": "Type B (US)",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600811003/600811004",
                "hersteller_nr": "SOCK-B-JW-BL/SOCK-B-JW-WH"
            },
            "features": [
                {"name": "Verbrauchsmessung", "description": "Überwachen Sie den Stromverbrauch in Echtzeit"},
                {"name": "Zeitpläne", "description": "Automatisches Ein-/Ausschalten"},
                {"name": "Kompaktes Design", "description": "Nimmt wenig Platz ein"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "LeaksProtect Jeweller",
            "category": "leak_detectors",
            "product_line": "comfort_automation",
            "description": "Wireless water leak detector",
            "short_description": "Kabelloser Wasserleckmelder",
            "usps": ["Wasserleck-Erkennung", "7 Jahre Batterie", "Kompakt", "Szenarien"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fleaksprotect_8530909770%402.png&1689152842",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "0°C bis +50°C",
                "ip_rating": "IP65",
                "xortec_nr": "600811005/600811006",
                "hersteller_nr": "LP-JW-BL/LP-JW-WH"
            },
            "features": [
                {"name": "Früherkennung", "description": "Erkennt Wasserlecks sofort"},
                {"name": "Szenarien", "description": "Automatisches Absperren über WaterStop"},
                {"name": "IP65 Schutz", "description": "Geschützt gegen Wasser und Staub"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "WaterStop 1\" (DN 25) Jeweller",
            "category": "shutoff_valves",
            "product_line": "comfort_automation",
            "description": "Wireless remotely controlled water shutoff valve 1 inch",
            "short_description": "Kabelloses Wasserabsperrventil 1 Zoll",
            "usps": ["1\" (DN 25)", "Fernsteuerung", "Szenarien", "Motor-getrieben"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fwaterstop_feb7973a94%402.png&1689152843",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1000m",
                "valve_size": "1\" (DN 25)",
                "power": "110-230V AC oder 12V DC",
                "operating_temp": "0°C bis +50°C",
                "xortec_nr": "600811007",
                "hersteller_nr": "WS-1-JW"
            },
            "features": [
                {"name": "Fernsteuerung", "description": "Wasser per App abdrehen"},
                {"name": "Szenarien", "description": "Automatisches Absperren bei Leck"},
                {"name": "Manueller Override", "description": "Notfallbedienung am Ventil"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "LifeQuality Jeweller",
            "category": "air_quality_detectors",
            "product_line": "comfort_automation",
            "description": "Wireless temperature, humidity, and CO₂ monitor",
            "short_description": "Raumklima-Monitor (Temp, Feuchte, CO₂)",
            "usps": ["CO₂-Messung", "Temperatur", "Luftfeuchtigkeit", "E-Ink Display"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Flifequality_9644fe6470%402.png&1689152843",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 5 Jahre",
                "sensors": ["CO₂", "Temperatur", "Luftfeuchtigkeit"],
                "operating_temp": "0°C bis +50°C",
                "xortec_nr": "600811008",
                "hersteller_nr": "LQ-JW"
            },
            "features": [
                {"name": "3-in-1 Sensor", "description": "CO₂, Temperatur und Luftfeuchtigkeit"},
                {"name": "E-Ink Display", "description": "Energiesparendes Display"},
                {"name": "Szenarien", "description": "Automatische Lüftungssteuerung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MultiTransmitter Jeweller",
            "category": "integration_modules",
            "product_line": "comfort_automation",
            "description": "Wireless module to integrate up to 18 third-party devices into the Ajax system",
            "short_description": "Integrationsmodul für bis zu 18 Drittgeräte",
            "usps": ["Bis zu 18 Geräte", "Universell", "Verdrahtet", "DIN-Montage"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmultitransmitter_jeweller_a9d90bcffb%402.png&1707486834",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "inputs": "18 verdrahtete Eingänge",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600811009",
                "hersteller_nr": "MT-JW"
            },
            "features": [
                {"name": "18 Eingänge", "description": "Integrieren Sie bis zu 18 Drittgeräte"},
                {"name": "Universell", "description": "Für alle verdrahteten Sensoren und Melder"},
                {"name": "Szenarien", "description": "Automation mit integrierten Geräten"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "Transmitter Jeweller",
            "category": "integration_modules",
            "product_line": "comfort_automation",
            "description": "Wireless module to integrate one third-party device into the Ajax system",
            "short_description": "Integrationsmodul für 1 Drittgerät",
            "usps": ["1 Gerät", "Kompakt", "Verdrahtet", "Universell"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ftransmitter_897ae41178%402.png&1689152843",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "inputs": "1 verdrahteter Eingang",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600811010",
                "hersteller_nr": "TRM-JW"
            },
            "features": [
                {"name": "1 Eingang", "description": "Integrieren Sie ein Drittgerät"},
                {"name": "Kompakt", "description": "Klein und unauffällig"},
                {"name": "Batteriebetrieben", "description": "Keine externe Stromversorgung nötig"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "LightSwitch (1-gang) [120] Jeweller",
            "category": "light_switches",
            "product_line": "comfort_automation",
            "description": "Smart touch 1-gang light switch for 120V systems",
            "short_description": "NEU: 1-Kanal Touch-Lichtschalter",
            "usps": ["NEU", "Touch-Bedienung", "Szenarien", "120V"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fls_120_1_gang_black_715a1a19d0%402.png&1732142073",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1000m",
                "voltage": "120V AC",
                "max_load": "1200W",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600811011/600811012",
                "hersteller_nr": "LS-1G-120-JW-BL/LS-1G-120-JW-WH"
            },
            "features": [
                {"name": "Touch-Bedienung", "description": "Moderne kapazitive Touch-Oberfläche"},
                {"name": "Szenarien", "description": "Automation und Zeitpläne"},
                {"name": "Dimmer-kompatibel", "description": "Unterstützt dimmbare Leuchtmittel"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION BASELINE - MOTION DETECTORS (ADDITIONAL)
        # ========================================================================
        {
            "name": "MotionCam (PhOD) Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless IR motion detector with Photo on Demand and Photo by Script functions",
            "short_description": "PIR-Bewegungsmelder mit Foto on Demand",
            "usps": ["Foto on Demand", "Foto nach Zeitplan", "Foto nach Szenario", "Grade 2"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotioncam_phod_xl_30e7426296%402.jpg&1709543488",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller + Wings)",
                "range": "bis zu 1700m",
                "detection_range": "12m",
                "battery_life": "bis zu 4 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810065/600810066",
                "hersteller_nr": "8020.55.BL1/8020.55.WH1"
            },
            "features": [
                {"name": "Photo on Demand", "description": "Fotos auf Anfrage jederzeit möglich"},
                {"name": "Photo by Script", "description": "Automatische Fotos nach Szenarien"},
                {"name": "Haustierimmunität", "description": "Ignoriert Haustiere bis 20kg"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MotionCam Outdoor HighMount (PhOD) Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless IR motion detector with extended photo verification possibilities. For outdoor installation at a 2-4 m height from the ground",
            "short_description": "Outdoor PIR mit erweiterter Foto-Verifikation (2-4m Höhe)",
            "usps": ["NEU", "2-4m Montagehöhe", "Foto-Verifikation", "Outdoor IP55"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmc_outdoor_high_mount_phod_jeweller_xl_7b09da9d88%402.jpg&1732142253",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller + Wings)",
                "range": "bis zu 1700m",
                "detection_range": "15m",
                "battery_life": "bis zu 3 Jahre",
                "operating_temp": "-25°C bis +60°C",
                "ip_rating": "IP55",
                "xortec_nr": "600810067/600810068",
                "hersteller_nr": "8020.60.BL1/8020.60.WH1"
            },
            "features": [
                {"name": "Hohe Montage", "description": "Speziell für 2-4m Montagehöhe entwickelt"},
                {"name": "Erweiterte Foto-Verifikation", "description": "8 Foto-Verifikationstypen"},
                {"name": "Outdoor", "description": "IP55 Schutz für raue Bedingungen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "Curtain Outdoor Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless dual-technology curtain motion detector for outdoor and indoor use. First line of defense for perimeter protection",
            "short_description": "Outdoor Vorhang-Melder für Perimeter-Schutz",
            "usps": ["Perimeter-Schutz", "Dual-Tech", "39 ft Reichweite", "Outdoor IP55"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fco_xl_031082deba%402.jpg&1722925558",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller + Wings)",
                "range": "bis zu 1700m",
                "detection_range": "39 ft (ca. 12m)",
                "battery_life": "bis zu 3 Jahre",
                "operating_temp": "-13°F bis +140°F (-25°C bis +60°C)",
                "ip_rating": "IP55",
                "viewing_angle_horizontal": "8°",
                "viewing_angle_vertical": "85° / 15°",
                "xortec_nr": "600810067/600810068",
                "hersteller_nr": "CO.Y.J.BL/CO.Y.J.WH"
            },
            "features": [
                {"name": "Schmaler Erfassungsbereich", "description": "8° horizontal für präzisen Perimeter-Schutz"},
                {"name": "Dual-Technologie", "description": "PIR + K-band Mikrowelle"},
                {"name": "Anti-Masking Hood", "description": "Schutz vor Regen und Schnee"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "Curtain Outdoor Mini Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless dual-technology curtain motion detector in a more compact body for easy placement. For outdoor and indoor use",
            "short_description": "NEU: Kompakter Outdoor Vorhang-Melder",
            "usps": ["NEU", "Kompakt", "Dual-Tech", "Outdoor IP55"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fco_mini_jeweller_xl_d86bc61b07%402.jpg&1758023655",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller + Wings)",
                "range": "bis zu 1700m",
                "detection_range": "16 ft (ca. 5m)",
                "battery_life": "bis zu 3 Jahre",
                "operating_temp": "-13°F bis +140°F (-25°C bis +60°C)",
                "ip_rating": "IP55",
                "xortec_nr": "600810069/600810070",
                "hersteller_nr": "CO.M.J.BL/CO.M.J.WH"
            },
            "features": [
                {"name": "Kompakte Bauweise", "description": "Kleinere Größe für unauffällige Montage"},
                {"name": "Dual-Technologie", "description": "PIR + K-band Mikrowelle"},
                {"name": "2 Erkennungsmodi", "description": "Main und Pet Mode"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "CurtainCam Outdoor HighMount (PhOD) Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless dual-technology curtain motion detector with extended photo verification possibilities. For outdoor installation at a height of 2-4 m",
            "short_description": "NEU: Vorhang-Melder mit Kamera (2-4m Höhe)",
            "usps": ["NEU", "2-4m Montagehöhe", "Foto-Verifikation", "Vorhang-Schutz"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fcurtaincamoutdoor_phod_j_xl_db29859dc6%402.jpg&1761136204",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller + Wings)",
                "range": "bis zu 1700m",
                "detection_range": "49 ft (ca. 15m)",
                "battery_life": "bis zu 3 Jahre",
                "operating_temp": "-13°F bis +140°F (-25°C bis +60°C)",
                "ip_rating": "IP55",
                "xortec_nr": "600810071/600810072",
                "hersteller_nr": "CC.OHMP.J.BL/CC.OHMP.J.WH"
            },
            "features": [
                {"name": "Schmaler Erfassungswinkel", "description": "7° horizontal für präzise Perimeter-Überwachung"},
                {"name": "Foto-Verifikation", "description": "8 Foto-Verifikationstypen inkl. Pre-Alarm"},
                {"name": "HDR Technologie", "description": "Klare Fotos auch bei schwierigen Lichtverhältnissen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION BASELINE - KEYPADS (ADDITIONAL)
        # ========================================================================
        {
            "name": "KeyPad Outdoor Jeweller",
            "category": "keypads",
            "product_line": "intrusion_baseline",
            "description": "Keypad for outdoor and indoor use, featuring authentication via smartphones, Pass, Tag, and codes",
            "short_description": "NEU: Outdoor-Tastatur für Außeneinsatz",
            "usps": ["NEU", "Outdoor IP54", "Smartphone-Auth", "RFID"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_outdoor_jeweller_xl_0e3f5ac928%402.jpg&1716796181",
            "colors": ["Black", "White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 3.5 Jahre",
                "operating_temp": "-25°C bis +60°C",
                "ip_rating": "IP54",
                "xortec_nr": "600810073/600810074",
                "hersteller_nr": "KP.O.J.BL/KP.O.J.WH"
            },
            "features": [
                {"name": "Outdoor-fähig", "description": "IP54 Schutz für Außenmontage"},
                {"name": "Smartphone-Authentifizierung", "description": "DESFire-kompatible NFC-Karten"},
                {"name": "Vielfältige Auth-Methoden", "description": "Code, Pass, Tag, Smartphone"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION BASELINE - VOICE MODULE
        # ========================================================================
        {
            "name": "SpeakerPhone Jeweller",
            "category": "voice_modules",
            "product_line": "intrusion_baseline",
            "description": "Wireless voice module for alarm verification by monitoring or security companies for filtering false alarms",
            "short_description": "NEU: Voice-Modul zur Alarmverifikation",
            "usps": ["NEU", "Zwei-Wege-Audio", "Alarmverifikation", "VoRF Protokoll"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fspeakerphone_jeweller_xl_7e8c5a9d32%402.jpg&1716796195",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller + VoRF)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 2 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810075",
                "hersteller_nr": "SP.J.WH"
            },
            "features": [
                {"name": "Zwei-Wege-Audio", "description": "Kommunikation zwischen Alarmzentrale und Objekt"},
                {"name": "VoRF Protokoll", "description": "Ajax proprietäres Audio-Streaming-Protokoll"},
                {"name": "Alarmverifikation", "description": "Reduziert Fehlalarme durch Sprachüberprüfung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # COMFORT & AUTOMATION - INTEGRATION MODULES (ADDITIONAL)
        # ========================================================================
        {
            "name": "vhfBridge Jeweller",
            "category": "integration_modules",
            "product_line": "comfort_automation",
            "description": "Wireless module for connecting an Ajax system to third-party VHF transmitters",
            "short_description": "VHF-Integrationsmodul für Fernübertragung",
            "usps": ["VHF-Integration", "Bis zu 75h Batterie", "8 Ausgänge", "Große Reichweite"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fvhf_bridge_xl_e2702205cc%402.jpg&1755765199",
            "colors": ["White"],
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1800m",
                "outputs": "8 Transistor-Ausgänge",
                "operating_temp": "-10°C bis +40°C",
                "backup_battery": "7 Ah (optional)",
                "xortec_nr": "600811013",
                "hersteller_nr": "VHF.B.J"
            },
            "features": [
                {"name": "VHF-Kommunikation", "description": "Verbindet Ajax mit VHF-Transmittern für große Reichweiten"},
                {"name": "8 konfigurierbare Ausgänge", "description": "Flexible Ereigniszuordnung"},
                {"name": "Bis zu 75h Autonomie", "description": "Mit 7 Ah Backup-Batterie"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # POWER SUPPLIES
        # ========================================================================
        {
            "name": "12V PSU for Hub/Hub Plus/ReX",
            "category": "power_supplies",
            "product_line": "intrusion_baseline",
            "description": "A power supply unit, connecting Hub/Hub Plus control panels and ReX radio signal range extender to low-voltage power sources",
            "short_description": "12V Netzteil für Hub/ReX",
            "usps": ["12V Betrieb", "Für mobile Einsätze", "Batteriebetrieb möglich", "Kompakt"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fpsu_12v_hub_plus_xl_155bff7118%402.jpg&1755765055",
            "colors": ["White"],
            "specifications": {
                "voltage": "12V DC",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600811014",
                "hersteller_nr": "12V.PSU"
            },
            "features": [
                {"name": "12V Betrieb", "description": "Ermöglicht Betrieb mit Autobatterie oder Solaranlagen"},
                {"name": "Mobile Einsätze", "description": "Ideal für Wohnmobile, Yachten, Baustellen"},
                {"name": "Einfache Installation", "description": "Ersetzt das Standard-Netzteil im Hub"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller"],
            "accessories": ["Terminal Adapter"]
        },
        {
            "name": "6V PSU (type A) for Hub 2/Hub 2 Plus/ReX",
            "category": "power_supplies",
            "product_line": "intrusion_baseline",
            "description": "Power supply unit for operation of the device from portable battery. With an alternative 6 V power supply, hub can operate from an external battery for years",
            "short_description": "6V Netzteil für Batteriebetrieb",
            "usps": ["6V Betrieb", "Jahrelanger Betrieb", "Portable Batterien", "Netzunabhängig"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fpsu_6v_xl_e2d789457a%402.jpg&1717581250",
            "colors": ["White"],
            "specifications": {
                "voltage": "6V DC",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600811015",
                "hersteller_nr": "6V.H2R2.Y"
            },
            "features": [
                {"name": "Batteriebetrieb", "description": "Betrieb mit externen Batterien für jahrelangen Einsatz"},
                {"name": "Netzunabhängig", "description": "Ideal für Objekte ohne Stromversorgung"},
                {"name": "Schützt leerstehende Immobilien", "description": "Perfekt für Baustellenüberwachung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller"],
            "accessories": ["Terminal Adapter"]
        },
        {
            "name": "12-24V PSU (type A) for Hub 2/ReX 2",
            "category": "power_supplies",
            "product_line": "intrusion_baseline",
            "description": "Power supply unit for the device operation on a low-voltage power source. Ideal for trailers, yachts, and warehouses",
            "short_description": "12-24V Netzteil für Niederspannung",
            "usps": ["12-24V Betrieb", "Mobile Einsätze", "Fahrzeuge & Yachten", "Flexibel"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fpsu_12_type_a_xl_9a7028a264%402.jpg&1717766385",
            "colors": ["White"],
            "specifications": {
                "voltage": "12-24V DC",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600811016",
                "hersteller_nr": "24V.H2R2.Y"
            },
            "features": [
                {"name": "12-24V Betrieb", "description": "Flexibler Einsatz mit verschiedenen Spannungsquellen"},
                {"name": "Mobile Sicherheit", "description": "Ideal für Wohnmobile, LKW und Yachten"},
                {"name": "Lagerh allen", "description": "Perfekt für Objekte mit instabiler Stromversorgung"}
            ],
            "compatible_hubs": ["Hub 2 (2G) Jeweller", "Hub 2 (4G) Jeweller"],
            "accessories": ["Terminal Adapter"]
        },

        # ========================================================================
        # CASES / GEHÄUSE
        # ========================================================================
        {
            "name": "Case A (106)",
            "category": "cases",
            "product_line": "intrusion_superior",
            "description": "Casing for secure wired connection of one Ajax device. Dimensions: 106 × 168 × 56 mm",
            "short_description": "Gehäuse für 1 Ajax-Modul",
            "usps": ["1 Modul", "Kompakt", "Kabelmanagement", "Tamper-Schutz"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fcase_a_ca1bb298fb%402.jpg&1700147006",
            "colors": ["White", "Black"],
            "specifications": {
                "dimensions": "106 × 168 × 56 mm",
                "mounting_type": "Wall-mount",
                "ip_rating": "IP20",
                "xortec_nr": "600811020/600811021",
                "hersteller_nr": "CASE.A.WH/CASE.A.BL"
            },
            "features": [
                {"name": "1 Geräte-Slot", "description": "Für LineSplit, LineProtect oder MultiRelay"},
                {"name": "Kabelmanagement", "description": "Perforierte Zonen für organisierte Verkabelung"},
                {"name": "Tamper-Schutz", "description": "Integrierter Sabotageschutz"}
            ]
        },
        {
            "name": "Case B (175)",
            "category": "cases",
            "product_line": "intrusion_superior",
            "description": "Casing for secure wired connection of up to two Ajax devices. Dimensions: 175 × 225 × 57 mm",
            "short_description": "Gehäuse für bis zu 2 Ajax-Module",
            "usps": ["2 Module", "Flexibel", "Kabelmanagement", "Tamper-Schutz"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fcase_b_33af16f0b5%402.jpg&1700147006",
            "colors": ["White", "Black"],
            "specifications": {
                "dimensions": "175 × 225 × 57 mm",
                "device_slots": 2,
                "mounting_type": "Wall-mount",
                "ip_rating": "IP20",
                "xortec_nr": "600811022/600811023",
                "hersteller_nr": "CASE.B.WH/CASE.B.BL"
            },
            "features": [
                {"name": "2 Geräte-Slots", "description": "Für 2 Fibra-Module gleichzeitig"},
                {"name": "Organisiert", "description": "Professionelles Kabelmanagement"},
                {"name": "Erweiterbar", "description": "Flexible Gerätekombinationen"}
            ]
        },
        {
            "name": "Case C (260)",
            "category": "cases",
            "product_line": "intrusion_superior",
            "description": "Casing for one Ajax device and a 7 Ah battery. Dimensions: 260 × 195 × 93 mm",
            "short_description": "Gehäuse für 1 Modul + 7 Ah Batterie",
            "usps": ["1 Modul + Batterie", "7 Ah", "Backup-Power", "Kompakt"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fcase_c_b2b90717f1%402.jpg&1700147005",
            "colors": ["White", "Black"],
            "specifications": {
                "dimensions": "260 × 195 × 93 mm",
                "battery_capacity": "7 Ah",
                "device_slots": 1,
                "mounting_type": "Wall-mount",
                "ip_rating": "IP20",
                "xortec_nr": "600811024/600811025",
                "hersteller_nr": "CASE.C.WH/CASE.C.BL"
            },
            "features": [
                {"name": "Batterie-Slot", "description": "Platz für 7 Ah Backup-Batterie"},
                {"name": "LineSupply", "description": "Für LineSupply (45W oder 75W) Fibra"},
                {"name": "Backup-Power", "description": "Autonome Stromversorgung"}
            ]
        },
        {
            "name": "Case D (430)",
            "category": "cases",
            "product_line": "intrusion_superior",
            "description": "Casing for up to eight Ajax devices and two 18 Ah batteries. Dimensions: 430 × 400 × 133 mm",
            "short_description": "Gehäuse für bis zu 8 Module + 2x 18 Ah Batterien",
            "usps": ["Bis zu 8 Module", "2x 18 Ah", "Enterprise", "Maximum"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fcase_update_xl_093103f5d9%401.jpg&1696582570",
            "colors": ["White", "Black"],
            "specifications": {
                "dimensions": "430 × 400 × 133 mm",
                "device_slots": 8,
                "battery_capacity": "2x 18 Ah",
                "mounting_type": "Wall-mount",
                "ip_rating": "IP20",
                "xortec_nr": "600811026/600811027",
                "hersteller_nr": "CASE.D.WH/CASE.D.BL"
            },
            "features": [
                {"name": "Bis zu 8 Module", "description": "Maximale Kapazität für große Installationen"},
                {"name": "2x 18 Ah Batterien", "description": "Lange Backup-Zeit"},
                {"name": "Professionell", "description": "Für Enterprise-Projekte"}
            ]
        }
    ]


def get_ajax_categories_complete():
    return [
        {
            "id": "hubs",
            "name": "Hubs",
            "description": "Alarmzentralen",
            "icon": "hub"
        },
        {
            "id": "range_extenders",
            "name": "Reichweitenverlängerer",
            "description": "Funk-Repeater",
            "icon": "signal"
        },
        {
            "id": "motion_detectors",
            "name": "Bewegungsmelder", 
            "description": "PIR und Dual-Technologie Sensoren",
            "icon": "motion"
        },
        {
            "id": "opening_detectors",
            "name": "Öffnungsmelder",
            "description": "Tür- und Fenstersensoren",
            "icon": "door"
        },
        {
            "id": "glass_break_detectors",
            "name": "Glasbruchmelder",
            "description": "Akustische Glasbruchmelder",
            "icon": "glass"
        },
        {
            "id": "keypads",
            "name": "Tastaturen",
            "description": "Bedientastaturen und RFID",
            "icon": "keypad"
        },
        {
            "id": "buttons",
            "name": "Buttons & Fernbedienungen",
            "description": "Panik-Buttons und Key Fobs",
            "icon": "button"
        },
        {
            "id": "sirens",
            "name": "Sirenen",
            "description": "Innen- und Außensirenen",
            "icon": "siren"
        },
        {
            "id": "cameras",
            "name": "Kameras",
            "description": "Verkabelte IP-Sicherheitskameras",
            "icon": "camera"
        },
        {
            "id": "wifi_cameras", 
            "name": "Wi-Fi Kameras",
            "description": "Kabellose IP-Kameras",
            "icon": "wifi-camera"
        },
        {
            "id": "doorbells",
            "name": "Türklingeln",
            "description": "Video-Türklingeln",
            "icon": "doorbell"
        },
        {
            "id": "nvrs",
            "name": "NVRs",
            "description": "Netzwerk-Videorekorder",
            "icon": "nvr"
        },
        {
            "id": "fire_detectors",
            "name": "Brandmelder",
            "description": "Rauch-, Hitze- und CO-Melder",
            "icon": "fire"
        },
        {
            "id": "relays",
            "name": "Relais",
            "description": "Schaltrelais für Automation",
            "icon": "relay"
        },
        {
            "id": "sockets",
            "name": "Steckdosen",
            "description": "Smarte Steckdosen",
            "icon": "socket"
        },
        {
            "id": "leak_detectors",
            "name": "Wasserleckmelder",
            "description": "Wasserleck-Detektoren",
            "icon": "water"
        },
        {
            "id": "shutoff_valves",
            "name": "Absperrventile",
            "description": "Automatische Wasserabsperrventile",
            "icon": "valve"
        },
        {
            "id": "air_quality_detectors",
            "name": "Raumklima-Sensoren",
            "description": "Temperatur, Luftfeuchtigkeit, CO₂",
            "icon": "air"
        },
        {
            "id": "integration_modules",
            "name": "Integrationsmodule",
            "description": "Module zur Integration von Drittgeräten",
            "icon": "integration"
        },
        {
            "id": "light_switches",
            "name": "Lichtschalter",
            "description": "Smarte Touch-Lichtschalter",
            "icon": "light"
        },
        {
            "id": "voice_modules",
            "name": "Voice Module",
            "description": "Sprachmodule für Alarmverifikation",
            "icon": "microphone"
        },
        {
            "id": "power_supplies",
            "name": "Netzteile",
            "description": "Stromversorgungseinheiten",
            "icon": "power"
        },
        {
            "id": "cases",
            "name": "Gehäuse",
            "description": "Montagegehäuse für Ajax-Module",
            "icon": "box"
        }
    ]


def get_ajax_product_lines_complete():
    return [
        {
            "id": "intrusion_baseline",
            "name": "Intrusion - Baseline",
            "description": "Professionelle kabellose Geräte für Wohn- und Gewerbeobjekte",
            "features": ["Grade 2 EN 50131", "Jeweller-Protokoll", "Große Auswahl", "Einfache Installation"],
            "target_group": "Alle Ajax-Partner",
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbaseline_lg_bc7460aa05%402.jpg&1731779933"
        },
        {
            "id": "intrusion_superior",
            "name": "Intrusion - Superior",
            "description": "Hochprofessionelle kabellose und verdrahtete Geräte für höchste Ansprüche",
            "features": ["Grade 3 EN 50131", "Jeweller + Fibra", "Erweiterte Funktionen", "Nur für akkreditierte Partner"],
            "target_group": "Akkreditierte Ajax-Partner",
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_lg_7b3c7741db%402.jpg&1731780001"
        },
        {
            "id": "video_baseline",
            "name": "Video - Baseline",
            "description": "Wesentliche Videogeräte für alle Überwachungsanforderungen",
            "features": ["KI-gestützt", "Hybrid-Beleuchtung", "4K-Auflösung", "NDAA-konform"],
            "target_group": "Alle Ajax-Partner",
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fvideo_surveillance_lg_60f5f58bb5%402.jpg&1763473120"
        },
        {
            "id": "video_superior",
            "name": "Video - Superior", 
            "description": "Unkompromierende Überwachung für anspruchsvolle Projekte",
            "features": ["Erweiterte KI", "Robuste Hardware", "Professional Grade", "Nur für akkreditierte Partner"],
            "target_group": "Akkreditierte Ajax-Partner",
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_video_surveillance_lg_f004ac28bd%402.jpg&1763473037"
        },
        {
            "id": "en54",
            "name": "EN54 Fire & Life Safety",
            "description": "Brandschutz- und Lebensschutz-Systeme nach EN54",
            "features": ["EN54-zertifiziert", "Brandschutz", "Professionell", "Europäische Normen"],
            "target_group": "Zertifizierte Brandschutz-Partner",
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fproduct-categories%2Ffire-and-life-safety.lg.jpg&1751882727"
        },
        {
            "id": "comfort_automation",
            "name": "Comfort & Automation",
            "description": "Smart Home Automatisierungslösungen",
            "features": ["Smart Home", "Automatisierung", "Komfort", "Integration"],
            "target_group": "Alle Ajax-Partner",
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fcomfort_lg_North_America_47689d0854%402.jpg&1743597220"
        }
    ]


if __name__ == "__main__":
    products = get_ajax_products_complete()
    categories = get_ajax_categories_complete()
    product_lines = get_ajax_product_lines_complete()
    
    print(f"Anzahl Produkte: {len(products)}")
    print(f"Anzahl Kategorien: {len(categories)}")
    print(f"Anzahl Produktlinien: {len(product_lines)}")
    
    # Produktlinien zählen
    lines = {}
    for product in products:
        line = product['product_line']
        if line not in lines:
            lines[line] = 0
        lines[line] += 1
        
    print("\nProdukte pro Produktlinie:")
    for line, count in sorted(lines.items()):
        print(f"  {line}: {count}")
        
    # Kategorien zählen
    cats = {}
    for product in products:
        cat = product['category']
        if cat not in cats:
            cats[cat] = 0
        cats[cat] += 1
    
    print("\nProdukte pro Kategorie:")
    for cat, count in sorted(cats.items()):
        print(f"  {cat}: {count}")
    
    # Farboptionen
    color_count = sum(1 for p in products if 'colors' in p and len(p.get('colors', [])) > 1)
    print(f"\nProdukte mit Farboptionen: {color_count}")
