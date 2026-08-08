from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, ValidationError

# 1. Define a nested model
class ProductItem(BaseModel):
    product_id: int
    quantity: int = Field(gt=0, description="Quantity must be greater than 0")
    price: float

# 2. Define the main model
class Order(BaseModel):
    # Required field
    order_id: str
    
    # Required field with built-in Pydantic email validation
    customer_email: EmailStr
    
    # Optional field with a default value
    status: str = "pending"
    
    # Nested list of other Pydantic models
    items: List[ProductItem]
    
    # Optional field that defaults to None
    discount_code: Optional[str] = None
    
    # Field with automatic timestamp fallback if not provided
    created_at: datetime = Field(default_factory=datetime.utcnow)

# ==========================================
# Example Usage & Validation
# ==========================================

# Valid raw data (simulating an API request or database record)
valid_data = {
    "order_id": "ORD-12345",
    "customer_email": "user@example.com",
    "items": [
        {"product_id": 101, "quantity": 2, "price": 29.99},
        {"product_id": 102, "quantity": 1, "price": 9.99}
    ]
}

try:
    # Parse and validate a dictionary
    order = Order.model_validate(valid_data)
    
    # Access fields using dot notation
    print(f"Order ID: {order.order_id}")
    print(f"First Item Price: {order.items[0].price}")
    print(f"Created At: {order.created_at}")

    # Export back to a Python dictionary
    order_dict = order.model_dump()
    
    # Export to a JSON string
    order_json = order.model_dump_json()

except ValidationError as e:
    print("Validation failed!")
    print(e.json())

# ==========================================
# Example of Data Coercion & Validation Failure
# ==========================================

invalid_data = {
    "order_id": "ORD-99999",
    "customer_email": "not-an-email",  # Invalid email format
    "items": [
        {"product_id": 103, "quantity": 0, "price": "15.50"}  # Quantity must be > 0. Price '15.50' (string) will be coerced to float 15.50 automatically.
    ]
}

print("\n--- Testing Invalid Data ---")
try:
    Order.model_validate(invalid_data)
    
except ValidationError as e:
    # Pydantic captures all errors at once rather than stopping at the first one
    print(e)