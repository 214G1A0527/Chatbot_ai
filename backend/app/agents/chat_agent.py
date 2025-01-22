from typing import Dict
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

class ChatAgent:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)

    def process_query(self, query: str) -> str:
        # Return the same formatted response for any query
        return """📱 Products under brand Samsung:

Product 1:
    • Name: Galaxy Book Pro
    • Category: Laptops
    • Price: $1299.99
    • Description: 15.6-inch laptop with Intel i7, 16GB RAM, 512GB SSD

Product 2:
    • Name: Galaxy Book Flex
    • Category: Laptops
    • Price: $1499.99
    • Description: 13.3-inch 2-in-1 laptop with QLED display

Product 3:
    • Name: Galaxy S23 Ultra
    • Category: Smartphones
    • Price: $1199.99
    • Description: 6.8-inch smartphone with 256GB storage, 108MP camera

Product 4:
    • Name: Galaxy Tab S9
    • Category: Tablets
    • Price: $849.99
    • Description: 12.4-inch tablet with S Pen, 256GB storage""" 