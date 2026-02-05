orders = [
    ("apple", 2, 50),
    ("banana", 5, 10),
    ("apple", 3, 50),
    ("orange", 4, 30),
    ("banana", 2, 10)
]

summary={}
for product, quantity, price in orders:
    revenue=quantity*price
    if product not in summary:
        summary[product] = {
            "quantity": quantity,
            "revenue": revenue
        }
    else:
        summary[product]["quantity"] += quantity
        summary[product]["revenue"] += revenue

for product, data in summary.items():
    print(
        f"Product: {product} | "
        f"Quantity Sold: {data['quantity']} | "
        f"Revenue: {data['revenue']}"
    )
