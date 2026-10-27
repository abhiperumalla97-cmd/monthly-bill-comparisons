
# Sports Tournament Ranking System

teams = ["Team A", "Team B", "Team C", "Team D"]

# Match results: [Wins, Draws, Goals Scored, Goals Against]
results = [
    [3, 1, 10, 4],
    [3, 1, 12, 5],
    [2, 2, 8, 6],
    [1, 1, 5, 10]
]

points = []

# Calculate total points
for i in range(len(teams)):
    wins = results[i][0]
    draws = results[i][1]

    total = wins * 3 + draws * 1
    goal_difference = results[i][2] - results[i][3]

    points.append([teams[i], total, goal_difference])

# Ranking based on points and goal difference
points.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("----- Tournament Rankings -----")

for i in range(len(points)):
    print("Rank:", i + 1)
    print("Team:", points[i][0])
    print("Points:", points[i][1])
    print("Goal Difference:", points[i][2])
    print()
