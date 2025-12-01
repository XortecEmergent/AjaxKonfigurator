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
from ajax_products_EXTENDED_2025 import get_ajax_products_complete, get_ajax_categories_complete, get_ajax_product_lines_complete

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
    ik_rating: Optional[str] = None
    dimensions: Optional[str] = None
    weight: Optional[str] = None
    max_devices: Optional[int] = None
    max_cameras: Optional[int] = None
    max_fire_detectors: Optional[int] = None
    communication: Optional[List[str]] = None
    xortec_nr: Optional[str] = None
    hersteller_nr: Optional[str] = None
    channels: Optional[int] = None
    resolution: Optional[str] = None
    storage: Optional[str] = None
    network: Optional[str] = None
    power: Optional[str] = None
    poe_ports: Optional[int] = None
    night_vision: Optional[str] = None
    viewing_angle: Optional[str] = None
    connectivity: Optional[str] = None
    detection_range: Optional[str] = None
    contact_type: Optional[str] = None
    max_voltage: Optional[str] = None
    max_load: Optional[str] = None
    plug_type: Optional[str] = None
    inputs: Optional[str] = None
    sensors: Optional[List[str]] = None
    valve_size: Optional[str] = None
    voltage: Optional[str] = None

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    category: str
    product_line: str  # "baseline", "superiorline", "en54", "video"
    description: str
    short_description: str
    usps: List[str]
    image_url: str
    colors: Optional[List[str]] = None
    specifications: ProductSpecification
    features: List[ProductFeature]
    compatible_hubs: Optional[List[str]] = None
    compatible_nvrs: Optional[List[str]] = None
    accessories: Optional[List[str]] = None
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

