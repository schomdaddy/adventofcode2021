import sys

grid = []
for x in open("input.txt"):
    line = x.strip()
    entry = []
    for y in line:
        if y == "v":
            entry.append("D")
        elif y == ">":
            entry.append("R")
        else:
            entry.append(".")
    grid.append(entry)
step = grid
i = 1
print(step)
moved = False
while True:
    for x in range(len(grid)):
        for y in range(len(grid[x])):

            if grid[x][y] == "R":
                if y + 1 == len(grid[x]):
                    if grid[x][0] == ".":
                        step[x][y] = "."
                        step[x][0] = "R"
                        moved = True
                    else:
                        step[x][y] = "R"
                else:
                    if grid[x][y+1] == ".":
                        moved = True
                        step[x][y] = "."
                        step[x][y+1] = "R"
                    else:
                        step[x][y] = "R"
    grid = step
    step = grid
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "D":
                if x + 1 == len(grid):
                    if grid[0][y] == ".":
                        step[x][y] = "."
                        step[0][y] = "D"
                        moved = True
                    else:
                        step[x][y] = "D"
                else:
                    if grid[x+1][y] == ".":
                        moved = True
                        step[x][y] = "."
                        step[x+1][y] = "D"
                    else:
                        step[x][y] = "D"
    if not moved:
        print(i)
        sys.exit(0)
    i += 1
    moved = False
    grid = step
    step = grid
