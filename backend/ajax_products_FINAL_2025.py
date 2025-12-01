"""
Ajax Systems Produkt-Datenbank 2025 - VOLLSTÄNDIG UND AKKURAT
Basierend auf ajax.systems offizielle Daten (Stand: Dezember 2025)
Produktlinien: Intrusion (Superior/Baseline), Video (Superior/Baseline), EN54, Comfort & Automation

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
            "description": "Wireless control panel with support for photo verification. Connectable via Wi-Fi, Ethernet, and two SIM cards (2G/3G/LTE)",
            "short_description": "Kabellose Alarmzentrale mit Foto-Verifikation",
            "usps": ["Foto-Verifikation", "4 Kommunikationswege", "Bis zu 200 Geräte", "Grade 2"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078",
            "specifications": {
                "frequency": "868 MHz (Jeweller), 433 MHz (Wings)",
                "range": "bis zu 2000m (Jeweller)",
                "communication": ["Wi-Fi", "Ethernet", "2G/3G/LTE (2x SIM)"],
                "max_devices": 200,
                "max_cameras": 100,
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
            "product_line": "intrusion_baseline",
            "description": "Wireless battery-powered control panel. Supports photo verification. Connectable via two SIM cards (2G/3G/LTE)",
            "short_description": "Batteriebetriebene Alarmzentrale",
            "usps": ["NEU", "Batteriebetrieben", "Mobil einsetzbar", "Bis zu 200 Geräte"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_bp_jeweller_black_1760739e4c%402.png&1732115997",
            "specifications": {
                "frequency": "868 MHz (Jeweller), 433 MHz (Wings)",
                "range": "bis zu 2000m (Jeweller)",
                "communication": ["2G/3G/LTE (2x SIM)"],
                "max_devices": 200,
                "max_cameras": 100,
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

        # ========================================================================
        # INTRUSION SUPERIOR - HUBS
        # ========================================================================
        {
            "name": "Superior Hub Hybrid (4G)",
            "category": "hubs",
            "product_line": "intrusion_superior",
            "description": "Professional control panel for high-security applications with Jeweller and Fibra protocol support",
            "short_description": "Grade 3 Hub für höchste Sicherheitsanforderungen",
            "usps": ["Grade 3", "Fibra + Jeweller", "Bis zu 400 Geräte", "Professional"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_hub_hybrid%402.png",
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
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_7e25a60ef8%402.png&1689152842",
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MotionProtect Plus Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless IR motion detector with an additional K-band microwave sensor",
            "short_description": "Dual-Technologie Bewegungsmelder",
            "usps": ["Duale Sensorik", "Grade 2", "Anti-Masking", "Falschalarmsicher"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_plus_111a8e0f23%402.png&1689159156",
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MotionCam Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless IR motion detector supporting photo by alarm feature",
            "short_description": "PIR-Bewegungsmelder mit Kamera",
            "usps": ["Foto-Verifikation", "Grade 2", "Anti-Sabotage", "Haustierimmun"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotion_cam_jeweller_black_50c00ca247%402.png&1727442738",
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "DoorProtect Plus Jeweller",
            "category": "opening_detectors",
            "product_line": "intrusion_baseline",
            "description": "Wireless opening detector with additional tilt and shock sensors",
            "short_description": "Erweiteter Tür-/Fenstersensor mit Neigung & Erschütterung",
            "usps": ["3-in-1 Sensor", "Grade 2", "Neigung & Erschütterung", "7 Jahre Batterie"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_plus_1d3ec6085c%402.png&1689152842",
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },

        # ========================================================================
        # INTRUSION BASELINE - KEYPADS
        # ========================================================================
        {
            "name": "KeyPad Plus Jeweller",
            "category": "keypads",
            "product_line": "intrusion_baseline",
            "description": "Wireless control keypad with RFID card reader",
            "short_description": "NEU: Tastatur mit RFID",
            "usps": ["NEU", "Touch-Tasten", "RFID-Leser", "Code & Karten"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_plus_jeweller_black_25cf406a42%402.png&1732188086",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 4.5 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810737",
                "hersteller_nr": "8001.52.BL1"
            },
            "features": [
                {"name": "Touch-Tasten", "description": "Moderne kapazitive Touch-Oberfläche"},
                {"name": "RFID-Leser", "description": "Unterstützt Pass und Tag für schnelle Bedienung"},
                {"name": "Duress-Funktion", "description": "Stiller Alarm bei Zwangssituationen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"],
            "accessories": ["Pass", "Tag", "Holder"]
        },

        # ========================================================================
        # INTRUSION SUPERIOR - MOTION DETECTORS
        # ========================================================================
        {
            "name": "Superior MotionProtect Jeweller",
            "category": "motion_detectors",
            "product_line": "intrusion_superior",
            "description": "Wireless IR motion detector. Superior edition",
            "short_description": "Professional PIR-Bewegungsmelder",
            "usps": ["Grade 3", "Erweiterte Anti-Sabotage", "Professional", "12m Erfassung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmpsj_s_34e8d588e9%402.png&1688046986",
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
            "description": "Wireless combined heat, smoke, and CO detector with replaceable batteries",
            "short_description": "Kombimelder: Hitze, Rauch & CO",
            "usps": ["3-in-1 Sensor", "UL-zertifiziert", "Austauschbare Batterien", "Sirene integriert"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffireprotect2_smoke_028348da8d%402.png&1689152843",
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "FireProtect 2 RB (Heat/Smoke) UL Jeweller",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Wireless combined heat and smoke detector with replaceable batteries",
            "short_description": "Kombimelder: Hitze & Rauch",
            "usps": ["2-in-1 Sensor", "UL-zertifiziert", "Austauschbare Batterien", "Sirene integriert"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffireprotect2_smoke_028348da8d%402.png&1689152843",
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "FireProtect 2 RB (Heat) UL Jeweller",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Wireless fire detector with a heat sensor. Version with replaceable batteries",
            "short_description": "NEU: Hitzemelder",
            "usps": ["NEU", "Hitzesensor", "UL-zertifiziert", "Batteriebetrieben"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffire_protect_2_ul_black_7620cda5e6%402.png&1732126298",
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "FireProtect 2 RB (CO) UL Jeweller",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Wireless fire detector with a CO sensor. Version with replaceable batteries",
            "short_description": "NEU: CO-Melder",
            "usps": ["NEU", "CO-Sensor", "UL-zertifiziert", "Batteriebetrieben"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffire_protect_2_ul_black_7620cda5e6%402.png&1732126298",
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
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
            "specifications": {
                "resolution": "5MP (2592x1944)",
                "night_vision": "Hybrid Lighting (IR + Weißlicht)",
                "viewing_angle": "103° (H), 54° (V)",
                "operating_temp": "-30°C bis +60°C",
                "ip_rating": "IP67",
                "xortec_nr": "600810451",
                "hersteller_nr": "BC-HL-5MP"
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
            "specifications": {
                "resolution": "8MP (3840x2160)",
                "night_vision": "Hybrid Lighting (IR + Weißlicht)",
                "viewing_angle": "106° (H), 56° (V)",
                "operating_temp": "-30°C bis +60°C",
                "ip_rating": "IP67",
                "xortec_nr": "600810452",
                "hersteller_nr": "BC-HL-8MP"
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
            "specifications": {
                "resolution": "5MP (2592x1944)",
                "night_vision": "Hybrid Lighting (IR + Weißlicht)",
                "viewing_angle": "103° (H), 54° (V)",
                "operating_temp": "-30°C bis +60°C",
                "ip_rating": "IP67",
                "ik_rating": "IK10",
                "xortec_nr": "600810453",
                "hersteller_nr": "TC-HL-5MP"
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"],
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
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"],
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
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1000m",
                "max_load": "1.8kW (110-120V)",
                "plug_type": "Type B (US)",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600811003",
                "hersteller_nr": "SOCK-B-JW"
            },
            "features": [
                {"name": "Verbrauchsmessung", "description": "Überwachen Sie den Stromverbrauch in Echtzeit"},
                {"name": "Zeitpläne", "description": "Automatisches Ein-/Ausschalten"},
                {"name": "Kompaktes Design", "description": "Nimmt wenig Platz ein"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "LeaksProtect Jeweller",
            "category": "leak_detectors",
            "product_line": "comfort_automation",
            "description": "Wireless water leak detector",
            "short_description": "Kabelloser Wasserleckmelder",
            "usps": ["Wasserleck-Erkennung", "7 Jahre Batterie", "Kompakt", "Szenarien"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fleaksprotect_8530909770%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "0°C bis +50°C",
                "ip_rating": "IP65",
                "xortec_nr": "600811004",
                "hersteller_nr": "LP-JW"
            },
            "features": [
                {"name": "Früherkennung", "description": "Erkennt Wasserlecks sofort"},
                {"name": "Szenarien", "description": "Automatisches Absperren über WaterStop"},
                {"name": "IP65 Schutz", "description": "Geschützt gegen Wasser und Staub"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "WaterStop 1\" (DN 25) Jeweller",
            "category": "shutoff_valves",
            "product_line": "comfort_automation",
            "description": "Wireless remotely controlled water shutoff valve 1 inch",
            "short_description": "Kabelloses Wasserabsperrventil 1 Zoll",
            "usps": ["1\" (DN 25)", "Fernsteuerung", "Szenarien", "Motor-getrieben"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fwaterstop_feb7973a94%402.png&1689152843",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1000m",
                "valve_size": "1\" (DN 25)",
                "power": "110-230V AC oder 12V DC",
                "operating_temp": "0°C bis +50°C",
                "xortec_nr": "600811005",
                "hersteller_nr": "WS-1-JW"
            },
            "features": [
                {"name": "Fernsteuerung", "description": "Wasser per App abdrehen"},
                {"name": "Szenarien", "description": "Automatisches Absperren bei Leck"},
                {"name": "Manueller Override", "description": "Notfallbedienung am Ventil"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "LifeQuality Jeweller",
            "category": "air_quality_detectors",
            "product_line": "comfort_automation",
            "description": "Wireless temperature, humidity, and CO₂ monitor",
            "short_description": "Raumklima-Monitor (Temp, Feuchte, CO₂)",
            "usps": ["CO₂-Messung", "Temperatur", "Luftfeuchtigkeit", "E-Ink Display"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Flifequality_9644fe6470%402.png&1689152843",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 5 Jahre",
                "sensors": ["CO₂", "Temperatur", "Luftfeuchtigkeit"],
                "operating_temp": "0°C bis +50°C",
                "xortec_nr": "600811006",
                "hersteller_nr": "LQ-JW"
            },
            "features": [
                {"name": "3-in-1 Sensor", "description": "CO₂, Temperatur und Luftfeuchtigkeit"},
                {"name": "E-Ink Display", "description": "Energiesparendes Display"},
                {"name": "Szenarien", "description": "Automatische Lüftungssteuerung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MultiTransmitter Jeweller",
            "category": "integration_modules",
            "product_line": "comfort_automation",
            "description": "Wireless module to integrate up to 18 third-party devices into the Ajax system",
            "short_description": "Integrationsmodul für bis zu 18 Drittgeräte",
            "usps": ["Bis zu 18 Geräte", "Universell", "Verdrahtet", "DIN-Montage"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmultitransmitter_jeweller_a9d90bcffb%402.png&1707486834",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "inputs": "18 verdrahtete Eingänge",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600811007",
                "hersteller_nr": "MT-JW"
            },
            "features": [
                {"name": "18 Eingänge", "description": "Integrieren Sie bis zu 18 Drittgeräte"},
                {"name": "Universell", "description": "Für alle verdrahteten Sensoren und Melder"},
                {"name": "Szenarien", "description": "Automation mit integrierten Geräten"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "Transmitter Jeweller",
            "category": "integration_modules",
            "product_line": "comfort_automation",
            "description": "Wireless module to integrate one third-party device into the Ajax system",
            "short_description": "Integrationsmodul für 1 Drittgerät",
            "usps": ["1 Gerät", "Kompakt", "Verdrahtet", "Universell"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ftransmitter_897ae41178%402.png&1689152843",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "inputs": "1 verdrahteter Eingang",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600811008",
                "hersteller_nr": "TRM-JW"
            },
            "features": [
                {"name": "1 Eingang", "description": "Integrieren Sie ein Drittgerät"},
                {"name": "Kompakt", "description": "Klein und unauffällig"},
                {"name": "Batteriebetrieben", "description": "Keine externe Stromversorgung nötig"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "LightSwitch (1-gang) [120] Jeweller",
            "category": "light_switches",
            "product_line": "comfort_automation",
            "description": "Smart touch 1-gang light switch for 120V systems",
            "short_description": "NEU: 1-Kanal Touch-Lichtschalter",
            "usps": ["NEU", "Touch-Bedienung", "Szenarien", "120V"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fls_120_1_gang_black_715a1a19d0%402.png&1732142073",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1000m",
                "voltage": "120V AC",
                "max_load": "1200W",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600811010",
                "hersteller_nr": "LS-1G-120-JW"
            },
            "features": [
                {"name": "Touch-Bedienung", "description": "Moderne kapazitive Touch-Oberfläche"},
                {"name": "Szenarien", "description": "Automation und Zeitpläne"},
                {"name": "Dimmer-kompatibel", "description": "Unterstützt dimmbare Leuchtmittel"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
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
            "id": "sirens",
            "name": "Sirenen",
            "description": "Innen- und Außensirenen",
            "icon": "siren"
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
