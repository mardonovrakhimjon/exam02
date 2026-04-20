def calculate_cart(cart: dict) -> int:
    total_sum = 0
    for item in cart.values():
        total_sum += item['price'] * item['quantity']
    return total_sum

cart = {
    'non': {'price': 3000, 'quantity': 2},
    'sut': {'price': 8000, 'quantity': 1},
    'olma': {'price': 5000, 'quantity': 5}
}

print(calculate_cart(cart))
