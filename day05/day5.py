import sys
from collections import deque

def parse_input(data):
    rules_section, updates_section = data.split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_section.split()]
    updates = [list(map(int, update.split(','))) for update in updates_section.split()]
    return rules, updates

def is_correct_order(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def correct_order(update, rules):
    update = deque(update)
    changed = True
    while changed:
        changed = False
        for i in range(len(update) - 1):
            for x, y in rules:
                if x in update and y in update:
                    if update.index(x) > update.index(y):
                        update.remove(x)
                        update.insert(update.index(y), x)
                        changed = True
    return list(update)

def solve(data):
    rules, updates = parse_input(data)
    pages_correct = 0
    pages_incorrect = 0

    for update in updates:
        if is_correct_order(update, rules):
            middle_index = len(update) // 2
            pages_correct += update[middle_index]
        else:
            update = correct_order(update, rules)
            middle_index = len(update) // 2
            pages_incorrect += update[middle_index]

    return pages_correct, pages_incorrect

def main():
    data = sys.stdin.read().strip()
    correct_sum, incorrect_sum = solve(data)
    print(f"res1: {correct_sum}")
    print(f"res2: {incorrect_sum}")

if __name__ == "__main__":
    main()
