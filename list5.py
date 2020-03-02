number_grid = [
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]

# 2D list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid)
print(len(number_grid))
print(number_grid[1][2])

for row in number_grid:
    print(row)
    for j in row:
        print(j)