f = open("input.txt")
rule = f.readline().strip()
f.readline()
grid = []
line = ""
for x in f:
    line = x.strip()
    grid.append(line)
    line = ""
points = set()
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == '#':
            points.add((x,y))
xmax = 0
xmin = 0
ymax = 0
ymin = 0
turn = True
for i in range(50):
    for (x,y) in points:
        xmin = min(xmin, x - 1)
        xmax = max(xmax, x + 1)
        ymin = min(ymin, y - 1)
        ymax = max(ymax, y + 1)
    if turn:
        p2 = set()
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                exp = 8
                total = 0
                for i in [-1,0,1]:
                    for j in [-1, 0 , 1]:
                        if (x + i, y + j) in points:
                            total += 2 ** exp
                        exp -= 1
                if rule[total] == '.':
                    p2.add((x,y))
        points = p2
        turn = False
    else:
        for (x, y) in points:
            xmin = min(xmin, x - 1)
            xmax = max(xmax, x + 1)
            ymin = min(ymin, y - 1)
            ymax = max(ymax, y + 1)
        if set:
            p2 = set()
            for x in range(xmin, xmax + 1):
                for y in range(ymin, ymax + 1):
                    exp = 8
                    total = 0
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if (x + i, y + j) not in points:
                                total += 2 ** exp
                            exp -= 1
                    if rule[total] == '#':
                        p2.add((x, y))
            points = p2
        turn = True
print(len(points))