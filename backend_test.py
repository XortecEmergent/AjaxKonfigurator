#!/usr/bin/env python3
"""
Ajax Konfigurator Backend Test Suite
Tests all API endpoints for the Ajax Systems product configurator
"""

import requests
import json
import os
from typing import Dict, List, Any
import sys

# Get backend URL from environment
BACKEND_URL = "https://smart-security-8.preview.emergentagent.com/api"

class AjaxBackendTester:
    def __init__(self):
        self.base_url = BACKEND_URL
        self.test_results = []
        self.failed_tests = []
        
    def log_test(self, test_name: str, success: bool, message: str, details: Any = None):
        """Log test result"""
        result = {
            "test": test_name,
            "success": success,
            "message": message,
            "details": details
        }
        self.test_results.append(result)
        if not success:
            self.failed_tests.append(result)
        
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {test_name} - {message}")
        if details and not success:
            print(f"   Details: {details}")
    
    def test_api_root(self):
        """Test API root endpoint"""
        try:
            response = requests.get(f"{self.base_url}/", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if "Xortec GmbH" in data.get("message", ""):
                    self.log_test("API Root", True, "Root endpoint accessible with correct message")
                else:
                    self.log_test("API Root", False, "Root endpoint accessible but wrong message", data)
            else:
                self.log_test("API Root", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_test("API Root", False, f"Connection error: {str(e)}")
    
    def test_product_lines(self):
        """Test /api/product-lines endpoint"""
        try:
            response = requests.get(f"{self.base_url}/product-lines", timeout=10)
            if response.status_code == 200:
                data = response.json()
                product_lines = data.get("product_lines", [])
                
                # Check if all expected product lines are present
                expected_lines = ["baseline", "superiorline", "en54", "video"]
                found_lines = [pl["id"] for pl in product_lines]
                
                missing_lines = [line for line in expected_lines if line not in found_lines]
                if not missing_lines:
                    self.log_test("Product Lines", True, f"All 4 product lines found: {found_lines}")
                    
                    # Check structure of each product line
                    for pl in product_lines:
                        required_fields = ["id", "name", "description", "target_group", "features"]
                        missing_fields = [field for field in required_fields if field not in pl]
                        if missing_fields:
                            self.log_test("Product Lines Structure", False, f"Missing fields in {pl['id']}: {missing_fields}")
                        else:
                            self.log_test(f"Product Line {pl['id']}", True, f"Complete structure with {len(pl['features'])} features")
                else:
                    self.log_test("Product Lines", False, f"Missing product lines: {missing_lines}", found_lines)
            else:
                self.log_test("Product Lines", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_test("Product Lines", False, f"Connection error: {str(e)}")
    
    def test_categories(self):
        """Test /api/categories endpoint"""
        try:
            response = requests.get(f"{self.base_url}/categories", timeout=10)
            if response.status_code == 200:
                data = response.json()
                categories = data.get("categories", [])
                
                # Check expected categories
                expected_categories = [
                    "hubs", "motion_detectors", "opening_detectors", "glass_break_detectors",
                    "keypads", "sirens", "wired_cameras", "wifi_cameras", "doorbells",
                    "fire_detectors", "buttons_keyfobs", "range_extenders", "relays",
                    "integration_modules", "power_supplies"
                ]
                
                found_categories = [cat["id"] for cat in categories]
                missing_categories = [cat for cat in expected_categories if cat not in found_categories]
                
                if not missing_categories:
                    self.log_test("Categories", True, f"All {len(categories)} categories found")
                    
                    # Check structure
                    for cat in categories:
                        required_fields = ["id", "name", "description"]
                        missing_fields = [field for field in required_fields if field not in cat]
                        if missing_fields:
                            self.log_test("Category Structure", False, f"Missing fields in {cat['id']}: {missing_fields}")
                else:
                    self.log_test("Categories", False, f"Missing categories: {missing_categories}", found_categories)
            else:
                self.log_test("Categories", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_test("Categories", False, f"Connection error: {str(e)}")
    
    def test_products(self):
        """Test /api/products endpoint"""
        try:
            response = requests.get(f"{self.base_url}/products", timeout=15)
            if response.status_code == 200:
                products = response.json()
                
                if isinstance(products, list) and len(products) > 0:
                    self.log_test("Products", True, f"Retrieved {len(products)} products")
                    
                    # Test product structure and Xortec article numbers
                    products_with_xortec = 0
                    hubs_found = []
                    
                    for product in products[:10]:  # Check first 10 products
                        # Check required fields
                        required_fields = ["id", "name", "category", "product_line", "description", "specifications"]
                        missing_fields = [field for field in required_fields if field not in product]
                        
                        if missing_fields:
                            self.log_test("Product Structure", False, f"Missing fields in {product.get('name', 'Unknown')}: {missing_fields}")
                        
                        # Check for Xortec article numbers
                        specs = product.get("specifications", {})
                        if specs.get("xortec_nr"):
                            products_with_xortec += 1
                        
                        # Collect hubs for compatibility testing
                        if product.get("category") == "hubs":
                            hubs_found.append(product)
                    
                    self.log_test("Xortec Article Numbers", True, f"{products_with_xortec}/10 products have Xortec numbers")
                    self.log_test("Hub Products", True, f"Found {len(hubs_found)} hub products")
                    
                    # Store hubs for compatibility testing
                    self.hubs_for_testing = hubs_found
                    
                else:
                    self.log_test("Products", False, "No products returned or invalid format", type(products))
            else:
                self.log_test("Products", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_test("Products", False, f"Connection error: {str(e)}")
    
    def test_product_filtering(self):
        """Test product filtering by product_line and category"""
        try:
            # Test filtering by product line
            response = requests.get(f"{self.base_url}/products?product_line=baseline", timeout=10)
            if response.status_code == 200:
                baseline_products = response.json()
                if isinstance(baseline_products, list):
                    self.log_test("Product Filter - Baseline", True, f"Found {len(baseline_products)} baseline products")
                    
                    # Verify all are baseline
                    non_baseline = [p for p in baseline_products if p.get("product_line") != "baseline"]
                    if non_baseline:
                        self.log_test("Product Filter Accuracy", False, f"Found {len(non_baseline)} non-baseline products in baseline filter")
                else:
                    self.log_test("Product Filter - Baseline", False, "Invalid response format")
            
            # Test filtering by category
            response = requests.get(f"{self.base_url}/products?category=hubs", timeout=10)
            if response.status_code == 200:
                hub_products = response.json()
                if isinstance(hub_products, list):
                    self.log_test("Product Filter - Hubs", True, f"Found {len(hub_products)} hub products")
                    
                    # Check hub capacities
                    hubs_with_capacity = 0
                    for hub in hub_products:
                        specs = hub.get("specifications", {})
                        if specs.get("max_devices"):
                            hubs_with_capacity += 1
                    
                    self.log_test("Hub Capacities", True, f"{hubs_with_capacity}/{len(hub_products)} hubs have max_devices defined")
                else:
                    self.log_test("Product Filter - Hubs", False, "Invalid response format")
                    
        except Exception as e:
            self.log_test("Product Filtering", False, f"Connection error: {str(e)}")
    
    def test_compatibility(self):
        """Test /api/compatibility/{hub_id} endpoint"""
        if not hasattr(self, 'hubs_for_testing') or not self.hubs_for_testing:
            self.log_test("Compatibility Test", False, "No hubs available for testing")
            return
        
        try:
            # Test with first available hub
            test_hub = self.hubs_for_testing[0]
            hub_id = test_hub["id"]
            hub_name = test_hub["name"]
            
            response = requests.get(f"{self.base_url}/compatibility/{hub_id}", timeout=10)
            if response.status_code == 200:
                compatible_devices = response.json()
                
                if isinstance(compatible_devices, list):
                    self.log_test("Compatibility Check", True, f"Found {len(compatible_devices)} devices compatible with {hub_name}")
                    
                    # Verify compatibility logic
                    invalid_compatibility = []
                    for device in compatible_devices[:5]:  # Check first 5
                        compatible_hubs = device.get("compatible_hubs", [])
                        if hub_name not in compatible_hubs and "self" not in compatible_hubs:
                            invalid_compatibility.append(device["name"])
                    
                    if invalid_compatibility:
                        self.log_test("Compatibility Logic", False, f"Invalid compatibility for: {invalid_compatibility}")
                    else:
                        self.log_test("Compatibility Logic", True, "Compatibility logic working correctly")
                        
                else:
                    self.log_test("Compatibility Check", False, "Invalid response format", type(compatible_devices))
            else:
                self.log_test("Compatibility Check", False, f"HTTP {response.status_code}", response.text)
                
        except Exception as e:
            self.log_test("Compatibility Check", False, f"Connection error: {str(e)}")
    
    def test_configurations(self):
        """Test configuration endpoints"""
        try:
            # First get some products to create a configuration
            response = requests.get(f"{self.base_url}/products?category=hubs", timeout=10)
            if response.status_code != 200:
                self.log_test("Configuration Test Setup", False, "Could not get products for configuration test")
                return
            
            products = response.json()
            if not products:
                self.log_test("Configuration Test Setup", False, "No products available for configuration test")
                return
            
            # Create a test configuration
            test_config = {
                "name": "Test Ajax Konfiguration",
                "description": "Testkonfiguration für Ajax System",
                "product_line": "baseline",
                "selected_products": [products[0]["id"]],  # Use first product
                "created_by": "Backend Tester"
            }
            
            # Test POST /configurations
            response = requests.post(
                f"{self.base_url}/configurations",
                json=test_config,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 200:
                created_config = response.json()
                config_id = created_config.get("id")
                
                if config_id:
                    self.log_test("Configuration Creation", True, f"Created configuration with ID: {config_id}")
                    
                    # Test GET /configurations
                    response = requests.get(f"{self.base_url}/configurations", timeout=10)
                    if response.status_code == 200:
                        configs = response.json()
                        if isinstance(configs, list) and len(configs) > 0:
                            self.log_test("Configuration List", True, f"Retrieved {len(configs)} configurations")
                        else:
                            self.log_test("Configuration List", False, "No configurations returned")
                    
                    # Test GET /configurations/{id}
                    response = requests.get(f"{self.base_url}/configurations/{config_id}", timeout=10)
                    if response.status_code == 200:
                        config_detail = response.json()
                        if "configuration" in config_detail and "products" in config_detail:
                            self.log_test("Configuration Detail", True, "Configuration detail with products retrieved")
                        else:
                            self.log_test("Configuration Detail", False, "Invalid configuration detail format")
                    else:
                        self.log_test("Configuration Detail", False, f"HTTP {response.status_code}")
                        
                else:
                    self.log_test("Configuration Creation", False, "No ID returned in created configuration")
            else:
                self.log_test("Configuration Creation", False, f"HTTP {response.status_code}", response.text)
                
        except Exception as e:
            self.log_test("Configuration Test", False, f"Connection error: {str(e)}")
    
    def test_specific_ajax_products(self):
        """Test for specific Ajax products mentioned in requirements"""
        try:
            response = requests.get(f"{self.base_url}/products", timeout=15)
            if response.status_code != 200:
                self.log_test("Ajax Products Check", False, "Could not retrieve products")
                return
            
            products = response.json()
            product_names = [p.get("name", "") for p in products]
            
            # Check for key Ajax products
            key_products = [
                "Hub 2 Plus Jeweller",
                "MotionProtect Jeweller", 
                "DoorProtect Jeweller",
                "FireProtect 2 RB (Heat/Smoke)",
                "EN54 Fire Hub Jeweller"
            ]
            
            found_products = []
            missing_products = []
            
            for key_product in key_products:
                if any(key_product in name for name in product_names):
                    found_products.append(key_product)
                else:
                    missing_products.append(key_product)
            
            if not missing_products:
                self.log_test("Key Ajax Products", True, f"All key products found: {found_products}")
            else:
                self.log_test("Key Ajax Products", False, f"Missing products: {missing_products}")
            
            # Check for Xortec article numbers in products
            products_with_xortec = 0
            total_checked = 0
            
            for product in products:
                specs = product.get("specifications", {})
                if specs.get("xortec_nr"):
                    products_with_xortec += 1
                total_checked += 1
            
            xortec_percentage = (products_with_xortec / total_checked * 100) if total_checked > 0 else 0
            self.log_test("Xortec Article Numbers", True, f"{products_with_xortec}/{total_checked} products ({xortec_percentage:.1f}%) have Xortec numbers")
            
        except Exception as e:
            self.log_test("Ajax Products Check", False, f"Connection error: {str(e)}")
    
    def run_all_tests(self):
        """Run all tests"""
        print(f"🚀 Starting Ajax Konfigurator Backend Tests")
        print(f"📡 Backend URL: {self.base_url}")
        print("=" * 60)
        
        # Run all tests
        self.test_api_root()
        self.test_product_lines()
        self.test_categories()
        self.test_products()
        self.test_product_filtering()
        self.test_compatibility()
        self.test_configurations()
        self.test_specific_ajax_products()
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        passed_tests = len([t for t in self.test_results if t["success"]])
        failed_tests = len(self.failed_tests)
        
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests*100):.1f}%")
        
        if self.failed_tests:
            print("\n🔍 FAILED TESTS DETAILS:")
            for test in self.failed_tests:
                print(f"❌ {test['test']}: {test['message']}")
                if test.get('details'):
                    print(f"   Details: {test['details']}")
        
        return failed_tests == 0

if __name__ == "__main__":
    tester = AjaxBackendTester()
    success = tester.run_all_tests()
    
    if success:
        print("\n🎉 All tests passed! Ajax Konfigurator Backend is working correctly.")
        sys.exit(0)
    else:
        print(f"\n⚠️  {len(tester.failed_tests)} tests failed. Please check the issues above.")
        sys.exit(1)