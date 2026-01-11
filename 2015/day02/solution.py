from typing import List

def read_inputs_as_list(filename: str) -> List[str]:
    with open(filename, "r", encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def convert_line_str_into_dim_list(line: str) -> List[int]:
    dimensions = line.strip().split(sep="x")
    dimensions = [int(dim) for dim in dimensions]
    return dimensions

def part1_simple(dimensions_list: List[int]) -> int:
    # TODO: Try to refactor with some short form for combinations (suggeted to use itertools)
    boxes_surface_areas = [] # per each box
    boxes_total_areas = 0
    surface_D = 2
    for dimensions in dimensions_list:
        print(f"Dimensions of this box: {dimensions}")
        this_box_areas = []
        start_idx = 0
        while start_idx <= len(dimensions) - surface_D:
            for end_index in range(start_idx+1, len(dimensions)):
                this_box_areas.append(dimensions[start_idx] * dimensions[end_index])
                boxes_total_areas += 2 * dimensions[start_idx] * dimensions[end_index]
            start_idx += 1
        print(f"This box surfaces areas: {this_box_areas}")
        boxes_surface_areas.append(this_box_areas)
    lowest_surface_areas = [min(surface_areas_of_this_box) for surface_areas_of_this_box in boxes_surface_areas]
    return sum(lowest_surface_areas) + boxes_total_areas

def part2_simple(dimensions_list: List[int]) -> int:
    # TODO: is there an equivalent to sum but in product ? suggested to use reduce?
    total_volumes = sum(box_dimensions[0] * box_dimensions[1] * box_dimensions[2] for box_dimensions in dimensions_list)
    max_side_measurement = [max(box_dimensions) for box_dimensions in dimensions_list]
    return total_volumes + 2 * sum(sum(box_dimensions) for box_dimensions in dimensions_list) - 2 * sum(max_side_measurement)


if __name__=="__main__":
    list_of_input_lines = read_inputs_as_list("input.txt")
    list_of_dimensions = [convert_line_str_into_dim_list(line) for line in list_of_input_lines]
    print(list_of_dimensions)
    print(part1_simple(list_of_dimensions))
    print(part2_simple(list_of_dimensions))