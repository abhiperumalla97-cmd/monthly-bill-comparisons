
# Traffic Flow and Congestion Analysis

roads = int(input("Enter number of roads: "))

capacity = 100
max_traffic = 0
peak_road = ""

for i in range(roads):
    road = input("\nEnter road name: ")
    total = 0

    for j in range(3):
        count = int(input("Enter vehicle count: "))
        total += count

    average = total / 3

    print("\nRoad:", road)
    print("Average Traffic:", average)

    if average < 40:
        print("Congestion: Low")
    elif average < 80:
        print("Congestion: Medium")
    else:
        print("Congestion: High")

    if average > capacity:
        print("Warning: Road exceeds capacity!")

    if total > max_traffic:
        max_traffic = total
        peak_road = road

print("\n----- Traffic Report -----")
print("Peak Traffic Road:", peak_road)
print("Maximum Vehicle Count:", max_traffic)
