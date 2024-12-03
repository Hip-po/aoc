import sys
import re

def solve(data):
    pattern = r'(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\))'
    matches = re.findall(pattern, data)

    total = 0
    enabled = True

    for match in matches:
        if match[1] and match[2]:
            if enabled:
                total += int(match[1]) * int(match[2])
        elif match[3]:
            enabled = True
        elif match[4]:
            enabled = False

    return total

def main():
    data = sys.stdin.read()
    print(f"res: {solve(data)}")

if __name__ == "__main__":
    main()