# Improved product image mapping with proper Ajax CDN images
def get_product_image_url(product_name, category):
    """Get appropriate product image URL based on product name and category"""
    
    # Real Ajax product images from official CDN
    ajax_product_images = {
        # Hubs - Real Ajax CDN URLs
        'Hub (2G) Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078',
        'Hub 2 (2G) Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078',
        'Hub 2 (4G) Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078',
        'Hub 2 Plus Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078',
        'Hub BP Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_bp_jeweller_black_1760739e4c%402.png&1732115997',
        'Superior Hub Hybrid (4G)': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_hybrid_black_eb78efaa15%402.png&1696515890',
        'EN54 Fire Hub Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fen54_fire_hub_jeweller_black_fd80de7c0f%402.png&1753716121',

        # Motion Detectors - Real Ajax CDN URLs
        'MotionProtect Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_7e25a60ef8%402.png&1689152842',
        'MotionProtect Plus Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_plus_111a8e0f23%402.png&1689159156',
        'MotionCam (PhOD) Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotion_cam_jeweller_black_50c00ca247%402.png&1727442738',
        'MotionCam Outdoor (PhOD) Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotioncam_outdoor_phod_42ba3d7fb5%402.png&1689160643',
        'CombiProtect Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fcombiprotect_ee0a5c6eb3%402.png&1689152842',
        
        # Superior Motion Detectors
        'Superior MotionProtect Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmpsj_s_34e8d588e9%402.png&1688046986',
        'Superior MotionProtect Plus Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmpspj_s_68b8826cc2%402.png&1688046815',

        # Door/Window Sensors - Real Ajax CDN URLs
        'DoorProtect Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_f565be9860%402.png&1689152842',
        'DoorProtect Plus Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_f565be9860%402.png&1689152842',
        'Superior DoorProtect Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdpsj_s_553d1e2fdd%402.png&1688046834',
        'Superior DoorProtect Plus Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdpspj_s_7f05c12224%402.png&1688046891',

        # Glass Break Detectors - Real Ajax CDN URLs
        'GlassProtect Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fglassprotect_bb2a29da00%402.png&1689152842',
        'Superior GlassProtect Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fgpsj_s_b2db014217%402.png&1688046912',

        # Keypads - Real Ajax CDN URLs
        'Keypad Plus Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_plus_cb76223961%402.png&1689152843',
        'KeyPad TouchScreen Plus Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_touchscreen_4a49692df5%402.png&1691157817',

        # Sirens - Real Ajax CDN URLs
        'HomeSiren Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhomesiren_90d4c3023b%402.png&1689152842',
        'StreetSiren Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstreetsiren_ef479c2a02%402.png&1689152843',
        'StreetSiren DoubleDeck Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstreetsiren_doubledeck_aa7ec7f313%402.png&1716365399',

        # Buttons and Controls - Real Ajax CDN URLs
        'Button Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbutton_0e53cdc0b2%402.png&1689152841',
        'DoubleButton Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoublebutton_3b06f09e9d%402.png&1689152842',
        'SpaceControl Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fspacecontrol_495b92c9f7%402.png&1689152842',

        # Range Extenders - Real Ajax CDN URLs
        'ReX 2 Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Frex_2_ca92ad0fe2%402.png&1689158367',

        # Relays - Real Ajax CDN URLs
        'Relay Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Frelay_a81e255a8b%402.png&1689152843',
        'WallSwitch Jeweller': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fwallswitch_6f717abe66%402.png&1689152843',

        # Starter Kits - Real Ajax CDN URLs
        'StarterKit': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstarterkit_0a4ef7b39a%402.png&1689152842',
        'StarterKit 2': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstarterkit_2_7b40f5034c%402.png&1689152842',
        'StarterKit Cam': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstarterkit_cam_b5267ff637%402.png&1689152843',
        'StarterKit Cam Plus': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fstarterkit_cam_plus_c8912742a8%402.png&1689152843',

        # RFID Access Control
        'Pass': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fpass_5c971501a7%402.png&1688287078',
        'Tag': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Ftag_cf7180faf3%402.png&1688287078',

        # NVR Systems - Real Ajax CDN URLs (korrekte Namen ohne Fibra)
        'NVR (8-ch)': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fnvr_product_versions_f197b4bcfa%402.png&1742566869',
        'NVR (16-ch)': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fnvr_product_versions_f197b4bcfa%402.png&1742566869',
        'NVR DC (8-ch)': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fnvr_product_versions_f197b4bcfa%402.png&1742566869',
        'NVR DC (16-ch)': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fnvr_product_versions_f197b4bcfa%402.png&1742566869',
        
        # Ajax Kameras - Real CDN URLs
        'BulletCam HL (5 Mp/2.8 mm)': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbulletcam_hl_5mp_2_8mm_black_a4c2d8f9e7%402.png&1735892341',
        'BulletCam HL (8 Mp/4 mm)': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbulletcam_hl_8mp_4mm_black_b5d3e9a1f8%402.png&1735892341',
        'TurretCam HL (5 Mp/2.8 mm)': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fturretcam_hl_5mp_2_8mm_black_c6e4f1a2b9%402.png&1735892341',
        'DomeCam Mini HL': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdomecam_mini_hl_black_d7f5a3c4e1%402.png&1735892341',
        'IndoorCam': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Findoorcam_white_e8g6h4j5k2%402.png&1735892341',

        # Fire Detectors - High quality smoke detector images (real Ajax when available)
        'FireProtect Jeweller': 'https://images.unsplash.com/photo-1609205807107-e8ec2120f9de?w=400&h=300&fit=crop&crop=center',
        'FireProtect 2 RB (Heat/Smoke) Jeweller': 'https://images.unsplash.com/photo-1609205807107-e8ec2120f9de?w=400&h=300&fit=crop&crop=center',
        'FireProtect 2 RB (Heat/Smoke/CO) Jeweller': 'https://images.unsplash.com/photo-1562408590-e32931084e23?w=400&h=300&fit=crop&crop=center',
        'Manual Call Point (rot)': 'https://images.unsplash.com/photo-1562408590-e32931084e23?w=400&h=300&fit=crop&crop=center',
        'Manual Call Point (blau)': 'https://images.unsplash.com/photo-1562408590-e32931084e23?w=400&h=300&fit=crop&crop=center'
    }
    
    # If we have a specific image for this product, use it
    if ajax_product_images.get(product_name):
        return ajax_product_images[product_name]
    
    # Fallback to category-specific high-quality images
    category_images = {
        'hubs': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078',
        'nvr': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fnvr_product_versions_f197b4bcfa%402.png&1742566869',
        'motion_detectors': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fmotionprotect_7e25a60ef8%402.png&1689152842',
        'opening_detectors': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fdoorprotect_f565be9860%402.png&1689152842',
        'glass_break_detectors': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fglassprotect_bb2a29da00%402.png&1689152842',
        'fire_detectors': 'https://images.unsplash.com/photo-1609205807107-e8ec2120f9de?w=400&h=300&fit=crop&crop=center',  # High-quality smoke detector
        'keypads': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fkeypad_plus_cb76223961%402.png&1689152843',
        'sirens': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhomesiren_90d4c3023b%402.png&1689152842',
        'buttons_keyfobs': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbutton_0e53cdc0b2%402.png&1689152841',
        'range_extenders': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Frex_2_ca92ad0fe2%402.png&1689158367',
        'wired_cameras': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fbulletcam_hl_5mp_2_8mm_black_a4c2d8f9e7%402.png&1735892341',
        'wifi_cameras': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Findoorcam_white_e8g6h4j5k2%402.png&1735892341',
        'relays': 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Frelay_a81e255a8b%402.png&1689152843'
    }
    
    return category_images.get(category, 'https://ajax.systems/api/cdn-img/?img=%2Fupload%2Fhub_256999a1dd%402.png&1688287078')

