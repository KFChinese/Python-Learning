number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])  # calls the 1 from first 2D List


print("")

for row in number_grid:
    print(row)
# Prints out rows in 2D grid
print("")

for row in number_grid:
    for col in row:
        print(col)
# Prints out the coloum for 2D grid
