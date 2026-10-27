
# Product Catalogue Audit

products = [
    ("P101", 500, 20),
    ("P102", 1200, 5),
    ("P103", -300, 10),
    ("P104", 800, 0),
    ("P105", 1500, 3)
]

total_value = 0

print("Product Catalogue Audit")

for p in products:
    pid, price, stock = p

    print("\nProduct ID:", pid)

    # Detect invalid records
    if price <= 0 or stock < 0:
        print("Invalid Record")
        continue

    value = price * stock
    total_value += value

    print("Price:", price)
    print("Stock:", stock)
    print("Inventory Value:", value)

    # Replenishment check
    if stock < 10:
        print("Replenishment Required")

print("\nTotal Inventory Value:", total_value)