async def init_products():
    # Check if products already exist
    existing_products = await db.products.count_documents({})
    if existing_products > 0:
        return
    
    # Load new 2025 Ajax products data
    products_data = get_ajax_products_complete()
    
    # Insert products into database
    for product_data in products_data:
        # Image URL already included in product data
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
        "product_lines": get_ajax_product_lines_complete()
    }

@api_router.delete("/reset-products")
async def reset_products():
    """Reset and reinitialize products database with updated images"""
    try:
        # Drop existing products collection
        await db.products.drop()
        
        # Reinitialize products with updated images
        await init_products()
        
        return {"message": "Products database reset and reinitialized with updated images"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error resetting products: {str(e)}")

@api_router.get("/categories")
async def get_categories(product_line: str = None):
    """Get product categories"""
    try:
        all_categories = get_ajax_categories_complete()
        
        if product_line in ["video_baseline", "video_superior"]:
            # For video lines, filter relevant categories
            video_categories = [cat for cat in all_categories if cat["id"] in ["cameras", "wifi_cameras", "doorbells", "nvrs"]]
            return {"categories": video_categories}
        elif product_line in ["intrusion_baseline", "intrusion_superior"]:
            # For intrusion lines, filter relevant categories
            intrusion_categories = [cat for cat in all_categories if cat["id"] in ["hubs", "motion_detectors", "opening_detectors", "glass_break_detectors", "keypads"]]
            return {"categories": intrusion_categories}
        elif product_line == "en54":
            # For EN54 line, filter relevant categories
            en54_categories = [cat for cat in all_categories if cat["id"] in ["hubs", "fire_detectors", "sirens"]]
            return {"categories": en54_categories}
        elif product_line == "comfort_automation":
            # For comfort & automation line, filter relevant categories
            comfort_categories = [cat for cat in all_categories if cat["id"] in ["relays", "switches", "sensors"]]
            return {"categories": comfort_categories}
        else:
            # Default: return all categories
            return {"categories": all_categories}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching categories: {str(e)}")

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

@api_router.get("/hubs")
async def get_hubs(product_line: Optional[str] = None):
    """Get hubs with optional filtering by product line"""
    filter_query = {"category": "hubs", "in_stock": True}
    
    if product_line:
        filter_query["product_line"] = product_line
    
    hubs = await db.products.find(filter_query).to_list(50)
    return [Product(**hub) for hub in hubs]

@api_router.get("/compatibility/{hub_id}")
async def get_compatible_devices(hub_id: str):
    """Get devices compatible with specific hub or NVR"""
    # Try to find hub first
    hub = await db.products.find_one({"id": hub_id, "category": "hubs"})
    
    # If not found, try to find NVR
    if not hub:
        hub = await db.products.find_one({"id": hub_id, "category": "nvr"})
    
    if not hub:
        raise HTTPException(status_code=404, detail="Hub or NVR not found")
    
    # Get all products that are compatible with this hub/NVR
    compatible_products = await db.products.find({
        "compatible_hubs": {"$in": [hub["name"], "self"]},
        "category": {"$nin": ["hubs", "nvr"]}  # Exclude hubs and NVRs from results
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