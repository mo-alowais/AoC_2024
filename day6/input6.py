grid = list(map(list,open('input6.txt').read().splitlines()))

startRow, startCol = 0, 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "^":
            startRow, startCol = r, c
            break
