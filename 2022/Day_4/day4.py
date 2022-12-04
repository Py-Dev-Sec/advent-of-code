import time


def process_data(input_file: str) -> None:
    """
    Wrapper. Loads input data from the file and executes methods for solutions part 1 & 2
    """
    with open(input_file, "r") as file:
        assignments = [line.strip() for line in file.readlines()]
    converted = convert_assignment(assignments)
    process_data_part_one(converted)
    process_data_part_two(converted)


def process_data_part_one(converted_assignments: list) -> None:
    """
    Solves part 1 puzzle
    """
    total_pairs = 0
    for pair in converted_assignments:
        if check_subset(pair[0], pair[1]):
            total_pairs += 1
    answer_p1 = total_pairs
    print("PART 1 answer: {}".format(answer_p1))


def process_data_part_two(converted_assignments: list) -> None:
    """
    Solves part 2 puzzle
    """
    total_overlaps = 0
    for pair in converted_assignments:
        if check_intersection(pair[0], pair[1]):
            total_overlaps += 1
    answer_p2 = total_overlaps
    print("PART 2 answer: {}".format(answer_p2))


def convert_assignment(assignments: list) -> list:
    """
    Converts raw assignment to list of pairs. Each pair is related with elves pair and contains 2 sets with
    assignments ID for their work in sections.
    """
    section_mapped = map(convert_sections_to_set, assignments)
    return list(section_mapped)


def convert_sections_to_set(section: str) -> list:
    """
    Converts sections ID string to set of ID numbers.
    """
    pair = section.split(",")
    set_list = list()
    for member in pair:
        pos = convert_range_section_str(member)
        member_set = set([i for i in range(pos[0], pos[1]+1)])
        set_list.append(member_set)
    return set_list


def convert_range_section_str(single_range: str) -> list:
    """
    Converts section's range ID string to list of start/end range ID.
    """
    return [int(pos) for pos in single_range.split("-")]


def check_subset(set_a: set, set_b: set) -> bool:
    """
    Checks if set A or set B are subset for each other.
    """
    is_subset = False
    if set_a.issubset(set_b) or set_b.issubset(set_a):
        is_subset = True
    return is_subset


def check_intersection(set_a: set, set_b: set) -> bool:
    """
    Checks if a pair of the sets A and B contains intersection.
    """
    is_intersection = False
    if set_a.intersection(set_b):
        is_intersection = True
    return is_intersection


if __name__ == "__main__":
    print("Advent of Code 2022 - Day 4")
    fp = "input"
    start_time = time.time()
    process_data(fp)
    end_time = time.time()
    exc_time = (end_time - start_time) * 1000
    print("Total Execution time: {} ms".format(exc_time))
