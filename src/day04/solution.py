#!/usr/bin/env python3

import os
import re


def parseInput(filename: str) -> str:
    rows = []
    dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir, filename), 'r') as f:
        for line in f:
            cols = list(line.strip())
            rows.append(cols)
    return rows


def checkOrdinalPatterns(grid: list[list[str]], row: int, col: int, target: str = "XMAS"):

    checks = [
        [[0, 0], [-1, +0], [-2, +0], [-3, +0]],
        [[0, 0], [+1, +0], [+2, +0], [+3, +0]],
        [[0, 0], [+0, -1], [+0, -2], [+0, -3]],
        [[0, 0], [+0, +1], [+0, +2], [+0, +3]],
        [[0, 0], [-1, -1], [-2, -2], [-3, -3]],
        [[0, 0], [-1, +1], [-2, +2], [-3, +3]],
        [[0, 0], [+1, -1], [+2, -2], [+3, -3]],
        [[0, 0], [+1, +1], [+2, +2], [+3, +3]]
    ]

    solutions = 0
    for check in checks:
        checkResult = ''
        for drow, dcol in check:
            r, c = row + drow, col + dcol
            if (r >= 0 and r < len(grid)) and (c >= 0 and c < len(grid[0])):
                checkResult += grid[r][c]
        if checkResult == target:
            solutions += 1
    return solutions


def checkCrossPattern(grid: list[list[str]], row: int, col: int, target: str = 'MAS'):

    checks = [
        [[[-1, -1], [+0, +0], [+1, +1]], [[-1, +1], [+0, +0], [+1, -1]]],
        [[[+1, -1], [+0, +0], [-1, +1]], [[+1, +1], [+0, +0], [-1, -1]]],
        [[[-1, -1], [+0, +0], [+1, +1]], [[+1, -1], [+0, +0], [-1, +1]]],
        [[[-1, +1], [+0, +0], [+1, -1]], [[+1, +1], [+0, +0], [-1, -1]]],
    ]

    solutions = 0
    for check in checks:
        checkResult = 0
        for item in check:
            itemResult = ''
            for drow, dcol in item:
                r, c = row + drow, col + dcol
                if (r >= 0 and r < len(grid)) and (c >= 0 and c < len(grid[0])):
                    itemResult += grid[r][c]
            if itemResult == target:
                checkResult += 1
        if checkResult == len(check):
            solutions += 1

    return solutions


def partOne(grid: list[list[str]]) -> int:
    solutions = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            solutions += checkOrdinalPatterns(grid, row, col, 'XMAS')
    return solutions


def partTwo(grid: list[list[str]]) -> int:
    solutions = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            solutions += checkCrossPattern(grid, row, col, 'MAS')
    return solutions


if __name__ == '__main__':
    input = parseInput('input.txt')
    solution1 = partOne(input)
    print(f'The solution to part one: {str(solution1)}')
    solution2 = partTwo(input)
    print(f'The solution to part two: {str(solution2)}')
