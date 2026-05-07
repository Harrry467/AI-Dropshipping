from langchain.tools import tool
from typing import Optional
import random

@tool
def find_winning_product(category: Optional[str] = "kitchen gadgets") -> dict:
    """
    Searches AliExpress/Amazon for a trending dropshippable product.
    Returns a dict with name, price, supplier_url, image_url, description.
    """
    # TODO: Implement scraping or use Apify/AliExpress API
    # For now, return a mock product for demonstration
    products = [
        {
            "name": "Self-Stirring Mug",
            "price": 12.99,
            "supplier_url": "https://aliexpress.com/item/123456.html",
            "image_url": "https://placeholder.com/mug.jpg",
            "description": "Never stir manually again! Magnetic self-stirring mug, perfect for coffee lovers.",
            "supplier": "AliExpress",
            "shipping_days": 10,
        },
        # add more mock products...
    ]
    return random.choice(products)
