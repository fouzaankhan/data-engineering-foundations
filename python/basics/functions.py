orders = [
    (1000, 10),
    (500, 5),
    (2000, 20),
    (-300, 10)
]

def final_price(amount, discount):
    """
    Calculates final price and raises ValueError for invalid inputs.
    """
    if amount < 0 or discount < 0 or discount > 100:
        raise ValueError("Invalid amount or discount")
    return amount - (amount * discount / 100)

for amount, discount in orders:
    try:
        price = final_price(amount, discount)
        print(f"Final Price: {price:.2f}")
    except ValueError as e:
        print(f"Error for order (amount={amount}, discount={discount}): {e}")
