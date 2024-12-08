import sys

def get_all_chars(data):
    all_chars = {}
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char not in [".", "\n"]:
                if char not in all_chars:
                    all_chars[char] = []
                all_chars[char].append((x, y))
    return all_chars

def all_lines(row, col, pos, dx, dy):
    antinode = set()
    while 0 <= pos[0] < row and 0 <= pos[1] < col:
        antinode.add(pos)
        pos = (pos[0] + dx, pos[1] + dy)
    return antinode

def distance_nodes(data, char):
    antinode = set()
    row = len(data)
    col = len(data[0]) - 1

    for i in range(len(char)-1):
        for j in range(i+1, len(char)):
            pos1, pos2 = char[i], char[j]
            if pos1[0] > pos2[0]:
                pos1, pos2 = pos2, pos1
            dx, dy = pos2[0] - pos1[0], pos2[1] - pos1[1]
            antinode.update(all_lines(row, col, pos1, -dx, -dy))
            antinode.update(all_lines(row, col, pos2, dx, dy))

    return antinode

def solve(data):
    antinode = set()
    all_chars = get_all_chars(data)
    grid = [[x for x in line] for line in data]

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == ".":
                for char in all_chars.keys():
                    antinode.update(distance_nodes(data, all_chars[char]))

    return len(antinode)

def main():
    data = sys.stdin.readlines()
    print(solve(data))

if __name__ == '__main__':
    main()
