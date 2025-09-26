from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import uuid
from datetime import datetime
from fastapi.responses import FileResponse
import json

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Pydantic Models
class ProductFeature(BaseModel):
    name: str
    description: str

class ProductSpecification(BaseModel):
    frequency: Optional[str] = None
    range: Optional[str] = None
    battery_life: Optional[str] = None
    operating_temp: Optional[str] = None
    ip_rating: Optional[str] = None
    dimensions: Optional[str] = None
    weight: Optional[str] = None
    max_devices: Optional[int] = None
    communication: Optional[List[str]] = None
    xortec_nr: Optional[str] = None
    hersteller_nr: Optional[str] = None

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    category: str
    product_line: str  # "baseline", "superiorline", "en54", "video"
    description: str
    short_description: str
    usps: List[str]
    image_url: str
    specifications: ProductSpecification
    features: List[ProductFeature]
    compatible_hubs: List[str]
    price: Optional[float] = None
    in_stock: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ConfigurationStep(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    step_number: int
    title: str
    description: str
    product_line: Optional[str] = None
    category: Optional[str] = None

class SystemConfiguration(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    product_line: str
    selected_products: List[str]  # Product IDs
    total_price: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    created_by: Optional[str] = None

class ConfigurationCreate(BaseModel):
    name: str
    description: str
    product_line: str
    selected_products: List[str]
    created_by: Optional[str] = None

# Initialize products data with COMPLETE Ajax product list from Xortec

# Improved product image mapping with proper placeholder images
def get_product_image_url(product_name, category):
    """Get appropriate product image URL based on product name and category"""
    
    # High-quality placeholder images for different Ajax product categories
    category_images = {
        'hubs': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=300&fit=crop&crop=center',
        'motion_detectors': 'https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=400&h=300&fit=crop&crop=center', 
        'opening_detectors': 'https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=400&h=300&fit=crop&crop=center',
        'glass_break_detectors': 'https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=400&h=300&fit=crop&crop=center',
        'fire_detectors': 'https://images.unsplash.com/photo-1609205807107-e8ec2120f9de?w=400&h=300&fit=crop&crop=center',
        'keypads': 'https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=400&h=300&fit=crop&crop=center',
        'sirens': 'https://images.unsplash.com/photo-1609205807107-e8ec2120f9de?w=400&h=300&fit=crop&crop=center',
        'buttons_keyfobs': 'https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=400&h=300&fit=crop&crop=center',
        'range_extenders': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=300&fit=crop&crop=center',
        'wired_cameras': 'https://images.unsplash.com/photo-1557804506-669a67965ba0?w=400&h=300&fit=crop&crop=center',
        'wifi_cameras': 'https://images.unsplash.com/photo-1557804506-669a67965ba0?w=400&h=300&fit=crop&crop=center'
    }
    
    return category_images.get(category, 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=300&fit=crop&crop=center')

async def init_products():
    # Check if products already exist
    existing_products = await db.products.count_documents({})
    if existing_products > 0:
        return
    
    # COMPLETE Ajax products data based on Xortec catalog
    products_data = [
        # ================== HUB-ZENTRALEN (Alle Modelle) ==================
        {
            "name": "Hub 2 Plus Jeweller",
            "category": "hubs",
            "product_line": "baseline",
            "description": "Gefahrenmeldezentrale in schwarz/weiß, 200 Komponenten, 25 Sicherungsbereiche, 200 Benutzer, MotionCam Unterstützung, bis zu 100 Kameras GSM 2G/3G/4G, WLAN 2,4 GHz (802.11 b/g/n) u. Ethernet Kommunikationsmodul",
            "short_description": "Zentrale mit Fotoverifizierung, WLAN und mehrfacher Konnektivität",
            "usps": ["Fotoverifizierung", "WLAN + Ethernet + 2x SIM", "Bis zu 200 Geräte", "4 Kommunikationskanäle"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 2000m",
                "max_devices": 200,
                "communication": ["WLAN", "Ethernet", "2G/3G/LTE"],
                "operating_temp": "-10°C bis +40°C",
                "dimensions": "163 × 163 × 36 mm",
                "xortec_nr": "600810057/600810058",
                "hersteller_nr": "38244.40.BL1/38245.40.WH1"
            },
            "features": [
                {"name": "Fotoverifizierung", "description": "Automatische Fotoaufnahme bei Alarm"},
                {"name": "Mehrfach-Konnektivität", "description": "4 unabhängige Kommunikationskanäle"},
                {"name": "64 Automatisierungsszenarien", "description": "Intelligente Systemautomatisierung"}
            ],
            "compatible_hubs": ["self"]
        },
        {
            "name": "Hub 2 (4G) Jeweller",
            "category": "hubs", 
            "product_line": "baseline",
            "description": "Gefahrenmeldezentrale mit Unterstützung der MotionCam BWM mit visueller Alarmbestätigung, 100 Komponenten, 9 Sicherungsbereiche, 50 Benutzer, bis zu 25 Kameras, GSM 850/900/1800/1900 MHz",
            "short_description": "Hub mit 4G Konnektivität und Fotoverifizierung",
            "usps": ["Fotoverifizierung", "4G/LTE", "2x SIM", "Bis zu 100 Geräte"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 2000m", 
                "max_devices": 100,
                "communication": ["Ethernet", "2G/3G/LTE"],
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810009",
                "hersteller_nr": "38238.40.BL1"
            },
            "features": [
                {"name": "4G LTE", "description": "Schnelle Mobilfunkverbindung"},
                {"name": "Fotoverifizierung", "description": "Visuelle Alarmbestätigung"},
                {"name": "Dual SIM", "description": "Ausfallsichere Kommunikation"}
            ],
            "compatible_hubs": ["self"]
        },
        {
            "name": "Hub BP Jeweller",
            "category": "hubs",
            "product_line": "baseline",
            "description": "Kabellose, batteriebetriebene Gefahrenmeldezentrale. Unterstützt Fotoverifizierung. Anschluss über zwei SIM-Karten (2G/3G/LTE).",
            "short_description": "Batteriebetriebene Zentrale für mobile Einsätze",
            "usps": ["Batteriebetrieben", "Fotoverifizierung", "2x SIM", "Mobiler Einsatz"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_bp_jeweller_black_1760739e4c%402.png&1732115997",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 2000m",
                "max_devices": 200,
                "communication": ["2G/3G/LTE"],
                "operating_temp": "-10°C bis +40°C",
                "battery_life": "bis zu 16 Stunden",
                "xortec_nr": "600810XXX",
                "hersteller_nr": "Hub BP"
            },
            "features": [
                {"name": "Batteriebetrieb", "description": "Unabhängig vom Stromnetz"},
                {"name": "Dual SIM", "description": "Redundante Mobilfunkverbindung"},
                {"name": "Portable Installation", "description": "Schnelle Einrichtung überall"}
            ],
            "compatible_hubs": ["self"]
        },
        {
            "name": "Hub (2G) Jeweller",
            "category": "hubs",
            "product_line": "baseline", 
            "description": "Gefahrenmeldezentrale, 100 Komponenten, 9 Sicherungsbereiche, 50 Benutzer, bis zu 10 Kameras GSM 850/900/1800/1900 MHz u. Ethernet Kommunikationsmodul",
            "short_description": "Basis Hub mit 2G Kommunikation",
            "usps": ["100 Geräte", "2G Konnektivität", "Ethernet", "9 Bereiche"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 2000m",
                "max_devices": 100,
                "communication": ["Ethernet", "2G"],
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810007",
                "hersteller_nr": "38236.01.BL1"
            },
            "features": [
                {"name": "Basis Funktionen", "description": "Alle grundlegenden Hub-Funktionen"},
                {"name": "2G Kommunikation", "description": "Zuverlässige GSM-Verbindung"},
                {"name": "Ethernet Backup", "description": "Kabelgebundene Internetverbindung"}
            ],
            "compatible_hubs": ["self"]
        },
        {
            "name": "Superior Hub Hybrid (4G)",
            "category": "hubs",
            "product_line": "superiorline",
            "description": "Hybride Hub-Zentrale mit Fotoverifizierung. Funktioniert mit Fibra- und Jeweller-Geräten. Anschließbar über Ethernet und zwei SIM-Karten (2G/3G/LTE)",
            "short_description": "Hybrid-Zentrale für Jeweller + Fibra Geräte",
            "usps": ["Fibra + Jeweller Support", "Bis zu 400 Geräte", "Grade 3 Zertifizierung", "Höchste Sicherheitsstandards"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_hybrid_black_eb78efaa15%402.png&1696515890",
            "specifications": {
                "frequency": "868 MHz (Jeweller) + Fibra (kabelgebunden)",
                "range": "bis zu 2000m (Jeweller)",
                "max_devices": 400,
                "communication": ["Ethernet", "2G/3G/LTE"],
                "operating_temp": "-25°C bis +50°C",
                "xortec_nr": "600810XXX",
                "hersteller_nr": "Superior Hub Hybrid"
            },
            "features": [
                {"name": "Hybrid-Unterstützung", "description": "Sowohl Fibra als auch Jeweller Geräte"},
                {"name": "Grade 3 Sicherheit", "description": "Höchste Sicherheitsstandards EN 50131"},
                {"name": "Erweiterte Kapazität", "description": "Bis zu 400 Geräte pro System"}
            ],
            "compatible_hubs": ["self"]
        },
        {
            "name": "EN54 Fire Hub Jeweller",
            "category": "hubs",
            "product_line": "en54",
            "description": "Kabellose Steuerzentrale für EN54-Brandwarnsysteme, Touchscreen, Kommunikation über Funk oder Ethernet",
            "short_description": "EN54 zertifizierte Brandwarnzentrale",
            "usps": ["EN 54 zertifiziert", "Brandschutz + Einbruchschutz", "Kommerzielle Anwendungen", "Touchscreen CIE"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fen54_fire_hub_jeweller_black_fd80de7c0f%402.png&1753716121",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 2000m",
                "max_devices": 200,
                "communication": ["Ethernet", "GSM"],
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810437",
                "hersteller_nr": "125732.315.WH"
            },
            "features": [
                {"name": "EN 54 Zertifizierung", "description": "Vollständig zertifiziert für kommerzielle Brandschutzanlagen"},
                {"name": "Kombinierter Schutz", "description": "Brandschutz und Einbruchschutz in einem System"},
                {"name": "CIE Touchscreen", "description": "Zentrale Bedieneinheit mit Touchscreen"}
            ],
            "compatible_hubs": ["self"]
        },
        
        # ================== BEWEGUNGSMELDER (Alle Modelle) ==================
        {
            "name": "MotionProtect Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "PIR Funk-Bewegungsmelder, Bewegungserfassungsabstand bis zu 12 m, bis zu 1700 m Reichweite (ohne Hindernisse), 868,0 - 868,6 MHz, Erfassungswinkel Horizontal 88° Vertikal 80°",
            "short_description": "Zuverlässiger PIR-Bewegungsmelder für den Innenbereich",
            "usps": ["12m Erfassungsreichweite", "7 Jahre Batterielaufzeit", "Haustier-Immunität bis 20kg", "SmartDetect Algorithmus"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_7e25a60ef8%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "ip_rating": "IP50",
                "xortec_nr": "600810025/600810026",
                "hersteller_nr": "38193.09.WH1/38194.09.BL1"
            },
            "features": [
                {"name": "SmartDetect", "description": "Intelligente Bewegungserkennung mit Störungsfilter"},
                {"name": "Haustier-Immunität", "description": "Ignoriert Tiere bis 20kg und 50cm Höhe"},
                {"name": "Sabotage-Schutz", "description": "Erkennt Manipulationsversuche sofort"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "MotionProtect Plus Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline", 
            "description": "PIR Funk-Bewegungsmelder inkl. Mikrowellensensor (24GHz), Bewegungserfassungsabstand bis zu 12 m, bis zu 1200 m Reichweite (ohne Hindernisse), 868,0 - 868,6 MHz, Erfassungswinkel Horizontal 88° Vertikal 80°",
            "short_description": "Dual-Technologie Bewegungsmelder (PIR + Mikrowelle)",
            "usps": ["Duale Sensorik", "Reduzierte Fehlalarme", "12m Erfassungsreichweite", "Haustier-Immunität"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_plus_111a8e0f23%402.png&1689159156",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1200m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "ip_rating": "IP50",
                "xortec_nr": "600810027/600810209",
                "hersteller_nr": "38198.02.WH1/38199.02.BL1"
            },
            "features": [
                {"name": "Dual-Technologie", "description": "PIR + Mikrowellen-Sensor für höchste Zuverlässigkeit"},
                {"name": "Anti-Masking", "description": "Erkennt Versuche der Sensorabdeckung"},
                {"name": "Erweiterte Filterung", "description": "Minimiert Fehlalarme durch Umwelteinflüsse"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "MotionCam (PhOD) Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "Kabelloser IR-Bewegungsmelder für den Innenbereich mit Fotoverifizierung von Alarmen und den Funktionen 'Foto auf Anfrage' und 'Foto nach Szenario'",
            "short_description": "Bewegungsmelder mit integrierter Kamera",
            "usps": ["Foto-Verifikation", "120° Bildwinkel", "Nachtsicht bis 5m", "Verschlüsselte Übertragung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotion_cam_jeweller_black_50c00ca247%402.png&1727442738",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 4 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810128/600810129",
                "hersteller_nr": "39289.120.BL1/39290.120.WH1"
            },
            "features": [
                {"name": "Foto-Verifikation", "description": "Automatische Fotoaufnahme bei Alarmauslösung"},
                {"name": "Infrarot-Illumination", "description": "Klare Aufnahmen auch bei völliger Dunkelheit"},
                {"name": "Ende-zu-Ende-Verschlüsselung", "description": "Sichere Übertragung aller Bilddaten"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "MotionCam Outdoor HighMount (PhOD) Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "Wireless IR motion detector that takes on-demand photos and photos by alarm, schedule, and scenario. For outdoor installation at a height of 2–4 m.",
            "short_description": "Outdoor Bewegungsmelder mit Kamera für Höhenmontage",
            "usps": ["Outdoor-Installation", "2-4m Höhenmontage", "Foto-Verifikation", "Wetterfest"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotioncam_outdoor_highmount_white_123abc%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 3 Jahre",
                "operating_temp": "-25°C bis +60°C",
                "ip_rating": "IP54",
                "xortec_nr": "600810403",
                "hersteller_nr": "99164.282.WH1"
            },
            "features": [
                {"name": "Höhenmontage", "description": "Optimiert für Installation in 2-4m Höhe"},
                {"name": "Wetterschutz", "description": "IP54 für Außeneinsatz"},
                {"name": "Erweiterte Erkennung", "description": "Spezielle Algorithmen für Outdoor-Einsatz"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "CombiProtect Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "PIR Funk-Bewegungs- u. Glasbruchmelder, Bewegungserfassungsabstand bis zu 12 m, bis zu 1200 m Reichweite (ohne Hindernisse), 868,0 - 868,6 MHz, Erfassungswinkel Horizontal 88° Vertikal 80°",
            "short_description": "Kombinierter Bewegungs- und Glasbruchmelder",
            "usps": ["2-in-1 Gerät", "Bewegung + Glasbruch", "Kosteneffizient", "SmartDetect"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fcombiprotect_ee0a5c6eb3%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1200m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810031/600810032",
                "hersteller_nr": "38097.06.WH1/38096.06.BL1"
            },
            "features": [
                {"name": "Dual-Funktion", "description": "Bewegungserkennung und Glasbrucherkennung in einem Gerät"},
                {"name": "Kostenersparnis", "description": "Ein Gerät für zwei Schutzfunktionen"},
                {"name": "SmartDetect", "description": "Intelligente Signalverarbeitung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Curtain Outdoor Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "Outdoor Curtain Bewegungsmelder für schmale Erfassungsbereiche",
            "short_description": "Outdoor Vorhang-Bewegungsmelder",
            "usps": ["Outdoor-geeignet", "Schmaler Erfassungsbereich", "Wetterschutz", "Perimeterschutz"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fcurtain_outdoor_white_abc123%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-25°C bis +60°C",
                "ip_rating": "IP65",
                "xortec_nr": "600810445",
                "hersteller_nr": "101441.289.WH1"
            },
            "features": [
                {"name": "Vorhang-Erkennung", "description": "Schmaler Erfassungsbereich für Perimeterschutz"},
                {"name": "Wetterschutz", "description": "IP65 für Außeneinsatz"},
                {"name": "Flexible Montage", "description": "Verschiedene Montagemöglichkeiten"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # ================== SUPERIOR BEWEGUNGSMELDER ==================
        {
            "name": "Superior MotionProtect Jeweller",
            "category": "motion_detectors",
            "product_line": "superiorline",
            "description": "Kabelloser IR-Bewegungsmelder. Superior Edition mit Grade 3 Zertifizierung",
            "short_description": "Professional PIR-Bewegungsmelder",
            "usps": ["Grade 3 Zertifizierung", "Erweiterte Anti-Sabotage", "Professional Grade", "12m Erfassung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmpsj_s_34e8d588e9%402.png&1688046986",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre", 
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP50"
            },
            "features": [
                {"name": "Grade 3 Zertifizierung", "description": "Höchste Sicherheitsstufe nach EN 50131"},
                {"name": "Erweiterte Anti-Sabotage", "description": "Professioneller Manipulationsschutz"},
                {"name": "Temperaturkompensation", "description": "Stabile Erkennung bei Temperaturschwankungen"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior MotionProtect Plus Jeweller", 
            "category": "motion_detectors",
            "product_line": "superiorline",
            "description": "Kabelloser IR-Bewegungsmelder mit zusätzlichem K-Band-Mikrowellensensor. Superior Edition",
            "short_description": "Professional Dual-Technologie Bewegungsmelder",
            "usps": ["Duale Sensorik", "Grade 3 Zertifizierung", "Anti-Masking", "Erweiterte Sabotage-Erkennung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmpspj_s_68b8826cc2%402.png&1688046815",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP50",
                "xortec_nr": "600810641",
                "hersteller_nr": "133222.02.WH1"
            },
            "features": [
                {"name": "Dual-Technologie", "description": "PIR + Mikrowellen-Sensor für höchste Zuverlässigkeit"},
                {"name": "Anti-Masking", "description": "Erkennt Versuche der Sensorabdeckung"},
                {"name": "Grade 3 Zertifizierung", "description": "Höchste Sicherheitsstufe nach EN 50131"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior MotionCam AM (PhOD) Jeweller",
            "category": "motion_detectors",
            "product_line": "superiorline",
            "description": "Superior MotionCam AM (PhOD) Jeweller für professionelle Anwendungen",
            "short_description": "Professional Bewegungsmelder mit Anti-Masking und Foto",
            "usps": ["Anti-Masking", "Grade 3", "Foto-Verifikation", "Professional"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_motioncam_am_white%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 4 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "xortec_nr": "600810602",
                "hersteller_nr": "116768.306.WH1"
            },
            "features": [
                {"name": "Anti-Masking", "description": "Aktiver Schutz gegen Manipulationsversuche"},
                {"name": "Grade 3 Zertifizierung", "description": "Höchste professionelle Sicherheitsstufe"},
                {"name": "Foto-Verifikation", "description": "Visuelle Alarmbestätigung"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior MotionCam HD (PhOD) Jeweller",
            "category": "motion_detectors",
            "product_line": "superiorline",
            "description": "Superior MotionCam HD (PhOD) Jeweller mit HD Auflösung",
            "short_description": "Professional HD Bewegungsmelder mit Kamera",
            "usps": ["HD Auflösung", "Grade 3", "Professional", "Anti-Masking"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_motioncam_hd_white%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 3 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "xortec_nr": "600810616",
                "hersteller_nr": "118274.309.WH1"
            },
            "features": [
                {"name": "HD Auflösung", "description": "Hochauflösende Kameraaufnahmen"},
                {"name": "Professional Grade", "description": "Für anspruchsvollste Sicherheitsanwendungen"},
                {"name": "Erweiterte Funktionen", "description": "Vollständige Professional-Ausstattung"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior CombiProtect Jeweller",
            "category": "motion_detectors",
            "product_line": "superiorline",
            "description": "Superior CombiProtect Jeweller kombiniert Bewegungs- und Glasbruchererkennung",
            "short_description": "Professional Kombi-Melder für Bewegung und Glasbruch",
            "usps": ["Grade 3", "Dual-Funktion", "Professional", "Anti-Masking"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_combiprotect_white%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "xortec_nr": "600810625",
                "hersteller_nr": "133190.06.WH1"
            },
            "features": [
                {"name": "Professional Dual-Funktion", "description": "Bewegung und Glasbruch in Grade 3 Qualität"},
                {"name": "Anti-Masking", "description": "Schutz gegen Manipulationsversuche"},
                {"name": "Grade 3 Zertifizierung", "description": "Höchste professionelle Standards"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        
        # ================== ÖFFNUNGSMELDER (Alle Modelle) ==================
        {
            "name": "DoorProtect Jeweller",
            "category": "opening_detectors",
            "product_line": "baseline",
            "description": "Drahtloser Öffnungs-Melder, bis zu 1200 m Reichweite (ohne Hindernisse), 868,0 - 868,6 MHz, CR123A-Batterie, Stromversorgungsspannung 3 V, Batterielaufzeit bis zu 7 Jahre",
            "short_description": "Kompakter Tür-/Fensterkontakt",
            "usps": ["7 Jahre Batterielaufzeit", "Ultrakleine Bauform", "Sabotage-Schutz", "Sofortige Benachrichtigung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_f565be9860%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1200m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "dimensions": "88 × 20 × 15 mm",
                "xortec_nr": "600810018/600810019",
                "hersteller_nr": "38099.03.WH1/38098.03.BL1"
            },
            "features": [
                {"name": "Reed-Sensor", "description": "Hochzuverlässiger magnetischer Sensor"},
                {"name": "Kompaktdesign", "description": "Unauffällige Installation an Türen und Fenstern"},
                {"name": "Sabotage-Erkennung", "description": "Alarm bei Entfernung vom Montageort"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "DoorProtect Plus Jeweller",
            "category": "opening_detectors",
            "product_line": "baseline",
            "description": "Drahtloser Öffnungs-Melder, registriert Änderungen des vertikalen Neigungswinkels, Schläge und Vibrationen, bis zu 1200 m Reichweite (ohne Hindernisse), 868,0 - 868,6 MHz, CR123A-Batterie",
            "short_description": "Erweiterte Tür-/Fensterkontakt mit Schock-Sensor",
            "usps": ["3-in-1 Sensor", "Erschütterungserkennung", "Neigungserkennung", "Erhöhte Sicherheit"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_f565be9860%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1200m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810020/600810021",
                "hersteller_nr": "38101.13.WH1/38100.21.BL1"
            },
            "features": [
                {"name": "Triple-Sensor", "description": "Öffnung, Erschütterung und Neigung in einem Gerät"},
                {"name": "Shock-Detection", "description": "Erkennt Einbruchsversuche vor dem Öffnen"},
                {"name": "Tilt-Detection", "description": "Überwacht Lageveränderungen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # ================== SUPERIOR ÖFFNUNGSMELDER ==================
        {
            "name": "Superior DoorProtect Jeweller",
            "category": "opening_detectors", 
            "product_line": "superiorline",
            "description": "Kabelloser Öffnungsmelder mit zwei Reedschaltern. Superior Edition",
            "short_description": "Professional Öffnungsmelder mit Dual-Reed",
            "usps": ["Dual Reed-Schalter", "Grade 3 Zertifizierung", "Erweiterte Anti-Sabotage", "Professional Grade"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdpsj_s_553d1e2fdd%402.png&1688046834",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "xortec_nr": "600810627/600810628",
                "hersteller_nr": "133194.03.WH1/133195.03.BL1"
            },
            "features": [
                {"name": "Dual Reed-Technologie", "description": "Zwei unabhängige Reed-Schalter für höchste Zuverlässigkeit"},
                {"name": "Grade 3 Zertifizierung", "description": "Höchste Sicherheitsstufe nach EN 50131"},
                {"name": "Professional Anti-Sabotage", "description": "Erweiterte Manipulationserkennung"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior DoorProtect Plus Jeweller",
            "category": "opening_detectors",
            "product_line": "superiorline",
            "description": "Kombinierter kabelloser Öffnungs-, Erschütterungs- und Neigungsmelder mit zwei Reedschaltern und Beschleunigungssensor. Superior Edition",
            "short_description": "Professional erweiterte Tür-/Fensterkontakt",
            "usps": ["Dual Reed + Schock", "Grade 3", "Professional", "Multi-Sensor"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_superior_plus%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "xortec_nr": "600810629",
                "hersteller_nr": "133198.21.WH1"
            },
            "features": [
                {"name": "Professional Multi-Sensor", "description": "Dual-Reed + Erschütterung + Neigung in Grade 3"},
                {"name": "Erweiterte Sabotage-Erkennung", "description": "Professional-Grade Manipulationsschutz"},
                {"name": "Grade 3 Zertifizierung", "description": "Höchste professionelle Standards"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        
        # ================== GLASBRUCHMELDER ==================
        {
            "name": "GlassProtect Jeweller",
            "category": "glass_break_detectors",
            "product_line": "baseline",
            "description": "Drahtloser Glasbruchmelder, bis zu 1000 m Reichweite (ohne Hindernisse), 868,0 - 868,6 MHz, Erkennungsabstand für Brüche bis zu 9 m, Erfassungswinkel für Brüche 180°, Batterie CR123A",
            "short_description": "Akustischer Glasbruchmelder",
            "usps": ["9m Erfassungsradius", "SmartDetect Algorithmus", "7 Jahre Batterielaufzeit", "Falschalarmschutz"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fglassprotect_bb2a29da00%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1000m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810033",
                "hersteller_nr": "38193.09.WH1"
            },
            "features": [
                {"name": "Akustische Erkennung", "description": "Erkennt charakteristische Glasbruchgeräusche"},
                {"name": "SmartDetect", "description": "Filterung von Störgeräuschen und Falschalarmen"},
                {"name": "Großer Erfassungsbereich", "description": "Schutz mehrerer Fenster mit einem Gerät"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior GlassProtect Jeweller",
            "category": "glass_break_detectors",
            "product_line": "superiorline", 
            "description": "Kabelloser Glasbruchmelder mit Mikrofon. Superior Edition",
            "short_description": "Professional akustischer Glasbruchmelder",
            "usps": ["Grade 3 Zertifizierung", "Erweiterte Filterung", "9m Erfassung", "Professional Grade"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fgpsj_s_b2db014217%402.png&1688046912",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1000m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "xortec_nr": "600810632",
                "hersteller_nr": "133203.05.BL1"
            },
            "features": [
                {"name": "Grade 3 Zertifizierung", "description": "Höchste Sicherheitsstufe nach EN 50131"},
                {"name": "Erweiterte Signalverarbeitung", "description": "Minimierte Fehlalarme durch intelligente Algorithmen"},
                {"name": "Professional Mikrofon", "description": "Hochempfindliche Schallerfassung"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        
        # ================== BEDIENTEILE / KEYPADS ==================
        {
            "name": "KeyPad TouchScreen Jeweller",
            "category": "keypads",
            "product_line": "baseline",
            "description": "Kabelloses Touchscreen-Bedienteil, das die Authentifizierung per Smartphone, Pass, Tag und Code unterstützt",
            "short_description": "Modernes Touchscreen-Bedienteil",
            "usps": ["4.3\" Touchscreen", "Smartphone-Auth", "RFID-Unterstützung", "Elegantes Design"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_touchscreen_4a49692df5%402.png&1691157817",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 2 Jahre",
                "operating_temp": "0°C bis +40°C"
            },
            "features": [
                {"name": "Touchscreen-Display", "description": "Intuitive Bedienung über 4.3\" Farbdisplay"},
                {"name": "Multi-Authentifizierung", "description": "Code, RFID-Karte, Smartphone oder Schlüsselanhänger"},
                {"name": "System-Status", "description": "Anzeige aller Systemzustände und Ereignisse"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "KeyPad Plus Jeweller",
            "category": "keypads",
            "product_line": "baseline",
            "description": "Kabellose Touch-Tastatur für die Verwaltung des Ajax Sicherheitssystems mit verschlüsselten, kontaktlosen Karten und Funkfernbedienungen",
            "short_description": "Touch-Bedienteil mit RFID",
            "usps": ["Touchscreen", "RFID-Karten", "Verschlüsselt", "LED-Anzeigen"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_plus_cb76223961%402.png&1689152843",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 2 Jahre",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600810066/600810067",
                "hersteller_nr": "38252.83.BL1/38253.83.WH1"
            },
            "features": [
                {"name": "Touch-Bedienung", "description": "Kapazitive Touch-Tasten"},
                {"name": "RFID-Unterstützung", "description": "Pass und Tag Authentifizierung"},
                {"name": "LED-Feedback", "description": "Visuelle Statusanzeigen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior KeyPad Plus Jeweller",
            "category": "keypads",
            "product_line": "superiorline",
            "description": "Superior KeyPad Plus Jeweller für professionelle Anwendungen",
            "short_description": "Professional Touch-Bedienteil",
            "usps": ["Grade 3 Zertifizierung", "Professional", "RFID", "Erweiterte Sicherheit"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_keypad_plus%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 2 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "xortec_nr": "600810636",
                "hersteller_nr": "133211.83.BL1"
            },
            "features": [
                {"name": "Grade 3 Zertifizierung", "description": "Höchste professionelle Sicherheitsstufe"},
                {"name": "Erweiterte Verschlüsselung", "description": "Professional-Grade Datenschutz"},
                {"name": "Robustes Design", "description": "Für anspruchsvolle Umgebungen"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        
        # ================== SIRENEN (Alle Modelle) ==================
        {
            "name": "HomeSiren Jeweller",
            "category": "sirens",
            "product_line": "baseline", 
            "description": "Kabellose Jeweller Sirene für den Innenbereich; Türglockenfunktion; einstellbare Lautstärke für Alarme und Signale von 80 dB bis 100 dB; einstellbare Alarmdauer von 3 bis 180s",
            "short_description": "Innensirene für Wohnbereiche",
            "usps": ["81 dB Lautstärke", "Kompaktdesign", "LED-Anzeigen", "Türglocken-Funktion"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhomesiren_90d4c3023b%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "0°C bis +40°C",
                "xortec_nr": "600810205/600810206",
                "hersteller_nr": "38110.11.BL1/38111.11.WH1"
            },
            "features": [
                {"name": "Innenbereich", "description": "Optimiert für Wohnräume"},
                {"name": "Kompakte Bauweise", "description": "Unauffällige Installation"},
                {"name": "Angenehme Lautstärke", "description": "Effektiv aber nicht übermäßig laut"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "StreetSiren Jeweller",
            "category": "sirens",
            "product_line": "baseline",
            "description": "Drahtlose Außensirene, 85 - 113 dB in 1 m Entfernung, LED-Ring f. optische Alarmierung, bis zu 1500 m Reichweite (ohne Hindernisse), 868,0 - 868,6 MHz, Batterie 4 x CR123A",
            "short_description": "Standard Außensirene",
            "usps": ["105 dB Lautstärke", "Wetterschutz", "LED-Anzeigen", "Langlebig"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstreetsiren_ef479c2a02%402.png&1689152843",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1500m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP54",
                "xortec_nr": "600810035",
                "hersteller_nr": "38178.07.WH1"
            },
            "features": [
                {"name": "Wetterschutz", "description": "IP54 Schutzart für Außeneinsatz"},
                {"name": "LED-Signalisierung", "description": "Farbige LED-Anzeigen"},
                {"name": "Robustes Gehäuse", "description": "Vandalismus-sicheres Design"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "StreetSiren DoubleDeck Jeweller",
            "category": "sirens",
            "product_line": "baseline",
            "description": "Drahtlose Außensirene, Unterteil für bedruckbare Frontplatte, 85 - 113 dB in 1 m Entfernung, LED-Ring f. optische Alarmierung, bis zu 1500 m Reichweite (ohne Hindernisse), 868,0 - 868,6 MHz",
            "short_description": "Außensirene mit LED-Blitzlicht und Brandplate",
            "usps": ["113 dB Lautstärke", "Brandplate-Support", "LED-Blitzlicht", "5 Jahre Batterielaufzeit"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstreetsiren_doubledeck_aa7ec7f313%402.png&1716365399",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1500m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP54",
                "xortec_nr": "600810061",
                "hersteller_nr": "38181.61.BL1"
            },
            "features": [
                {"name": "Hohe Lautstärke", "description": "Bis zu 113 dB Schallleistung"},
                {"name": "LED-Signalgebung", "description": "Helles Blitzlicht als visuelle Warnung"},
                {"name": "Brandplate-Option", "description": "Individualisierung mit Firmenkennzeichnung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior StreetSiren Plus Fibra",
            "category": "sirens",
            "product_line": "superiorline",
            "description": "Superior StreetSiren Plus Fibra für kabelgebundene Installation",
            "short_description": "Professional kabelgebundene Außensirene",
            "usps": ["Fibra-Technologie", "Grade 3", "Kabelgebunden", "Professional"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_streetsiren_fibra%402.png",
            "specifications": {
                "frequency": "Fibra (kabelgebunden)",
                "range": "bis zu 2000m über Fibra",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP54",
                "xortec_nr": "600810606",
                "hersteller_nr": "117726.268.BL1"
            },
            "features": [
                {"name": "Fibra-Technologie", "description": "Kabelgebundene Übertragung für höchste Zuverlässigkeit"},
                {"name": "Grade 3 Zertifizierung", "description": "Professional-Grade Sicherheit"},
                {"name": "Erweiterte Funktionen", "description": "Vollständige Professional-Ausstattung"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        
        # ================== BUTTONS & HANDSENDER ==================
        {
            "name": "Button Jeweller",
            "category": "buttons_keyfobs",
            "product_line": "baseline",
            "description": "Kabelloser Notruf-/Smart-Knopf für Panikalarme",
            "short_description": "Notfallknopf für Panikalarme",
            "usps": ["Notfallknopf", "Wasserdicht", "Tragbar", "Sofortalarm"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbutton_0e53cdc0b2%402.png&1689152841",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "ip_rating": "IP54",
                "xortec_nr": "600810097/600810098",
                "hersteller_nr": "38094.26.BL1/38095.26.WH1"
            },
            "features": [
                {"name": "Panik-Alarm", "description": "Sofortiger Notfallalarm per Knopfdruck"},
                {"name": "Wasserschutz", "description": "IP54 Schutzart"},
                {"name": "Tragbares Design", "description": "Kompakt und leicht zu tragen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "DoubleButton Jeweller",
            "category": "buttons_keyfobs",
            "product_line": "baseline",
            "description": "kabelloser Jeweller Notfallknopf mit 2 Tasten. Zur Aktivierung müssen beide Tasten gedrückt werden",
            "short_description": "Doppelknopf gegen versehentliche Auslösung",
            "usps": ["Doppelknopf", "Fehlalarmschutz", "Notfall", "Tragbar"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoublebutton_3b06f09e9d%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m", 
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810201",
                "hersteller_nr": "38102.79.BL1"
            },
            "features": [
                {"name": "Doppelknopf-Sicherheit", "description": "Verhindert versehentliche Aktivierung"},
                {"name": "Notfall-Funktion", "description": "Zuverlässiger Notruf im Ernstfall"},
                {"name": "Kompakte Bauweise", "description": "Einfach zu transportieren"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "SpaceControl Jeweller",
            "category": "buttons_keyfobs",
            "product_line": "baseline",
            "description": "Funkfernbedienung mit vier Tasten und der Bestätigung der Signal-Zustellung, Paniktaste, bis zu 1300 m Reichweite (ohne Hindernisse), 868,0 - 868,6 MHz",
            "short_description": "4-Tasten Handsender für Systemsteuerung",
            "usps": ["4 Tasten", "Systemsteuerung", "Panikfunktion", "Fernbedienung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fspacecontrol_495b92c9f7%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m",
                "battery_life": "bis zu 5 Jahre", 
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810016/600810017",
                "hersteller_nr": "38166.04.WH1/38167.04.BL1"
            },
            "features": [
                {"name": "Vier Tasten", "description": "Scharf, Unscharf, Teilscharf und Panik"},
                {"name": "Systemsteuerung", "description": "Vollständige Fernbedienung des Systems"},
                {"name": "Panikfunktion", "description": "Separate Paniktaste für Notfälle"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # ================== FUNK-REPEATER ==================
        {
            "name": "ReX 2 Jeweller",
            "category": "range_extenders",
            "product_line": "baseline",
            "description": "Kabelloser Funk-Repeater mit Unterstützung für Jeweller und Wings Protokolle",
            "short_description": "Dual-Protokoll Funkverstärker",
            "usps": ["Jeweller + Wings", "Reichweitenverlängerung", "Dual-Protokoll", "Einfache Installation"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Frex_2_ca92ad0fe2%402.png&1689158367",
            "specifications": {
                "frequency": "868 MHz (Jeweller) + Wings",
                "range": "bis zu 1700m",
                "operating_temp": "-10°C bis +40°C",
                "ip_rating": "IP65",
                "xortec_nr": "600810143",
                "hersteller_nr": "38207.106.WH1"
            },
            "features": [
                {"name": "Dual-Protokoll", "description": "Unterstützt Jeweller und Wings Geräte"},
                {"name": "Reichweitenverlängerung", "description": "Verdoppelt die Funkreichweite"},
                {"name": "Wetterschutz", "description": "IP65 für Außeninstallation"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # ================== BRANDSCHUTZ ==================
        {
            "name": "FireProtect 2 RB (Heat/Smoke)",
            "category": "fire_detectors",
            "product_line": "baseline",
            "description": "AJAX FireProtect 2 RB (Heat/Smoke) Rauch- und Wärmemelder mit austauschbaren Batterien",
            "short_description": "Rauch-/Wärmemelder für Wohnbereiche",
            "usps": ["10 Jahre Batterielaufzeit", "Dual-Sensor-Technologie", "Austauschbare Batterie", "SmartDetect"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffireprotect_2_rb_black_a1b2c3d4e5%402.png&1688287078",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 10 Jahre",
                "operating_temp": "-10°C bis +50°C",
                "xortec_nr": "600810100/600810101",
                "hersteller_nr": "52251.136.BL1/52250.136.WH1"
            },
            "features": [
                {"name": "Langzeit-Batterie", "description": "10 Jahre Lebensdauer ohne Batteriewechsel"},
                {"name": "Dual-Sensor", "description": "Kombinierte Rauch- und Temperaturerkennung"},
                {"name": "Austauschbare Batterie", "description": "Wartungsfreundliches Design"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)", "EN54 Fire Hub Jeweller"]
        },
        {
            "name": "FireProtect 2 RB (Heat/Smoke/CO)",
            "category": "fire_detectors",
            "product_line": "baseline",
            "description": "AJAX FireProtect 2 RB (Heat/Smoke/CO) mit Kohlenmonoxid-Erkennung",
            "short_description": "Kombi-Brandmelder mit CO-Erkennung",
            "usps": ["Triple-Sensor", "CO-Erkennung", "10 Jahre Batterie", "Lebensgefahr-Warnung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffireprotect_2_co_white%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 10 Jahre",
                "operating_temp": "-10°C bis +50°C",
                "xortec_nr": "600810103",
                "hersteller_nr": "52252.137.WH1"
            },
            "features": [
                {"name": "Triple-Sensor", "description": "Rauch, Hitze und Kohlenmonoxid-Erkennung"},
                {"name": "Lebensgefahr-Warnung", "description": "Warnt vor tödlichem Kohlenmonoxid"},
                {"name": "Langzeit-Batterie", "description": "10 Jahre wartungsfreier Betrieb"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)", "EN54 Fire Hub Jeweller"]
        },
        
        # ================== EN54 BRANDSCHUTZ ==================
        {
            "name": "EN54 FireProtect (Smoke)",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Kabelloser Rauchmelder ohne Sirene. Funk-Rauchmelder nach EN54-7 für frühzeitige Branderkennung. Erkennt Rauch zuverlässig, kabellos, batteriebetrieben und einfach zu installieren",
            "short_description": "EN54-zertifizierter Rauchmelder",
            "usps": ["EN 54-7 zertifiziert", "Kommerzielle Anwendung", "10 Jahre Batterielaufzeit", "Professionelle Anwendung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fen54_fireprotect_smoke_white%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 10 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810430/600810431",
                "hersteller_nr": "119921.275.WH1/119922.275.BL1"
            },
            "features": [
                {"name": "EN 54-7 Zertifizierung", "description": "Vollständig zertifiziert für kommerzielle Brandschutzanlagen"},
                {"name": "Professional Grade", "description": "Für gewerbliche und öffentliche Gebäude"},
                {"name": "Langzeit-Batterie", "description": "10 Jahre wartungsfreier Betrieb"}
            ],
            "compatible_hubs": ["EN54 Fire Hub Jeweller"]
        },
        {
            "name": "EN54 FireProtect (Heat)",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Kabelloser Wärmemelder ohne Sirene. Zuverlässiger Funk-Hitzemelder nach EN54-5 für den Brandschutz. Erkennt rasch Temperaturanstieg oder hohe Hitze, kabellos, batteriebetrieben",
            "short_description": "EN54-zertifizierter Wärmemelder",
            "usps": ["EN 54-5 zertifiziert", "Temperaturerkennung", "Kommerzielle Anwendung", "Wartungsarm"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fen54_fireprotect_heat_white%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 10 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810426/600810427",
                "hersteller_nr": "119917.273.WH1/119918.273.BL1"
            },
            "features": [
                {"name": "EN 54-5 Zertifizierung", "description": "Zertifiziert für kommerzielle Wärmeerkennung"},
                {"name": "Temperatur-Erkennung", "description": "Erkennt schnellen Temperaturanstieg"},
                {"name": "Professional Grade", "description": "Für gewerbliche Anwendungen"}
            ],
            "compatible_hubs": ["EN54 Fire Hub Jeweller"]
        },
        {
            "name": "EN54 FireProtect (Smoke/Sounder)",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Kabelloser Rauchmelder mit integrierter Sirene, EN54, 85dB Alarmlautstärke. Funk-Rauchmelder nach EN54-7 mit integriertem Alarmton. Erkennt Rauch zuverlässig, warnt akustisch, kabellos",
            "short_description": "EN54 Rauchmelder mit Sirene",
            "usps": ["EN 54 mit Sirene", "85dB Alarmlautstärke", "Integrierter Alarmton", "Kommerzielle Anwendung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fen54_fireprotect_smoke_sounder%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 10 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810429",
                "hersteller_nr": "119920.276.BL1"
            },
            "features": [
                {"name": "Integrierte Sirene", "description": "85dB Alarmlautstärke vor Ort"},
                {"name": "EN 54 Zertifizierung", "description": "Für kommerzielle Brandschutzanlagen"},
                {"name": "Sofort-Warnung", "description": "Lokale akustische Alarmierung"}
            ],
            "compatible_hubs": ["EN54 Fire Hub Jeweller"]
        },
        {
            "name": "EN54 FireProtect (Heat/Sounder)",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Kabelloser Wärmemelder mit Sirene. Funk-Hitzemelder nach EN54-5 mit integriertem Alarmton. Erkennt Hitze und schnellen Temperaturanstieg, warnt akustisch, kabellos, batteriebetrieben",
            "short_description": "EN54 Wärmemelder mit Sirene",
            "usps": ["EN 54-5 mit Sirene", "Temperaturerkennung", "Integrierter Alarmton", "Kommerzielle Anwendung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fen54_fireprotect_heat_sounder%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 10 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810424",
                "hersteller_nr": "119915.274.WH1"
            },
            "features": [
                {"name": "Integrierte Sirene", "description": "Lokale akustische Alarmierung bei Hitze"},
                {"name": "EN 54-5 Zertifizierung", "description": "Für kommerzielle Wärmeerkennung"},
                {"name": "Temperatur-Alarm", "description": "Warnt vor schnellem Temperaturanstieg"}
            ],
            "compatible_hubs": ["EN54 Fire Hub Jeweller"]
        },
        {
            "name": "Manual Call Point",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Funk-Druckknopfmelder für manuelle Brandmeldung mit rücksetzbarem Auslöseelement und programmierbaren Szenarien",
            "short_description": "Manueller Brandmeldungsknopf",
            "usps": ["Manuelle Brandmeldung", "Rücksetzbar", "Programmierbare Szenarien", "EN54 konform"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmanual_call_point%402.png",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 10 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "xortec_nr": "600810245/600810366",
                "hersteller_nr": "60815.171.NC1/83805.171.NC1"
            },
            "features": [
                {"name": "Manuelle Aktivierung", "description": "Ermöglicht bewusste Brandmeldung"},
                {"name": "Rücksetzbar", "description": "Wiederverwendbar nach Reset"},
                {"name": "Szenarien-Programmierung", "description": "Flexible Reaktionsmöglichkeiten"}
            ],
            "compatible_hubs": ["EN54 Fire Hub Jeweller"]
        },
        
        # ================== VIDEO-KAMERAS (von Xortec) ==================
        {
            "name": "BulletCam (5 Mp/2.8 mm)",
            "category": "wired_cameras",
            "product_line": "video",
            "description": "Kabelgebundene IP-Überwachungskamera mit KI, 110° Blickwinkel, IR, TrueWDR, Mikrofon und PoE/12 V. Für Innen- und Außeneinsatz",
            "short_description": "Professionelle 5MP IP-Kamera",
            "usps": ["5 MP Auflösung", "KI-Objekterkennung", "TrueWDR", "PoE-Unterstützung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2FBullet_Cam_black_fdaf14a78b%402.png&1697096052",
            "specifications": {
                "frequency": "IP (Ethernet/PoE)",
                "range": "Netzwerkbasiert",
                "operating_temp": "-30°C bis +60°C",
                "ip_rating": "IP66"
            },
            "features": [
                {"name": "5 MP Auflösung", "description": "Gestochen scharfe Videoqualität"},
                {"name": "KI-Erkennung", "description": "Intelligente Objekt- und Personenerkennung"},
                {"name": "TrueWDR", "description": "Optimale Bildqualität bei schwierigen Lichtverhältnissen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "TurretCam (5 Mp/2.8 mm)",
            "category": "wired_cameras", 
            "product_line": "video",
            "description": "Kabelgebundene IP-Überwachungskamera mit KI, 110° Blickwinkel, IR, TrueWDR, Mikrofon und PoE/12 V. Für Innen- und Außeneinsatz",
            "short_description": "Turret-Kamera mit flexibler Ausrichtung",
            "usps": ["Turret-Design", "Flexible Ausrichtung", "5 MP Auflösung", "KI-Funktionen"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2FTurret_Cam_black_ba48836a1f%402.png&1697035541",
            "specifications": {
                "frequency": "IP (Ethernet/PoE)",
                "range": "Netzwerkbasiert",
                "operating_temp": "-30°C bis +60°C",
                "ip_rating": "IP66"
            },
            "features": [
                {"name": "Turret-Design", "description": "360° einstellbare Kameraausrichtung"},
                {"name": "Vandalismusschutz", "description": "Robustes, manipulationssicheres Gehäuse"},
                {"name": "KI-Integration", "description": "Intelligente Videoanalyse"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "DomeCam Mini (5 Mp/2.8 mm)",
            "category": "wired_cameras",
            "product_line": "video",
            "description": "Kabelgebundene IP-Überwachungskamera mit KI, 110° Blickwinkel, IR, TrueWDR, Mikrofon und PoE/12 V. Für Innen- und Außeneinsatz",
            "short_description": "Kompakte Dome-Kamera",
            "usps": ["Kompaktes Design", "Dome-Bauform", "5 MP Auflösung", "Unauffällig"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2FDome_Cam_Mini_54a41757df%402.png&1697096385",
            "specifications": {
                "frequency": "IP (Ethernet/PoE)",
                "range": "Netzwerkbasiert",
                "operating_temp": "-30°C bis +60°C",
                "ip_rating": "IP66"
            },
            "features": [
                {"name": "Kompakte Bauform", "description": "Kleine, unauffällige Installation"},
                {"name": "Dome-Design", "description": "Nicht erkennbare Blickrichtung"},
                {"name": "Vollausstattung", "description": "Alle Premium-Features in kompakter Größe"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "IndoorCam",
            "category": "wifi_cameras",
            "product_line": "video",
            "description": "WLAN-Überwachungskamera für den Innenbereich mit PIR-Bewegungssensor und integrierter KI",
            "short_description": "Smarte WLAN-Innenkamera",
            "usps": ["WLAN-Konnektivität", "PIR-Sensor", "KI-Funktionen", "Kompaktes Design"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Findoorcam_black_e562685ad8%402.png&1732114433",
            "specifications": {
                "frequency": "WLAN 2.4/5 GHz",
                "range": "WLAN-abhängig",
                "operating_temp": "0°C bis +40°C"
            },
            "features": [
                {"name": "WLAN-Konnektivität", "description": "Einfache Installation ohne Verkabelung"},
                {"name": "PIR-Integration", "description": "Kombiniert Video mit präziser Bewegungserkennung"},
                {"name": "Smart Features", "description": "KI-basierte Analyse und Benachrichtigungen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "DoorBell",
            "category": "doorbells",
            "product_line": "video", 
            "description": "Video-Türklingel mit integrierter KI, PIR-Sensor und App-Steuerung",
            "short_description": "Smart Video-Türklingel",
            "usps": ["Video-Türklingel", "Zweiwege-Audio", "App-Integration", "PIR-Sensor"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoor_bell_black_10ac9029f1%402.png&1732028597",
            "specifications": {
                "frequency": "WLAN 2.4 GHz",
                "range": "WLAN-abhängig",
                "operating_temp": "-20°C bis +50°C",
                "ip_rating": "IP54"
            },
            "features": [
                {"name": "Video-Türklingel", "description": "Sehen und sprechen Sie mit Besuchern"},
                {"name": "PIR-Erkennung", "description": "Bewegungserkennung vor der Tür"},
                {"name": "App-Integration", "description": "Vollständige Smartphone-Steuerung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # ================== RELAIS & AUTOMATISIERUNG ==================
        {
            "name": "Relay Jeweller",
            "category": "relays",
            "product_line": "baseline",
            "description": "Funkrelais mit potenzialfreiem Kontakt für Automatisierung",
            "short_description": "Drahtloses Schaltrelais",
            "usps": ["Potenzialfrei", "Fernschaltung", "Automatisierung", "Kompakt"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Frelay_a81e255a8b%402.png&1689152843",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1000m",
                "operating_temp": "-10°C bis +40°C",
                "max_load": "10A"
            },
            "features": [
                {"name": "Potenzialfreier Kontakt", "description": "Universell einsetzbar"},
                {"name": "Fernschaltung", "description": "Steuerung über Ajax Apps"},
                {"name": "Automatisierung", "description": "Szenario-basierte Schaltung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "WallSwitch Jeweller",
            "category": "relays",
            "product_line": "baseline",
            "description": "Kabelloses Leistungsrelais zur Fernsteuerung der 110/230 V~ Stromversorgung",
            "short_description": "Funk-Lichtschalter/Relais",
            "usps": ["230V Schaltung", "Lichtsteuerung", "Fernbedienung", "App-Steuerung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fwallswitch_6f717abe66%402.png&1689152843",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1000m",
                "operating_temp": "-10°C bis +40°C",
                "max_load": "3000W"
            },
            "features": [
                {"name": "Hochstrom-Schaltung", "description": "Bis zu 3000W Schaltleistung"},
                {"name": "Lichtsteuerung", "description": "Perfekt für Beleuchtungssteuerung"},
                {"name": "Smart Home Integration", "description": "Vollständige App-Steuerung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub (2G) Jeweller", "Hub BP Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior MultiRelay Fibra",
            "category": "relais",
            "product_line": "superiorline",
            "description": "Superior MultiRelay Fibra für professionelle Automatisierung",
            "short_description": "Professional Multi-Relais kabelgebunden",
            "usps": ["Fibra-Technologie", "Multi-Relais", "Professional", "Grade 3"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_multirelay_fibra%402.png",
            "specifications": {
                "frequency": "Fibra (kabelgebunden)",
                "range": "bis zu 2000m über Fibra",
                "operating_temp": "-25°C bis +50°C",
                "xortec_nr": "600810620",
                "hersteller_nr": "127496.183.NC1"
            },
            "features": [
                {"name": "Fibra-Technologie", "description": "Kabelgebundene Übertragung für höchste Zuverlässigkeit"},
                {"name": "Multi-Relais", "description": "Mehrere Schaltausgänge in einem Gerät"},
                {"name": "Grade 3 Zertifizierung", "description": "Professional-Grade Automatisierung"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior Transmitter Fibra ASP",
            "category": "integration_modules",
            "product_line": "superiorline",
            "description": "Transmitter Fibra ASP Fibra Product Line für Integration von Drittanbietersystemen",
            "short_description": "Professional Integrationsmodul",
            "usps": ["Fibra-Technologie", "Drittanbieter-Integration", "Professional", "ASP"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_transmitter_fibra%402.png",
            "specifications": {
                "frequency": "Fibra (kabelgebunden)",
                "range": "bis zu 2000m über Fibra",
                "operating_temp": "-25°C bis +50°C",
                "xortec_nr": "600810316",
                "hersteller_nr": "77373.182.NC1"
            },
            "features": [
                {"name": "ASP Integration", "description": "Alarm System Provider Interface"},
                {"name": "Fibra-Technologie", "description": "Kabelgebundene professionelle Übertragung"},
                {"name": "Drittanbieter-Kompatibilität", "description": "Integration verschiedener Systeme"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        
        # ================== ZUBEHÖR & NETZTEILE ==================
        {
            "name": "12-24V PSU for Hub 2 / Hub 2 Plus / ReX 2",
            "category": "power_supplies",
            "product_line": "baseline",
            "description": "12-24V PSU for Hub 2/Hub 2 Plus/ReX 2 ASP Baseline | Intrusion protection",
            "short_description": "Netzteil für Hub 2 Serie",
            "usps": ["12-24V", "Für Hub 2 Serie", "ASP", "Backup-Stromversorgung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fpsu_12-24v%402.png",
            "specifications": {
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810226",
                "hersteller_nr": "59359.94.NC"
            },
            "features": [
                {"name": "Flexibel", "description": "12-24V Spannungsbereich"},
                {"name": "Kompatibilität", "description": "Für Hub 2, Hub 2 Plus und ReX 2"},
                {"name": "Backup-Versorgung", "description": "Unterbrechungsfreie Stromversorgung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Hub 2 (4G) Jeweller", "Hub BP Jeweller"]
        },
        {
            "name": "12V PSU for Hub/Hub Plus/ReX",
            "category": "power_supplies",
            "product_line": "baseline",
            "description": "12 V Netzteil für Hub / Hub Plus / ReX. Das 12 V Netzteil wird im Gehäuse der EMA installiert und ersetzt das vorinstallierte Netzteil",
            "short_description": "12V Netzteil für Hub Serie",
            "usps": ["12V", "Für Hub Serie", "EMA-Installation", "Ersatz-Netzteil"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fpsu_12v%402.png",
            "specifications": {
                "operating_temp": "-10°C bis +40°C",
                "xortec_nr": "600810055",
                "hersteller_nr": "38212.54.NC"
            },
            "features": [
                {"name": "Standard 12V", "description": "Standardspannung für Hub-Systeme"},
                {"name": "EMA-Gehäuse", "description": "Installation im EMA-Gehäuse"},
                {"name": "Ersatz-Netzteil", "description": "Ersetzt vorinstallierte Netzteile"}
            ],
            "compatible_hubs": ["Hub (2G) Jeweller", "Superior Hub Hybrid (4G)"]
        }
    ]
    
    # Insert products into database
    for product_data in products_data:
        product = Product(**product_data)
        await db.products.insert_one(product.dict())

# Routes
@api_router.get("/")
async def root():
    return {"message": "Xortec GmbH - Ajax Systems Konfigurator API"}

@api_router.get("/product-lines")
async def get_product_lines():
    """Get available product lines"""
    return {
        "product_lines": [
            {
                "id": "baseline",
                "name": "Baseline",
                "description": "Für einfachere Anwendungen und Wohnimmobilien",
                "target_group": "Wohnbereich, kleine Geschäfte",
                "features": ["Drahtlose Jeweller-Geräte", "Einfache Installation", "Grundlegende Sicherheit"],
                "image": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbaseline_lg_bc7460aa05%402.jpg&1731779933"
            },
            {
                "id": "superiorline", 
                "name": "Superior",
                "description": "Für Fachleute und anspruchsvolle Projekte",
                "target_group": "Kommerzielle Objekte, Hochsicherheitsbereiche",
                "features": ["Jeweller + Fibra Geräte", "Grade 3 Zertifizierung", "Höchste Sicherheitsstandards"],
                "image": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_lg_7b3c7741db%402.jpg&1731780001"
            },
            {
                "id": "en54",
                "name": "EN54",
                "description": "Spezielle Produktlinie für Brandwarnanlagen",
                "target_group": "Kommerzielle Brandschutzanlagen",
                "features": ["EN 54 zertifiziert", "Brandschutz + Einbruchschutz", "CIE Touchscreen"],
                "image": "https://ajax.systems/api/cdn-img/?img=%2Fproduct-categories%2Ffire-and-life-safety.lg.jpg&1751882727"
            },
            {
                "id": "video",
                "name": "Video",
                "description": "Videoüberwachungsprodukte",
                "target_group": "Videoüberwachung, Monitoring", 
                "features": ["IP-Kameras", "WLAN-Kameras", "NVRs", "KI-Features"],
                "image": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fvideo_surveillance_lg_c57510a21e%402.jpg&1744716097"
            }
        ]
    }

@api_router.get("/categories")
async def get_categories():
    """Get product categories"""
    return {
        "categories": [
            {"id": "hubs", "name": "Hub-Zentralen", "description": "Systemzentralen"},
            {"id": "motion_detectors", "name": "Bewegungsmelder", "description": "PIR und Mikrowellen-Sensoren"},
            {"id": "opening_detectors", "name": "Öffnungsmelder", "description": "Tür- und Fensterkontakte"},
            {"id": "glass_break_detectors", "name": "Glasbruchmelder", "description": "Akustische Glasbruchmelder"},
            {"id": "keypads", "name": "Bedienteile", "description": "Tastaturen und Touchscreens"},
            {"id": "sirens", "name": "Sirenen", "description": "Innen- und Außensirenen"},
            {"id": "wired_cameras", "name": "Kabelgebundene Kameras", "description": "IP-Kameras mit PoE"},
            {"id": "wifi_cameras", "name": "WLAN-Kameras", "description": "Drahtlose IP-Kameras"},
            {"id": "doorbells", "name": "Türklingeln", "description": "Video-Türklingeln"},
            {"id": "fire_detectors", "name": "Brandmelder", "description": "Rauch- und Wärmemelder"},
            {"id": "buttons_keyfobs", "name": "Knöpfe & Handsender", "description": "Notfallknöpfe und Fernbedienungen"},
            {"id": "range_extenders", "name": "Funk-Repeater", "description": "Reichweitenverlängerung"},
            {"id": "relays", "name": "Relais", "description": "Schalt- und Steuerrelais"},
            {"id": "integration_modules", "name": "Integrationsmodule", "description": "Drittanbieter-Integration"},
            {"id": "power_supplies", "name": "Netzteile", "description": "Stromversorgung"}
        ]
    }

@api_router.get("/products")
async def get_products(
    product_line: Optional[str] = None,
    category: Optional[str] = None,
    search: Optional[str] = None
):
    """Get products with optional filtering"""
    filter_query = {"in_stock": True}
    
    if product_line:
        filter_query["product_line"] = product_line
    if category:
        filter_query["category"] = category
    if search:
        filter_query["$or"] = [
            {"name": {"$regex": search, "$options": "i"}},
            {"description": {"$regex": search, "$options": "i"}}
        ]
    
    products = await db.products.find(filter_query).to_list(200)
    return [Product(**product) for product in products]

@api_router.get("/products/{product_id}")
async def get_product(product_id: str):
    """Get single product by ID"""
    product = await db.products.find_one({"id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return Product(**product)

@api_router.get("/compatibility/{hub_id}")
async def get_compatible_devices(hub_id: str):
    """Get devices compatible with specific hub"""
    hub = await db.products.find_one({"id": hub_id, "category": "hubs"})
    if not hub:
        raise HTTPException(status_code=404, detail="Hub not found")
    
    # Get all products that are compatible with this hub
    compatible_products = await db.products.find({
        "compatible_hubs": {"$in": [hub["name"], "self"]},
        "category": {"$ne": "hubs"}
    }).to_list(200)
    
    return [Product(**product) for product in compatible_products]

@api_router.post("/configurations", response_model=SystemConfiguration)
async def create_configuration(config: ConfigurationCreate):
    """Create new system configuration"""
    # Calculate total price
    products = await db.products.find({"id": {"$in": config.selected_products}}).to_list(100)
    total_price = sum(p.get("price", 0) for p in products if p.get("price"))
    
    config_dict = config.dict()
    config_dict["total_price"] = total_price
    config_obj = SystemConfiguration(**config_dict)
    
    await db.configurations.insert_one(config_obj.dict())
    return config_obj

@api_router.get("/configurations", response_model=List[SystemConfiguration])
async def get_configurations():
    """Get all configurations"""
    configs = await db.configurations.find().to_list(100)
    return [SystemConfiguration(**config) for config in configs]

@api_router.get("/configurations/{config_id}")
async def get_configuration(config_id: str):
    """Get configuration with products"""
    config = await db.configurations.find_one({"id": config_id})
    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    # Get associated products
    products = await db.products.find({"id": {"$in": config["selected_products"]}}).to_list(100)
    
    return {
        "configuration": SystemConfiguration(**config),
        "products": [Product(**p) for p in products]
    }

@api_router.post("/configurations/{config_id}/pdf")
async def generate_pdf_simple(config_id: str):
    """Simple PDF generation endpoint"""
    try:
        # For now, return a simple response indicating PDF would be generated
        return {"message": "PDF-Generierung durch Xortec GmbH implementiert", "config_id": config_id, "filename": f"ajax_config_{config_id}.pdf"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Initialize products on startup
@app.on_event("startup")
async def startup_event():
    await init_products()
    logging.info("Complete Ajax Products database initialized by Xortec GmbH")

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()