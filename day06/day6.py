import sys
from time import sleep

def simulate_gard(grid, pos):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction_map = {'^': 3, 'v': 1, '<': 0, '>': 2}

    x, y = pos
    direction = direction_map[grid[x][y]]
    grid[x][y] = 'X'
    visited = set()
    visited.add((x, y, direction))

    while True:
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
            return False

        if grid[nx][ny] != '#':
            x, y = nx, ny
            if grid[x][y] == '.':
                grid[x][y] = 'X'
            if (x, y, direction) in visited:
                return True
            visited.add((x, y, direction))
        else:
            direction = (direction + 1) % 4

def solve(data):
    pos = [0, 0]
    grid = []
    line = 0
    for i in data:
        if i == "\n":
            line += 1
            continue
        if line >= len(grid):
            grid.append([])
        grid[line].append(i)
        if i in ["^", "v", "<", ">"]:
            pos = [line, len(grid[line]) - 1]

    loop_positions = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.' and (i, j) != (pos[0], pos[1]):
                grid_copy = [row[:] for row in grid]
                grid_copy[i][j] = '#'
                if simulate_gard(grid_copy, pos):
                    loop_positions += 1

    return loop_positions

def main():
    data = sys.stdin.read().strip()
    res = solve(data)
    print(f"res: {res}")

if __name__ == "__main__":
    main()
