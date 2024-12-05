
#!/usr/bin/env python3

import os


def parseInput(filename: str) -> list[list[int]]:
    lists = [[], []]
    dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir, filename), 'r') as f:
        for line in f:
            columns = line.strip().split('   ')
            lists[0].append(int(columns[0]))
            lists[1].append(int(columns[1]))
    return lists


def partOne(a: list[int], b: list[int]) -> int:
    a.sort()
    b.sort()
    dist = 0
    for i in range(len(a)):
        dist += abs(a[i] - b[i])
    return dist


def partTwo(a: list[int], b: list[int]) -> int:
    score = 0
    for i in range(len(a)):
        val = a[i]
        freq = b.count(val)
        score += val * freq
    return score


if __name__ == '__main__':
    input = parseInput('input.txt')
    solution1 = partOne(input[0], input[1])
    print(f'The solution to part one: {str(solution1)}')
    solution2 = partTwo(input[0], input[1])
    print(f'The solution to part two: {str(solution2)}')
