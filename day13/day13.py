points = set()
folds = []

read = False
for x in open("input.txt"):
    x = x.strip()
    if x == "":
        read = True
    if not read:
        x,y = x.split(",")
        points.add((int(x), int(y)))
    elif read and not x == "":
        i,j, cord = x.split(" ")
        axis, dim = cord.split("=")
        folds.append((axis, int(dim)))
print(len(points))


for fold in folds:
    newpoints = set()
    if fold[0] == "x":
        for point in points:
            if point[0] > fold[1]:
                newpoints.add((point[0] - (2 * (point[0] - fold[1])), point[1]))
            elif point[0] < fold[1]:
                newpoints.add(point)
        points = newpoints
    if fold[0] == "y":
        for point in points:
            if point[1] > fold[1]:
                newpoints.add((point[0], point[1] - (2 * (point[1] - fold[1]))))
            elif point[1] < fold[1]:
                newpoints.add(point)
        points = newpoints
    print(len(points))
ans = ""
for y in range(7):
    for x in range (50):
        if (x,y) in points:
            ans += "#"
        else:
            ans += "."
    ans += "\n"
print(ans)