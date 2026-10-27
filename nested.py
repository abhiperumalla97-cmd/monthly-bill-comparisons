

# Nested List Classroom Occupancy Analysis

classrooms = [
    ["Pavan", "Reserved", None],
    ["Ravi", None, "Kiran"],
    [None, "Reserved", None]
]

students = ["Arjun", "Rahul", "Pavan"]

print("Classroom Seating:")

for i in range(len(classrooms)):
    for j in range(len(classrooms[i])):
        if classrooms[i][j] is None:
            if students:
                student = students.pop(0)

                # Check duplicate assignment
                if student not in sum(classrooms, []):
                    classrooms[i][j] = student
                else:
                    print("Duplicate student:", student)

print("\nFinal Classroom Occupancy:")

vacant = 0
reserved = 0
occupied = 0

for room in classrooms:
    print(room)

    for seat in room:
        if seat is None:
            vacant += 1
        elif seat == "Reserved":
            reserved += 1
        else:
            occupied += 1

print("\nOccupied Seats:", occupied)
print("Reserved Seats:", reserved)
print("Vacant Seats:", vacant)
print("Total Capacity:", occupied + reserved + vacant)
