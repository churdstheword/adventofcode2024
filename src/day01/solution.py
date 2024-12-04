
#!/usr/bin/env python3

import os


def parseInput() -> list[list[int]]:
    lists = [[],[]]
    dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir, 'input.txt'), 'r') as f:
        for line in f:
            columns = line.strip().split('   ')
            lists[0].append(int(columns[0]))
            lists[1].append(int(columns[1]))
    return lists


def partOne() -> int:

    
    lists = parseInput()
    lists[0].sort()
    lists[1].sort()
    
    distance = 0
    for i in range(len(lists[0])):
        distance += abs(lists[0][i] - lists[1][i])
        
    return distance

def partTwo() -> int:

    lists = parseInput()

    score = 0
    for i in range(len(lists[0])):
        value = lists[0][i];
        freq = lists[1].count(value)
        score += value * freq

    return score


if __name__ == '__main__':
    solution1 = partOne()
    print(f'The solution to part one: {str(solution1)}')
    solution2 = partTwo()
    print(f'The solution to part two: {str(solution2)}')