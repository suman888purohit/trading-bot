# check_order.py - Check order status
import os
from dotenv import load_dotenv
from binance.client import Client

# Load environment variables
load_dotenv()

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

print(f"API Key loaded: {'Yes' if API_KEY else 'No'}")
print(f"API Secret loaded: {'Yes' if API_SECRET else 'No'}")

# Initialize client for Demo
client = Client(API_KEY, API_SECRET)
client.API_URL = 'https://demo-fapi.binance.com/api'

# Get account info
try:
    account = client.futures_account()
    print("\n✅ Account Info Retrieved:")
    print(f"Total Wallet Balance: {account.get('totalWalletBalance', 'N/A')} USDT")
    print(f"Available Balance: {account.get('availableBalance', 'N/A')} USDT")
    
    # Check your order
    order = client.futures_get_order(symbol='BTCUSDT', orderId=13095899434)
    print(f"\n📊 Order Status:")
    print(f"Order ID: {order['orderId']}")
    print(f"Status: {order['status']}")
    print(f"Executed Quantity: {order['executedQty']}")
    print(f"Average Price: {order.get('avgPrice', 'N/A')}")
    
except Exception as e:
    print(f"\n❌ Error: {e}")