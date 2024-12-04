import sys
from collections import Counter

def solve(data):
    grid = data.split("\n")
    rows = len(grid)
    cols = len(grid[0])

    def check_x_mas(x, y):
        if (0 <= x - 1 < rows and 0 <= x + 1 < rows and
            0 <= y - 1 < cols and 0 <= y + 1 < cols):
            char_present = Counter([grid[x-1][y+1], grid[x+1][y-1], grid[x-1][y-1], grid[x+1][y+1]])
            if char_present["M"] == 2 and char_present["S"] == 2:
                if grid[x-1][y+1] == "M" and grid[x+1][y-1] == "S":
                    return True
                elif grid[x-1][y+1] == "S" and grid[x+1][y-1] == "M":
                    return True
                else:
                    return False
        return False

    total = 0
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 'A' and check_x_mas(x, y):
                total += 1

    return total

def main():
    data = sys.stdin.read().strip()
    print(f"res: {solve(data)}")

if __name__ == "__main__":
    main()
