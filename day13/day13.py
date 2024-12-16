import sys
import re
import tqdm
from math import gcd
from functools import lru_cache
from multiprocessing import Pool, cpu_count

def parse_input(data):
    machines = []
    pattern = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)')
    data = ''.join(data)
    matches = pattern.findall(data)
    for match in matches:
        a_x, a_y, b_x, b_y, prize_x, prize_y = map(int, match)
        machines.append(((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))
    return machines

@lru_cache(None)
def cached_gcd(x, y):
    return gcd(x, y)

def can_win(prize_x, prize_y, a_x, a_y, b_x, b_y):
    if prize_x % cached_gcd(a_x, b_x) != 0:
        return False
    if prize_y % cached_gcd(a_y, b_y) != 0:
        return False
    return True

def min_tokens(prize_x, prize_y, a_x, a_y, b_x, b_y):
    dp = [[(float('inf'), 0, 0)] * (prize_y + 1) for _ in range(prize_x + 1)]
    dp[0][0] = (0, 0, 0)
    for x in range(prize_x + 1):
        for y in range(prize_y + 1):
            tokens, a_count, b_count = dp[x][y]
            if tokens == float('inf'):
                continue
            if x + a_x <= prize_x and y + a_y <= prize_y:
                dp[x + a_x][y + a_y] = min(dp[x + a_x][y + a_y], (tokens + 1, a_count + 1, b_count))
            if x + b_x <= prize_x and y + b_y <= prize_y:
                dp[x + b_x][y + b_y] = min(dp[x + b_x][y + b_y], (tokens + 1, a_count, b_count + 1))
    return dp[prize_x][prize_y]

def process_machine(machine):
    (a_x, a_y), (b_x, b_y), (prize_x, prize_y) = machine
    if can_win(prize_x, prize_y, a_x, a_y, b_x, b_y):
        tokens, a_count, b_count = min_tokens(prize_x, prize_y, a_x, a_y, b_x, b_y)
        if tokens != float('inf'):
            return tokens, a_count, b_count
    return None

def solve(data):
    machines = parse_input(data)
    total_tokens = 0
    prizes_won = 0
    presses = []

    with Pool(cpu_count()) as pool:
        results = list(tqdm.tqdm(pool.imap(process_machine, machines), total=len(machines)))

    for result in results:
        if result:
            tokens, a_count, b_count = result
            total_tokens += tokens
            prizes_won += 1
            presses.append((a_count, b_count))

    return total_tokens, prizes_won, presses

def main():
    data = sys.stdin.readlines()
    total_tokens, prizes_won, presses = solve(data)
    res = sum(a_count * 3 + b_count for a_count, b_count in presses)
    print(f"Total tokens spent: {res}")

if __name__ == '__main__':
    main()
