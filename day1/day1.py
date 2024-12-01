#!/usr/bin/env python3

from collections import Counter
import sys

def read_input():
    left = []
    right = []
    for line in sys.stdin:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    return left, right

def calculate_total_distance(left, right):
    left.sort()
    right.sort()
    total_distance = sum(abs(l - r) for l, r in zip(left, right))
    return total_distance

def calculate_similarity_score(left, right):
    right_counter = Counter(right)
    similarity_score = sum(l * right_counter[l] for l in left)
    return similarity_score

def main():
    left, right = read_input()
    total_distance = calculate_total_distance(left, right)
    print(f"Total distance: {total_distance}")

    similarity_score = calculate_similarity_score(left, right)
    print(f"Similarity score: {similarity_score}")

if __name__ == "__main__":
    main()
