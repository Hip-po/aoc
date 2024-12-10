import sys

def parse(data):
    return [list(map(int, line.strip())) for line in data]

def is_valid(x, y, map_data):
    return 0 <= x < len(map_data) and 0 <= y < len(map_data[0])

def dfs(x, y, map_data, visited):
    if map_data[x][y] == 9:
        return 1
    visited.add((x, y))
    count = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, map_data) and (nx, ny) not in visited and map_data[nx][ny] == map_data[x][y] + 1:
            count += dfs(nx, ny, map_data, visited)
    visited.remove((x, y))
    return count

def solve(data):
    map_data = parse(data)
    trailheads = [(x, y) for x in range(len(map_data)) for y in range(len(map_data[0])) if map_data[x][y] == 0]
    total_score = 0
    for x, y in trailheads:
        score = dfs(x, y, map_data, set())
        total_score += score
    return total_score

def main():
    data = sys.stdin.readlines()
    print(solve(data))

if __name__ == '__main__':
    main()
