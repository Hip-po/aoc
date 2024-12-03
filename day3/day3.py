import sys
import re

def solve(data):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, data)

    total = 0
    for match in matches:
        x, y = map(int, match)
        total += x * y

    return total


def main():
    data = sys.stdin.read()
    print(f"res: {solve(data)}")


if __name__ == "__main__":
    main()
