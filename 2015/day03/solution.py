from typing import Tuple, List

ARROW_TO_TUPLE = {
    '^': (0,1),
    'v': (0,-1),
    '>': (1,0),
    '<': (-1,0) 
}

def read_input(filepath: str) -> str:
    with open(filepath, "r", encoding='utf-8') as f:
        content = f.read()

    return content

def convert_input_str_into_post_deltas(input:str) -> List[Tuple[int, int]]:
    input = input.strip()
    return [convert_arrow_char_to_tuple(arrow_char) for arrow_char in input]
    

def convert_arrow_char_to_tuple(c: str) -> Tuple[int, int]:
    return ARROW_TO_TUPLE[c]

def part1_naive(input: str) -> int:
    curr_pos = [0,0]
    unique_positions = set()
    unique_positions.add(tuple(curr_pos))

    deltas = convert_input_str_into_post_deltas(input)
    for delta in deltas:
        curr_pos[0] += delta[0]
        curr_pos[1] += delta[1]
        unique_positions.add(tuple(curr_pos))

    return len(unique_positions)


def part2_naive(input:str) -> int:
    # Santa and Robot starts at same state
    santa_pos, robot_pos = [0,0], [0,0]
    unique_positions = set()
    unique_positions.add(tuple(santa_pos))

    deltas = convert_input_str_into_post_deltas(input)

    for idx, delta in enumerate(deltas):
        if idx % 2 == 0:
            # Santa go from 0, on even steps
            santa_pos[0] += delta[0]
            santa_pos[1] += delta[1]
            unique_positions.add(tuple(santa_pos))
        else:
            # Robot go from 1, on odd steps
            robot_pos[0] += delta[0]
            robot_pos[1] += delta[1]
            unique_positions.add(tuple(robot_pos))     

    return len(unique_positions)

if __name__ == "__main__":
    input_str = read_input("input.txt")
    print(part1_naive(input_str))
    print(part2_naive(input_str))