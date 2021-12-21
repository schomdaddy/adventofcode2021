import heapq
from collections import defaultdict

def solve(size):
    rows, cols = sizey * size, sizex * size
    costs = defaultdict(int)
    queue = [(0,0,0)]
    heapq.heapify(queue)
    visited = set()
    while len(queue) > 0:
        cost, row, col = heapq.heappop(queue)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        costs[(row,col)] = cost
        if row == rows - 1 and col == cols - 1:
            break
        for mv_y, mv_x in [(0,1), (0,-1), (1,0), (-1,0)]:
            new_row = row + mv_y
            new_col = col + mv_x
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue
            new_cost = (
                (
                    grid[new_row % sizey][new_col % sizex]
                    + (new_row // sizey)
                    + (new_col // sizex)
                )
                -1
            ) % 9 + 1
            heapq.heappush(queue, (cost + new_cost, new_row, new_col))
    return costs[(rows - 1, cols - 1)]

grid = [[int(y) for y in x] for x in open("input.txt").read().strip().split("\n")]
sizey, sizex = len(grid), len(grid[0])
print(f"Part 1: {solve(1)}")
print(f"Part 2: {solve(5)}")