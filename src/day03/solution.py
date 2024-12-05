#!/usr/bin/env python3

import os
import re


def parseInput(filename: str) -> str:
    text = ''
    dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir, filename), 'r') as f:
        text = f.read().strip()
    return text


def partOne(memory: str) -> int:
    sum = 0
    for func, a, b in re.findall(r"(mul)\((\d{1,3}),(\d{1,3})\)", memory):
        if (func == 'mul'):
            sum += int(a) * int(b)
    return sum


def partTwo(memory: str) -> int:
    sum = 0
    enabled = True
    for func, a, b in re.findall(r"(do|don't|mul)\((?:(\d{1,3}),(\d{1,3}))?\)", memory):
        # Evalutate any do/don't commands that would flip the enabled flag
        if (func == 'don\'t' and enabled) or (func == 'do' and not enabled):
            enabled = not enabled
        # Evalulate the mul command
        if func == 'mul' and enabled:
            sum += int(a) * int(b)
    return sum


if __name__ == '__main__':
    input = parseInput('input.txt')
    solution1 = partOne(input)
    print(f'The solution to part one: {str(solution1)}')
    solution2 = partTwo(input)
    print(f'The solution to part two: {str(solution2)}')
