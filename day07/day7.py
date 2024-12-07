import sys
import itertools

def eval_eq(numbers, operators):
    result = numbers[0]
    for op, num in zip(operators, numbers[1:]):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '|':
            result = int(str(result) + str(num))
    return result

def solve(data):
    total_calibration_result = 0
    for line in data:
        res_eq, eq = line.split(':')
        res_eq = int(res_eq)
        numbers = list(map(int, eq.split()))

        operator_combinations = itertools.product('+*|', repeat=len(numbers) - 1)

        for operators in operator_combinations:
            if eval_eq(numbers, operators) == res_eq:
                total_calibration_result += res_eq
                break

    return total_calibration_result

def main():
    data = sys.stdin.readlines()
    print(solve(data))

if __name__ == '__main__':
    main()
