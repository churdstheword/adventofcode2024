
#!/usr/bin/env python3

import os


def parseInput(filename: str) -> list[list[int]]:
    lines = []
    dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir, filename), 'r') as f:
        for line in f:
            values = [int(item) for item in line.strip().split(' ')]
            lines.append(values)
    return lines


def getRates(levels: list[int]) -> list[int]:
    rates = []
    for i in range(len(levels) - 1):
        rate = levels[i + 1] - levels[i]
        rates.append(rate)
    return rates


def checkRates(rates: list[int]) -> bool:

    inBounds = 0
    ascending = 0
    decending = 0
    length = len(rates)
    for i in range(length):
        rate = abs(rates[i])
        if rate > 0 and rate <= 3:
            inBounds += 1
        if rates[i] > 0:
            ascending += 1
        if rates[i] < 0:
            decending += 1

    allRatesInBounds = (inBounds == length)
    allRatesAscending = (ascending == length)
    allRatesDecending = (decending == length)

    return (allRatesInBounds and (allRatesAscending or allRatesDecending))


def partOne(reports: list[list[int]]) -> int:
    numSafe = 0
    for report in reports:
        rates = getRates(report)
        if checkRates(rates):
            numSafe += 1
    return numSafe


def partTwo(reports: list[list[int]]) -> int:
    numSafe = 0
    for report in reports:
        # Evaluate a copy of each report having each copy missing a different item
        # If at least one copy is safe, then the original report is safe
        for i in range(len(report)):
            copy = report.copy()
            copy.pop(i)
            rates = getRates(copy)
            if checkRates(rates):
                numSafe += 1
                break
    return numSafe


if __name__ == '__main__':
    input = parseInput('input.txt')
    solution1 = partOne(input)
    print(f'The solution to part one: {str(solution1)}')
    solution2 = partTwo(input)
    print(f'The solution to part two: {str(solution2)}')
