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

# Initialize products data
async def init_products():
    # Check if products already exist
    existing_products = await db.products.count_documents({})
    if existing_products > 0:
        return
    
    # Ajax products data based on real specifications
    products_data = [
        # Hub-Zentralen
        {
            "name": "Hub 2 Plus Jeweller",
            "category": "hubs",
            "product_line": "baseline",
            "description": "Kabellose Hub-Zentrale mit Fotoverifizierung. Anschließbar über WLAN, Ethernet und zwei SIM-Karten (2G/3G/LTE)",
            "short_description": "Zentrale mit Fotoverifizierung und mehrfacher Konnektivität",
            "usps": ["Fotoverifizierung", "WLAN + Ethernet + 2x SIM", "Bis zu 200 Geräte", "4 Kommunikationskanäle"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 2000m",
                "max_devices": 200,
                "communication": ["WLAN", "Ethernet", "2G/3G/LTE"],
                "operating_temp": "-10°C bis +40°C",
                "dimensions": "163 × 163 × 36 mm"
            },
            "features": [
                {"name": "Fotoverifizierung", "description": "Automatische Fotoaufnahme bei Alarm"},
                {"name": "Mehrfach-Konnektivität", "description": "4 unabhängige Kommunikationskanäle"},
                {"name": "64 Automatisierungsszenarien", "description": "Intelligente Systemautomatisierung"}
            ],
            "compatible_hubs": ["self"]
        },
        {
            "name": "Superior Hub Hybrid (4G)",
            "category": "hubs",
            "product_line": "superiorline",
            "description": "Hybride Hub-Zentrale mit Fotoverifizierung. Funktioniert mit Fibra- und Jeweller-Geräten. Anschließbar über Ethernet und zwei SIM-Karten (2G/3G/LTE)",
            "short_description": "Hybrid-Zentrale für Jeweller + Fibra Geräte",
            "usps": ["Fibra + Jeweller Support", "Bis zu 400 Geräte", "Professionelle Grade", "Höchste Sicherheitsstandards"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_hybrid_black_eb78efaa15%402.png&1696515890",
            "specifications": {
                "frequency": "868 MHz (Jeweller) + Fibra (kabelgebunden)",
                "range": "bis zu 2000m (Jeweller)",
                "max_devices": 400,
                "communication": ["Ethernet", "2G/3G/LTE"],
                "operating_temp": "-25°C bis +50°C",
                "dimensions": "163 × 163 × 36 mm"
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
            "description": "Brandwarnzentrale mit Unterstützung von Einbruchschutzgeräten",
            "short_description": "EN54 zertifizierte Brandwarnzentrale",
            "usps": ["EN 54 zertifiziert", "Brandschutz + Einbruchschutz", "Kommerzielle Anwendungen", "Touchscreen CIE"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fen54_fire_hub_jeweller_black_fd80de7c0f%402.png&1753716121",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 2000m",
                "max_devices": 200,
                "communication": ["Ethernet", "GSM"],
                "operating_temp": "-10°C bis +55°C"
            },
            "features": [
                {"name": "EN 54 Zertifizierung", "description": "Vollständig zertifiziert für kommerzielle Brandschutzanlagen"},
                {"name": "Kombinierter Schutz", "description": "Brandschutz und Einbruchschutz in einem System"},
                {"name": "CIE Touchscreen", "description": "Zentrale Bedieneinheit mit Touchscreen"}
            ],
            "compatible_hubs": ["self"]
        },
        
        # Bewegungsmelder - Baseline
        {
            "name": "MotionProtect Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "Kabelloser IR-Bewegungsmelder",
            "short_description": "Zuverlässiger PIR-Bewegungsmelder für den Innenbereich",
            "usps": ["12m Erfassungsreichweite", "7 Jahre Batterielaufzeit", "Haustier-Immunität bis 20kg", "SmartDetect Algorithmus"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_7e25a60ef8%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "ip_rating": "IP50",
                "dimensions": "65 × 65 × 65 mm"
            },
            "features": [
                {"name": "SmartDetect", "description": "Intelligente Bewegungserkennung mit Störungsfilter"},
                {"name": "Haustier-Immunität", "description": "Ignoriert Tiere bis 20kg und 50cm Höhe"},
                {"name": "Sabotage-Schutz", "description": "Erkennt Manipulationsversuche sofort"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Superior Hub Hybrid (4G)"]
        },
        {
            "name": "MotionCam Jeweller",
            "category": "motion_detectors",
            "product_line": "baseline",
            "description": "Kabelloser IR-Bewegungsmelder mit der Funktion Foto nach Alarm",
            "short_description": "Bewegungsmelder mit integrierter Kamera",
            "usps": ["Foto-Verifikation", "120° Bildwinkel", "Nachtsicht bis 5m", "Verschlüsselte Übertragung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotion_cam_jeweller_black_50c00ca247%402.png&1727442738",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 4 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "dimensions": "65 × 65 × 65 mm"
            },
            "features": [
                {"name": "Foto-Verifikation", "description": "Automatische Fotoaufnahme bei Alarmauslösung"},
                {"name": "Infrarot-Illumination", "description": "Klare Aufnahmen auch bei völliger Dunkelheit"},
                {"name": "Ende-zu-Ende-Verschlüsselung", "description": "Sichere Übertragung aller Bilddaten"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # Bewegungsmelder - Superior
        {
            "name": "Superior MotionProtect Plus Jeweller",
            "category": "motion_detectors",
            "product_line": "superiorline",
            "description": "Kabelloser IR-Bewegungsmelder mit zusätzlichem K-Band-Mikrowellensensor. Superior Edition",
            "short_description": "Dual-Technologie Bewegungsmelder (PIR + Mikrowelle)",
            "usps": ["Duale Sensorik", "Grade 3 Zertifizierung", "Anti-Masking", "Erweiterte Sabotage-Erkennung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmpspj_s_68b8826cc2%402.png&1688046815",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP50",
                "dimensions": "65 × 65 × 65 mm"
            },
            "features": [
                {"name": "Dual-Technologie", "description": "PIR + Mikrowellen-Sensor für höchste Zuverlässigkeit"},
                {"name": "Anti-Masking", "description": "Erkennt Versuche der Sensorabdeckung"},
                {"name": "Grade 3 Zertifizierung", "description": "Höchste Sicherheitsstufe nach EN 50131"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        {
            "name": "Superior MotionProtect G3 Fibra",
            "category": "motion_detectors", 
            "product_line": "superiorline",
            "description": "Kabelgebundener PIR-Bewegungsmelder mit Anti-Masking-System",
            "short_description": "Professioneller kabelgebundener PIR-Melder",
            "usps": ["Fibra-Technologie", "Anti-Masking System", "Sofortige Alarmübertragung", "Professionelle Installation"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fsuperior_motion_protect_g3_fibra_725c1f53cf%402.png&1751281966",
            "specifications": {
                "frequency": "Fibra (kabelgebunden)",
                "range": "bis zu 2000m über Fibra",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP50",
                "dimensions": "65 × 65 × 65 mm"
            },
            "features": [
                {"name": "Fibra-Technologie", "description": "Kabelgebundene Übertragung für höchste Zuverlässigkeit"},
                {"name": "Anti-Masking", "description": "Aktive Überwachung gegen Manipulationsversuche"},
                {"name": "Sofort-Alarm", "description": "Verzögerungsfreie Alarmübertragung"}
            ],
            "compatible_hubs": ["Superior Hub Hybrid (4G)"]
        },
        
        # Öffnungsmelder
        {
            "name": "DoorProtect Jeweller",
            "category": "opening_detectors",
            "product_line": "baseline",
            "description": "Kabelloser Öffnungsmelder mit Reedschalter",
            "short_description": "Kompakter Tür-/Fensterkontakt",
            "usps": ["7 Jahre Batterielaufzeit", "Ultrakleine Bauform", "Sabotage-Schutz", "Sofortige Benachrichtigung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_f565be9860%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "dimensions": "88 × 20 × 15 mm"
            },
            "features": [
                {"name": "Reed-Sensor", "description": "Hochzuverlässiger magnetischer Sensor"},
                {"name": "Kompaktdesign", "description": "Unauffällige Installation an Türen und Fenstern"},
                {"name": "Sabotage-Erkennung", "description": "Alarm bei Entfernung vom Montageort"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # Glasbruchmelder
        {
            "name": "GlassProtect Jeweller",
            "category": "glass_break_detectors", 
            "product_line": "baseline",
            "description": "Kabelloser Glasbruchmelder mit Mikrofon",
            "short_description": "Akustischer Glasbruchmelder",
            "usps": ["9m Erfassungsradius", "SmartDetect Algorithmus", "7 Jahre Batterielaufzeit", "Falschalarmschutz"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fglassprotect_bb2a29da00%402.png&1689152842",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1300m",
                "battery_life": "bis zu 7 Jahre",
                "operating_temp": "-10°C bis +40°C",
                "dimensions": "115 × 65 × 30 mm"
            },
            "features": [
                {"name": "Akustische Erkennung", "description": "Erkennt charakteristische Glasbruchgeräusche"},
                {"name": "SmartDetect", "description": "Filterung von Störgeräuschen und Falschalarmen"},
                {"name": "Großer Erfassungsbereich", "description": "Schutz mehrerer Fenster mit einem Gerät"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # Bedienteile
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
                "operating_temp": "0°C bis +40°C",
                "dimensions": "150 × 103 × 25 mm"
            },
            "features": [
                {"name": "Touchscreen-Display", "description": "Intuitive Bedienung über 4.3\" Farbdisplay"},
                {"name": "Multi-Authentifizierung", "description": "Code, RFID-Karte, Smartphone oder Schlüsselanhänger"},
                {"name": "System-Status", "description": "Anzeige aller Systemzustände und Ereignisse"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # Sirenen
        {
            "name": "StreetSiren DoubleDeck Jeweller",
            "category": "sirens",
            "product_line": "baseline",
            "description": "Kabellose Sirene mit Halterung für eine Marken/Logo-Frontplatte",
            "short_description": "Außensirene mit LED-Blitzlicht",
            "usps": ["113 dB Lautstärke", "Brandplate-Support", "LED-Blitzlicht", "5 Jahre Batterielaufzeit"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstreetsiren_doubledeck_aa7ec7f313%402.png&1716365399",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1500m",
                "battery_life": "bis zu 5 Jahre",
                "operating_temp": "-25°C bis +50°C",
                "ip_rating": "IP54",
                "dimensions": "307 × 210 × 102 mm"
            },
            "features": [
                {"name": "Hohe Lautstärke", "description": "Bis zu 113 dB Schallleistung"},
                {"name": "LED-Signalgebung", "description": "Helles Blitzlicht als visuelle Warnung"},
                {"name": "Brandplate-Option", "description": "Individualisierung mit Firmenkennzeichnung"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # Video-Kameras
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
                "ip_rating": "IP66",
                "dimensions": "70 × 161 mm"
            },
            "features": [
                {"name": "5 MP Auflösung", "description": "Gestochen scharfe Videoqualität"},
                {"name": "KI-Erkennung", "description": "Intelligente Objekt- und Personenerkennung"},
                {"name": "TrueWDR", "description": "Optimale Bildqualität bei schwierigen Lichtverhältnissen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Superior Hub Hybrid (4G)"]
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
                "operating_temp": "0°C bis +40°C",
                "dimensions": "108 × 108 × 82 mm"
            },
            "features": [
                {"name": "WLAN-Konnektivität", "description": "Einfache Installation ohne Verkabelung"},
                {"name": "PIR-Integration", "description": "Kombiniert Video mit präziser Bewegungserkennung"},
                {"name": "Smart Features", "description": "KI-basierte Analyse und Benachrichtigungen"}
            ],
            "compatible_hubs": ["Hub 2 Plus Jeweller", "Superior Hub Hybrid (4G)"]
        },
        
        # Brandschutz EN54
        {
            "name": "FireProtect 2 RB (Heat/Smoke) Jeweller",
            "category": "fire_detectors",
            "product_line": "en54",
            "description": "Kabelloser Rauch- und Wärmemelder mit austauschbaren Batterien",
            "short_description": "EN54-zertifizierter Rauch-/Wärmemelder",
            "usps": ["EN 54-7/5 zertifiziert", "Dual-Sensor-Technologie", "10 Jahre Batterielaufzeit", "Professionelle Anwendung"],
            "image_url": "https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ffireprotect_2_rb_black_a1b2c3d4e5%402.png&1688287078",
            "specifications": {
                "frequency": "868 MHz (Jeweller)",
                "range": "bis zu 1700m", 
                "battery_life": "bis zu 10 Jahre",
                "operating_temp": "-10°C bis +55°C",
                "dimensions": "65 × 65 × 65 mm"
            },
            "features": [
                {"name": "EN 54 Zertifizierung", "description": "Vollständig zertifiziert für kommerzielle Brandschutzanlagen"},
                {"name": "Dual-Sensor", "description": "Kombinierte Rauch- und Temperaturerkennung"},
                {"name": "Austauschbare Batterie", "description": "Wartungsfreundliches Design"}
            ],
            "compatible_hubs": ["EN54 Fire Hub Jeweller"]
        }
    ]
    
    # Insert products into database
    for product_data in products_data:
        product = Product(**product_data)
        await db.products.insert_one(product.dict())

# Routes
@api_router.get("/")
async def root():
    return {"message": "Ajax Systems Konfigurator API"}

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
            {"id": "fire_detectors", "name": "Brandmelder", "description": "Rauch- und Wärmemelder"}
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
    
    products = await db.products.find(filter_query).to_list(100)
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

# Initialize products on startup
@app.on_event("startup")
async def startup_event():
    await init_products()
    logging.info("Products initialized")

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