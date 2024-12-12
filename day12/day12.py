import sys

def parse(data):
    return [list(line.strip()) for line in data]

def get_neighbors(x, y, max_x, max_y):
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < max_x - 1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < max_y - 1:
        neighbors.append((x, y+1))
    return neighbors

def flood_fill(map_data, x, y, visited):
    plant_type = map_data[x][y]
    stack = [(x, y)]
    region = []
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        region.append((cx, cy))
        for nx, ny in get_neighbors(cx, cy, len(map_data), len(map_data[0])):
            if map_data[nx][ny] == plant_type and (nx, ny) not in visited:
                stack.append((nx, ny))
    return region

def calculate_area_and_perimeter(region, map_data):
    area = len(region)
    perimeter = 0
    max_x = len(map_data)
    max_y = len(map_data[0])
    for x, y in region:
        for nx, ny in get_neighbors(x, y, max_x, max_y):
            if map_data[nx][ny] != map_data[x][y]:
                perimeter += 1
        # Check if the plot is at the edge of the map
        if x == 0 or x == max_x - 1:
            perimeter += 1
        if y == 0 or y == max_y - 1:
            perimeter += 1
    return area, perimeter

def solve(data):
    map_data = parse(data)
    visited = set()
    total_price = 0
    for x in range(len(map_data)):
        for y in range(len(map_data[0])):
            if (x, y) not in visited:
                region = flood_fill(map_data, x, y, visited)
                area, perimeter = calculate_area_and_perimeter(region, map_data)
                print(f"region: {map_data[region[0][0]][region[0][1]]}, area: {area}, perimeter: {perimeter}")
                total_price += area * perimeter
    return total_price

def main():
    data = sys.stdin.readlines()
    print(solve(data))

if __name__ == '__main__':
    main()
