grid = []
line = []
for x in open("input.txt"):
    for y in x.strip():
        line.append(int(y))
    grid.append(line)
    line = []

grid_height = len(grid)
grid_width = len(grid[0])

low_points = []

def get_neighbors(x,y):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < grid_width - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < grid_height - 1:
        neighbors.append((x, y + 1))
    return neighbors


def check_low_point(x, y):
    i = grid[y][x]
    neighbors = get_neighbors(x, y)
    for p in neighbors:
        x, y = p
        if i >= grid[y][x]:
            return False
    return True

ans = 0
for y, row in enumerate(grid):
    for x, height in enumerate(row):
        if check_low_point(x, y):
            low_points.append((x, y))
            ans += height + 1
print(ans)

def get_basin(x, y):
    basin_points = []
    neighbors = get_neighbors(x, y)
    for point in neighbors:
        n_x, n_y = point
        if grid[n_y][n_x] < 9:
            basin_points.append(point)
    return basin_points


def get_basin_whole(point, basin_points=[]):
    basin_points = basin_points.copy()
    basin_points.append(point)
    x, y = point
    adj_basin_points = get_basin(x, y)
    for adj_p in adj_basin_points:
        if adj_p not in basin_points:
            basin_points = get_basin_whole(adj_p, basin_points)
    return basin_points

basin_sizes = []
for p in low_points:
    basin_points = get_basin_whole(p)
    size = len(basin_points)
    basin_sizes.append(size)

basin_sizes.sort(reverse=True)
sub = basin_sizes[:3]
ans2 = 1
for i in sub:
    ans2 *= i
print(ans2)