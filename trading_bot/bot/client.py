from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()  # 👈 THIS IS REQUIRED

class BinanceClient:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        print("DEBUG:", api_key, api_secret)  # 👈 TEMP DEBUG

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client