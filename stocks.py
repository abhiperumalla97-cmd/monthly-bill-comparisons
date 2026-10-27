

# Inventory Matrix Reconciliation

warehouses = ["Warehouse A", "Warehouse B", "Warehouse C"]
products = ["Laptop", "Mobile", "Tablet"]

# Available stock in each warehouse
stock = [
    [50, 30, 40],
    [20, 60, 25],
    [40, 20, 35]
]

# Required stock targets
target = [
    [40, 40, 30],
    [30, 40, 30],
    [40, 30, 40]
]

print("Inventory Reconciliation Report")

for i in range(len(warehouses)):
    print("\n", warehouses[i])

    for j in range(len(products)):
        difference = stock[i][j] - target[i][j]

        if difference < 0:
            print(products[j], "Shortage:", abs(difference))

        elif difference > 0:
            print(products[j], "Surplus:", difference)

        else:
            print(products[j], "Stock Balanced")

# Calculate transfers
print("\nRequired Stock Transfers:")

for j in range(len(products)):
    surplus = 0
    shortage = 0

    for i in range(len(warehouses)):
        difference = stock[i][j] - target[i][j]

        if difference > 0:
            surplus += difference
        elif difference < 0:
            shortage += abs(difference)

    transfer = min(surplus, shortage)

    print(products[j], "Transfer Required:", transfer)

print("\nInventory Analysis Completed")
