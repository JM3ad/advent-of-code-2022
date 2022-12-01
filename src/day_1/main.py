import os

def load_txt():
    lines = []
    with open("src/day_1/day_1.txt") as f:
        lines = f.readlines()
    return lines

def part_1(lines):
    current = 0
    max = 0
    for line in lines:
        # print(f"{line} is digit {line.isdigit()}")

        if line.strip().isdigit():
            current += int(line)
        else:
            if current > max:
                max = current
            current = 0
    print(f"Day 1 part 1, max is {max}")

def part_2(lines):
    current = 0
    results = []
    for line in lines:
        # print(f"{line} is digit {line.isdigit()}")

        if line.strip().isdigit():
            current += int(line)
        else:
            results.append(current)
            current = 0
    results.sort()
    # print(results)
    sum = results[-3] + results[-2] + results[-1]
    print(f"Day 1 part 2, sum is {sum}")

def run():
    lines = load_txt()
    part_1(lines)
    part_2(lines)
