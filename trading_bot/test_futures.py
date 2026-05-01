# test_futures.py - Test if API key has Futures permissions
import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Load API keys
load_dotenv()
API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

print("="*60)
print("API Key Permission Test")
print("="*60)

# Test 1: Basic connection
print("\n1. Testing basic API connection...")
try:
    client = Client(API_KEY, API_SECRET)
    print("   ✓ Basic connection successful")
except Exception as e:
    print(f"   ✗ Basic connection failed: {e}")
    exit()

# Test 2: Check if key has Futures permissions
print("\n2. Testing Futures API access...")
try:
    # This call specifically tests Futures permissions
    account_info = client.futures_account()
    print("   ✓ SUCCESS! API key has Futures permissions!")
    print(f"   Account Balance: ${account_info.get('totalWalletBalance', 'N/A')}")
    print(f"   Available Balance: ${account_info.get('availableBalance', 'N/A')}")
    
    # Test 3: Try to get a market price
    print("\n3. Testing market data access...")
    ticker = client.futures_symbol_ticker(symbol='BTCUSDT')
    print(f"   ✓ Current BTCUSDT price: ${ticker['price']}")
    
    print("\n" + "="*60)
    print("✅ ALL TESTS PASSED! Your bot is ready to trade!")
    print("="*60)
    print("\nYou can now run: python cli.py interactive")
    
except BinanceAPIException as e:
    print(f"   ✗ FAILED: {e.message}")
    print(f"   Error Code: {e.code}")
    
    if e.code == -2015:
        print("\n" + "="*60)
        print("🔧 SOLUTION: API key missing Futures permissions")
        print("="*60)
        print("\n1. Go to https://demo.binance.com")
        print("2. Click Profile Icon → API Management")
        print("3. Delete your current API key")
        print("4. Click 'Create API Key'")
        print("5. IMPORTANT: Check the box for 'Enable Futures'")
        print("6. Complete verification")
        print("7. Copy the NEW API key and Secret")
        print("8. Update your .env file with the new keys")
        print("9. Wait 2 minutes for activation")
        print("10. Run this test again")
    else:
        print(f"\nUnknown error. Please share this error code: {e.code}")
        
except Exception as e:
    print(f"   ✗ Unexpected error: {e}")