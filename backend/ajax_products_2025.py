"""
Ajax Systems Produkt-Datenbank 2025 - Komplett aktualisiert basierend auf ajax.systems
Alle Produktlinien: Superior, Baseline, Video Surveillance, Fire & Life Safety, Comfort & Automation
"""

def get_ajax_products_2025():
    return [
        # ================== BASELINE HUBS ==================
        {
            "name": "Hub 2 Plus Jeweller",
            "category": "hubs",
            "product_line": "baseline",
            "description": "Kabellose Alarmzentrale mit Unterstützung für Foto-Verifikation. Verbindung über Wi-Fi, Ethernet und zwei SIM-Karten (2G/3G/LTE)",
            "short_description": "Hauptzentrale mit 4 Kommunikationswegen",
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
            "short_description": "Batteriebetriebene mobile Zentrale",
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
            "name": "MotionProtect Plus Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "Kabelloser IR-Bewegungsmelder mit zusätzlichem K-Band-Mikrowellensensor",
            "short_description": "Dual-Technologie Bewegungsmelder",
            "usps": ["Duale Sensorik", "Grade 2", "Anti-Masking", "Falschalarmsicher"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_plus_111a8e0f23%402.png&1689159156",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
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
        },
        {
            "name": "Curtain Outdoor Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "Kabelloser Dual-Technologie Vorhang-Bewegungsmelder für Innen- und Außenbereich",
            "short_description": "NEU: Outdoor Vorhang-Bewegungsmelder",
            "usps": ["NEU", "Outdoor", "Dual-Technologie", "15m Reichweite"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsurtain_outdoor_jeweller_c9b2b1bf49%402.png&1731920177",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-25°C bis +60°C",
                "ip_rating": "IP65",
                "xortec_nr": "600810745/600810746",
                "hersteller_nr": "8015.52.BL1/8015.52.WH1"
            },
            "features": [
                {"name": "Dual-Technologie", "description": "PIR + Mikrowellen für höchste Zuverlässigkeit"},
                {"name": "Wetterfest", "description": "IP65 Schutz für Außenbereich"},
                {"name": "Anti-Falschalarm", "description": "Intelligente Algorithmen gegen Wetteralarme"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "MotionCam Outdoor HighMount (PhOD) Jeweller",
            "category": "motion_detectors", 
            "product_line": "baseline",
            "description": "Kabelloser PIR-Bewegungsmelder mit erweiterten Foto-Verifikationsmöglichkeiten. Für Außeninstallation in 2-4 m Höhe",
            "short_description": "NEU: Outdoor High-Mount PIR mit Foto",
            "usps": ["NEU", "High-Mount 2-4m", "Erweiterte Foto-Verifikation", "Professional"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmc_outdoor_high_mount_phod_jeweller_ac5a405dd3%402.png&1732142253",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 2 Jahre",
                "operating_temp": "-25°C bis +60°C",
                "ip_rating": "IP65",
                "xortec_nr": "600810747/600810748",
                "hersteller_nr": "8028.52.BL1/8028.52.WH1"
            },
            "features": [
                {"name": "High-Mount Installation", "description": "Optimiert für Montage in 2-4 Meter Höhe"},
                {"name": "Erweiterte Foto-Verifikation", "description": "Hochauflösende Bilder aus großer Höhe"},
                {"name": "Professional Grade", "description": "Für anspruchsvolle Perimeter-Überwachung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },

        # ================== BASELINE ÖFFNUNGSMELDER ==================
        {
            "name": "DoorProtect Jeweller",
            "category": "opening_detectors", 
            "product_line": "baseline",
            "description": "Kabelloser Öffnungsmelder mit Reed-Schalter",
            "short_description": "Standard Öffnungsmelder",
            "usps": ["Reed-Schalter", "7 Jahre Batterie", "Compact Design", "Grade 2"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_f565be9860%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810045/600810046",
                "hersteller_nr": "7063.52.BL1/7063.52.WH1"
            },
            "features": [
                {"name": "Reed-Schalter", "description": "Zuverlässige magnetische Erkennung"},
                {"name": "Kompakt", "description": "Unauffällig und einfach zu installieren"},
                {"name": "Anti-Sabotage", "description": "Schutz gegen Manipulation"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "DoorProtect Plus Jeweller",
            "category": "opening_detectors",
            "product_line": "baseline", 
            "description": "Kabelloser kombinierter Öffnungs-, Erschütterungs- und Neigungsmelder mit Reed-Schalter und Beschleunigungssensor",
            "short_description": "Multifunktions-Öffnungsmelder",
            "usps": ["3-in-1 Funktion", "Reed + Accelerometer", "Erschütterung + Neigung", "Grade 2"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_f565be9860%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810047/600810048",
                "hersteller_nr": "7064.52.BL1/7064.52.WH1"
            },
            "features": [
                {"name": "Triple-Funktion", "description": "Öffnung + Erschütterung + Neigung in einem Gerät"},
                {"name": "Accelerometer", "description": "Hochsensitive Erschütterungserkennung"},
                {"name": "Adjustierbar", "description": "Einstellbare Empfindlichkeit"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"]
        },

        # ================== BASELINE TASTATUREN ==================
        {
            "name": "KeyPad TouchScreen Jeweller",
            "category": "keypads",
            "product_line": "baseline",
            "description": "Kabellose Tastatur mit Touchscreen, die Authentifizierung mit Smartphones, Pass, Tag und Codes unterstützt",
            "short_description": "NEU: Touchscreen-Tastatur mit Smartphone-Auth",
            "usps": ["NEU", "Touchscreen", "Smartphone-Auth", "Pass & Tag"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_touchscreen_4a49692df5%402.png&1691157817",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m",
                "battery_life": "bis zu 4 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810740/600810741",
                "hersteller_nr": "8008.52.BL1/8008.52.WH1"
            },
            "features": [
                {"name": "Touchscreen", "description": "Intuitives Touch-Display für einfache Bedienung"},
                {"name": "Multi-Authentifizierung", "description": "Smartphone, RFID-Tags, Karten und Codes"},
                {"name": "Live-Ereignisse", "description": "Aktuelle Systemereignisse auf dem Display"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"],
            "accessories": ["Pass (RFID-Karte)", "Tag (RFID-Anhänger)"]
        },
        {
            "name": "KeyPad Plus Jeweller",
            "category": "keypads",
            "product_line": "baseline",
            "description": "Kabellose Touch-Tastatur mit Unterstützung für verschlüsselte kontaktlose Karten und Schlüsselanhänger",
            "short_description": "Touch-Tastatur mit RFID",
            "usps": ["Touch-Tastatur", "RFID Cards", "Verschlüsselt", "Grade 2"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_plus_cb76223961%402.png&1689152843",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m", 
                "battery_life": "bis zu 4 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810051/600810052",
                "hersteller_nr": "8007.52.BL1/8007.52.WH1"
            },
            "features": [
                {"name": "Touch-Bedienung", "description": "Kapazitive Touch-Oberfläche ohne mechanische Tasten"},
                {"name": "RFID-Unterstützung", "description": "Pass-Karten und Tag-Anhänger"},
                {"name": "Verschlüsselung", "description": "Sichere Datenübertragung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub BP Jeweller"],
            "accessories": ["Pass (RFID-Karte)", "Tag (RFID-Anhänger)"]
        },

        # ================== VIDEO SURVEILLANCE - WIRED CAMERAS ==================
        {
            "name": "BulletCam HL (5 Mp/2.8 mm)",
            "category": "cameras",
            "product_line": "video",
            "description": "Verdrahtete KI-gestützte Sicherheits-IP-Kamera mit 110° Blickwinkel, Hybrid-Beleuchtung, TrueWDR, Mikrofon und PoE/12V. Für Außen- und Innenbereich",
            "short_description": "NEU: KI-Kamera mit Hybrid-Beleuchtung",
            "usps": ["NEU", "Hybrid-Beleuchtung", "KI-Powered", "5MP/110°"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbulletcam_hl_black_d032cbd5e2%402.png&1755086269",
            "specifications": {
                "resolution": "5 Megapixel",
                "lens": "2.8mm (110° Blickwinkel)",
                "illumination": "Hybrid (IR + White Light)",
                "power": "PoE/12V",
                "operating_temp": "-40°C bis +60°C",
                "ip_rating": "IP67",
                "xortec_nr": "600810765",
                "hersteller_nr": "BC-HL-5MP-2.8"
            },
            "features": [
                {"name": "Hybrid-Beleuchtung", "description": "IR-Nachtsicht + Weißlicht für Farbaufnahmen bei Nacht"},
                {"name": "KI-Analyse", "description": "Intelligente Objekterkennung und Klassifizierung"},
                {"name": "TrueWDR", "description": "Dynamischer Bereich für schwierige Lichtverhältnisse"}
            ],
            "compatible_nvrs": ["NVR (8-ch)", "NVR (16-ch)", "NVR DC (8-ch)", "NVR DC (16-ch)"],
            "accessories": ["JunctionBox (118×59)", "MountCam A1", "MountCam A2", "MountCam B1", "MountCam B2"]
        },
        {
            "name": "BulletCam HL (8 Mp/2.8 mm)",
            "category": "cameras",
            "product_line": "video",
            "description": "Verdrahtete KI-gestützte Sicherheits-IP-Kamera mit 110° Blickwinkel, Hybrid-Beleuchtung, TrueWDR, Mikrofon und PoE/12V. Für Außen- und Innenbereich",
            "short_description": "NEU: 8MP KI-Kamera mit Hybrid-Beleuchtung",
            "usps": ["NEU", "8MP Ultra HD", "Hybrid-Beleuchtung", "KI-Powered"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbulletcam_hl_black_d032cbd5e2%402.png&1755086269",
            "specifications": {
                "resolution": "8 Megapixel (4K)",
                "lens": "2.8mm (110° Blickwinkel)",
                "illumination": "Hybrid (IR + White Light)",
                "power": "PoE/12V",
                "operating_temp": "-40°C bis +60°C",
                "ip_rating": "IP67",
                "xortec_nr": "600810766",
                "hersteller_nr": "BC-HL-8MP-2.8"
            },
            "features": [
                {"name": "4K Ultra HD", "description": "8 Megapixel Auflösung für gestochen scharfe Bilder"},
                {"name": "Hybrid-Beleuchtung", "description": "IR-Nachtsicht + Weißlicht für Farbaufnahmen bei Nacht"},
                {"name": "KI-Analyse", "description": "Erweiterte Objekterkennung mit 4K-Details"}
            ],
            "compatible_nvrs": ["NVR (8-ch)", "NVR (16-ch)", "NVR DC (8-ch)", "NVR DC (16-ch)"],
            "accessories": ["JunctionBox (118×59)", "MountCam A1", "MountCam A2", "MountCam B1", "MountCam B2"]
        },
        {
            "name": "DomeCam Mini HL (5 Mp/2.8 mm)",
            "category": "cameras",
            "product_line": "video",
            "description": "Verdrahtete KI-gestützte Sicherheits-IP-Kamera mit 110° Blickwinkel, Hybrid-Beleuchtung, TrueWDR, Mikrofon und PoE/12V. Für Außen- und Innenbereich",
            "short_description": "NEU: Kompakte Dome-Kamera mit Hybrid-Beleuchtung",
            "usps": ["NEU", "Kompaktes Design", "Hybrid-Beleuchtung", "Vandalismusschutz"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdomecam_mini_hl_black_5655907271%402.png&1755086152",
            "specifications": {
                "resolution": "5 Megapixel",
                "lens": "2.8mm (110° Blickwinkel)",
                "illumination": "Hybrid (IR + White Light)",
                "power": "PoE/12V",
                "operating_temp": "-40°C bis +60°C",
                "ip_rating": "IP67",
                "xortec_nr": "600810767",
                "hersteller_nr": "DC-Mini-HL-5MP-2.8"
            },
            "features": [
                {"name": "Vandalismusschutz", "description": "Robuste Dome-Konstruktion gegen Manipulation"},
                {"name": "Hybrid-Beleuchtung", "description": "IR + Weißlicht für Tag/Nacht-Aufnahmen"},
                {"name": "Kompakt", "description": "Unauffälliges Design für diskrete Überwachung"}
            ],
            "compatible_nvrs": ["NVR (8-ch)", "NVR (16-ch)", "NVR DC (8-ch)", "NVR DC (16-ch)"],
            "accessories": ["JunctionBox (118×59)", "MountCam A1", "MountCam A2", "MountCam B1", "MountCam B2"]
        },
        {
            "name": "TurretCam HL (5 Mp/2.8 mm)",
            "category": "cameras",
            "product_line": "video",
            "description": "Verdrahtete KI-gestützte Sicherheits-IP-Kamera mit 110° Blickwinkel, Hybrid-Beleuchtung, TrueWDR, Mikrofon und PoE/12V. Für Außen- und Innenbereich",
            "short_description": "NEU: Turret-Kamera mit Hybrid-Beleuchtung",
            "usps": ["NEU", "Turret-Design", "Hybrid-Beleuchtung", "Flexible Montage"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fturretcam_hl_black_7720ca22b3%402.png&1755086269",
            "specifications": {
                "resolution": "5 Megapixel",
                "lens": "2.8mm (110° Blickwinkel)",
                "illumination": "Hybrid (IR + White Light)",
                "power": "PoE/12V",
                "operating_temp": "-40°C bis +60°C",
                "ip_rating": "IP67",
                "xortec_nr": "600810768",
                "hersteller_nr": "TC-HL-5MP-2.8"
            },
            "features": [
                {"name": "Turret-Design", "description": "Flexible Positionierung in jeden Winkel"},
                {"name": "Hybrid-Beleuchtung", "description": "IR + Weißlicht für optimale Nachtsicht"},
                {"name": "Vielseitige Montage", "description": "Anpassbar an verschiedene Überwachungsbedürfnisse"}
            ],
            "compatible_nvrs": ["NVR (8-ch)", "NVR (16-ch)", "NVR DC (8-ch)", "NVR DC (16-ch)"],
            "accessories": ["JunctionBox (118×59)", "MountCam A1", "MountCam A2", "MountCam B1", "MountCam B2"]
        },

        # ================== VIDEO SURVEILLANCE - WI-FI CAMERAS ==================
        {
            "name": "IndoorCam",
            "category": "wifi_cameras",
            "product_line": "video",
            "description": "Indoor Wi-Fi Sicherheitskamera mit PIR-Bewegungssensor und integrierter KI",
            "short_description": "NEU: Wi-Fi Indoor-Kamera mit PIR",
            "usps": ["NEU", "Wi-Fi", "PIR-Sensor", "KI-Analyse"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Findoorcam_black_e562685ad8%402.png&1732114433",
            "specifications": {
                "resolution": "2 Megapixel (1080p)",
                "connectivity": "Wi-Fi 802.11n",
                "detection": "PIR + Video Motion Detection",
                "power": "AC Adapter",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600810769",
                "hersteller_nr": "IC-WiFi-2MP"
            },
            "features": [
                {"name": "PIR + Video", "description": "Dual-Bewegungserkennung für höchste Genauigkeit"},
                {"name": "Wi-Fi Konnektivität", "description": "Einfache Installation ohne Verkabelung"},
                {"name": "KI-Objekterkennung", "description": "Unterscheidet Personen von anderen Objekten"}
            ],
            "compatible_nvrs": ["NVR (8-ch)", "NVR (16-ch)", "NVR DC (8-ch)", "NVR DC (16-ch)"]
        },

        # ================== VIDEO SURVEILLANCE - DOORBELLS ==================
        {
            "name": "DoorBell",
            "category": "doorbells",
            "product_line": "video",
            "description": "Video-Türklingel mit integrierter KI, PIR-Sensor und Steuerung über Apps",
            "short_description": "NEU: Smart Video-Türklingel",
            "usps": ["NEU", "Video-Türklingel", "PIR-Sensor", "App-Steuerung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoor_bell_black_10ac9029f1%402.png&1732028597",
            "specifications": {
                "resolution": "2 Megapixel (1080p)",
                "connectivity": "Wi-Fi 802.11n",
                "detection": "PIR + Video Motion Detection",
                "power": "Akku/Verkabelt",
                "operating_temp": "-20°C bis +50°C",
                "ip_rating": "IP65",
                "xortec_nr": "600810770",
                "hersteller_nr": "DB-WiFi-2MP"
            },
            "features": [
                {"name": "Zwei-Wege-Audio", "description": "Sprechen Sie mit Besuchern über die App"},
                {"name": "PIR-Erkennung", "description": "Bewegungserkennung vor der Haustür"},
                {"name": "Cloud-Recording", "description": "Automatische Aufzeichnung in der Cloud"}
            ],
            "compatible_nvrs": ["NVR (8-ch)", "NVR (16-ch)", "NVR DC (8-ch)", "NVR DC (16-ch)"]
        },

        # ================== VIDEO SURVEILLANCE - NVRs ==================
        {
            "name": "NVR (8-ch)",
            "category": "nvrs",
            "product_line": "video",
            "description": "Netzwerk-Videorekorder für 8 Kanäle",
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
            "product_line": "video", 
            "description": "Netzwerk-Videorekorder für 16 Kanäle",
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
            "product_line": "video",
            "description": "Netzwerk-Videorekorder für 8 Kanäle mit Niederspannungsversorgung",
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
            "product_line": "video",
            "description": "Netzwerk-Videorekorder für 16 Kanäle mit Niederspannungsversorgung",
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
        }
    ]

def get_ajax_categories_2025():
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
            "id": "keypads",
            "name": "Tastaturen",
            "description": "Bedientastaturen und RFID",
            "icon": "keypad"
        },
        {
            "id": "cameras",
            "name": "Kameras",
            "description": "IP-Sicherheitskameras",
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
        }
    ]

def get_ajax_product_lines_2025():
    return [
        {
            "id": "baseline",
            "name": "Baseline",
            "description": "Professionelle kabellose Geräte für Wohn- und Gewerbeobjekte",
            "features": ["Grade 2 EN 50131", "Jeweller-Protokoll", "Große Auswahl", "Einfache Installation"],
            "target_group": "Alle Ajax-Partner",
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbaseline_lg_bc7460aa05%402.jpg&1731779933"
        },
        {
            "id": "superiorline", 
            "name": "Superior",
            "description": "Hochprofessionelle kabellose und verdrahtete Geräte für höchste Ansprüche",
            "features": ["Grade 3 EN 50131", "Jeweller + Fibra", "Erweiterte Funktionen", "Nur für akkreditierte Partner"],
            "target_group": "Akkreditierte Ajax-Partner",
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_lg_7b3c7741db%402.jpg&1731780001"
        },
        {
            "id": "video",
            "name": "Video Surveillance",
            "description": "Professionelle Videoüberwachungslösungen",
            "features": ["KI-gestützt", "Hybrid-Beleuchtung", "4K-Auflösung", "NDAA-konform"],
            "target_group": "Alle Ajax-Partner",
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fvideo_surveillance_lg_60f5f58bb5%402.jpg&1763473120"
        },
        {
            "id": "en54",
            "name": "Fire & Life Safety",
            "description": "Brandschutz- und Lebensschutz-Systeme nach EN54",
            "features": ["EN54-zertifiziert", "Brandschutz", "Professionell", "Europäische Normen"],
            "target_group": "Zertifizierte Brandschutz-Partner",
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fproduct-categories%2Ffire-and-life-safety.lg.jpg&1751882727"
        }
    ]

if __name__ == "__main__":
    products = get_ajax_products_2025()
    categories = get_ajax_categories_2025()
    product_lines = get_ajax_product_lines_2025()
    
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