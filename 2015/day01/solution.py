from collections import Counter
from itertools import accumulate

def read_input(path: str) -> str:
    """Always assume that the input file size is manageable so that reading everything one shot
    into memory is feasible
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def part1_with_counter(input: str) -> int:
    counter_map = Counter(input)
    return counter_map['('] - counter_map[')']

def part1_with_generator(input: str) -> int:
    return sum(1 if c == '(' else -1 for c in input)

def part1_raw(input: str) -> int:
    sum = 0
    for c in input:
        if c == '(':
            sum += 1
        else:
            sum -= 1
    return sum

def part2_with_loop(input:str) -> int:
    sum = 0
    idx = 0
    while sum != -1:
        sum += 1 if input[idx] == '(' else -1
        idx+=1
    
    return idx

def part2_with_fancy_itertools(input:str) -> int:
    floors = accumulate(1 if c == '(' else -1 for c in input)
    TARGET = -1
    index = next(
        i for i, s in enumerate(floors) if s == TARGET
    )
    return index + 1


if __name__ == "__main__":
    problem_input = read_input("input.txt")
    print(part1_with_counter(problem_input))
    print(part1_with_generator(problem_input))
    print(part1_raw(problem_input))
    print(part2_with_loop(problem_input))
    print(part2_with_fancy_itertools(problem_input))