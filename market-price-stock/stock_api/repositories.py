
from decimal import Decimal
from .models import StockPrice
import os
import requests
from logging import Logger
logger = Logger(__name__)

API_TOKEN = os.getenv("API_KEY")


class StockPriceRepository:
    def get_current_stock_price(self, symbol: str, quantity: str):
        try:
            response = requests.get(
                "https://finnhub.io/api/v1/quote",
                params={"token": API_TOKEN, "symbol": symbol},
            )
            response.raise_for_status()
            json_data = response.json()
            current_price = json_data["c"]
            if not current_price:
                return {
                    "status": False,
                    "reason": "Invalid symbol"
                }
            
            decimal_price = Decimal(current_price * int(quantity))  
            price = decimal_price.quantize(Decimal('0.00'))  
            stock_price = {
                "status": True,
                "stock_price": {
                    "symbol": symbol,
                    "quantity": quantity,
                    "current_price": price,
                }
            }
            return stock_price
        except Exception as e:
            return {
                "status": False,
                "reason": "API error"
            }
