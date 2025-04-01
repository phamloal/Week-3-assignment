def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after discount, the original price
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Define user input
discount_amount = [
    (100, 25),  # Expected output: 75.0
    (50, 10),   # Expected output: 50.0
    (200, 20),  # Expected output: 160.0
    (150, 5)    # Expected output: 150.0
]

# Run discount_amount
for price, discount in discount_amount:
    final_price = calculate_discount(price, discount)
    print(f"Original Price: ksh{price}, Discount: {discount}%, Final Price: ksh{final_price:.2f}")
