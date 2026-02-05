orders = [
    (101, 1000, "completed"),
    (102, -500, "completed"),
    (103, 700, "cancelled"),
    (104, 0, "completed"),
    (105, 300, "pending"),
    (106, 1200, "completed")
]

for order_id, amount, status in orders:
    if status!="completed":
        continue
    if amount<=0:
        continue
    print(f"Order ID: {order_id} | Amount: {amount}")
