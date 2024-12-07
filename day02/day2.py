#!/usr/bin/env python3

import sys

def is_safe(report):
    levels = list(map(int, report.split()))
    if is_inc(levels) or is_dec(levels):
        return True
    for i in range(len(levels)):
        modified = levels[:i] + levels[i+1:]
        if is_inc(modified) or is_dec(modified):
            return True
    return False

def is_inc(lvl):
    return all(lvl[i] < lvl[i + 1] and 1 <= lvl[i + 1] - lvl[i] <= 3 for i in range(len(lvl) - 1))

def is_dec(lvl):
    return all(lvl[i] > lvl[i + 1] and 1 <= lvl[i] - lvl[i + 1] <= 3 for i in range(len(lvl) - 1))

def main():
    data = sys.stdin.read()
    reports = data.strip().split('\n')
    print(f"res: {sum(1 for report in reports if is_safe(report))}")

if __name__ == "__main__":
    main()
