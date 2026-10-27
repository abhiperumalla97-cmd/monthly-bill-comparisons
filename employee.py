

# Employee Shift Conflict Detection

shifts = [
    ("Pavan", 9, 13),
    ("Ravi", 12, 16),
    ("Arjun", 14, 18),
    ("Pavan", 15, 19),
    ("Kiran", 8, 12)
]

conflicts = []

print("Employee Shift Details:")

for shift in shifts:
    print(shift)

# Check overlapping shifts of same employee
print("\nShift Conflicts:")

for i in range(len(shifts)):
    for j in range(i + 1, len(shifts)):

        if shifts[i][0] == shifts[j][0]:

            if shifts[i][1] < shifts[j][2] and shifts[j][1] < shifts[i][2]:

                print("Employee:", shifts[i][0])
                print("Shift 1:", shifts[i][1], "-", shifts[i][2])
                print("Shift 2:", shifts[j][1], "-", shifts[j][2])

                conflicts.append(shifts[i][0])

# Display conflicting employees
print("\nEmployees with Conflicting Schedules:")

if conflicts:
    for name in set(conflicts):
        print(name)
else:
    print("No Conflicts Found")
