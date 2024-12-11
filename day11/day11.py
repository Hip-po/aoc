import sys

def solve(data):
    stones = list(map(int, ''.join(data).strip().split()))
    blinks = 75

    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                half_len = len(str(stone)) // 2
                left_half = int(str(stone)[:half_len])
                right_half = int(str(stone)[half_len:])
                new_stones.extend([left_half, right_half])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    return len(stones)

def main():
    data = sys.stdin.readlines()
    print(solve(data))

if __name__ == '__main__':
    main()
