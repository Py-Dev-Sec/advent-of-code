import time
from string import ascii_lowercase, ascii_uppercase
from collections import Counter
from functools import partial


def set_priority() -> dict:
    """
        Manages item type priority. Creates dict with item priority structure
        Item type priority:
            a-z -> 1-26
            A-Z -> 27-52
    """
    priority = dict()
    lowercase = list(ascii_lowercase)
    low_priority = [i+1 for i in range(26)]
    uppercase = list(ascii_uppercase)
    upp_priority = [i+1 for i in range(26, 52)]
    priority.update(dict(zip(lowercase, low_priority)))
    priority.update(dict(zip(uppercase, upp_priority)))
    return priority


def process_data(input_file: str) -> None:
    """
    Wrapper. Sets up item priority by type and loads input rucksacks from the file.
    """
    item_type_priority = set_priority()
    with open(input_file, "r") as file:
        rucksacks = [line.strip() for line in file.readlines()]
    answer_p1 = process_data_part_one(rucksacks, item_type_priority)
    answer_p2 = process_data_part_two(rucksacks, item_type_priority)
    print("PART 1 answer: {}".format(answer_p1))
    print("PART 2 answer: {}".format(answer_p2))


def process_data_part_one(input_file: list, item_type_priority: dict) -> int:
    """
    Solves part 1 puzzle
    """
    same_type_items = list()
    for item in input_file:
        pos = len(item) // 2
        c_first = Counter(item[:pos])
        c_second = Counter(item[pos:])
        intersection = c_first & c_second
        same_type_items.extend(list(intersection))
    total_priority_items = sum_priority_items(item_type_priority, same_type_items)
    return total_priority_items


def process_data_part_two(input_file: list, item_type_priority: dict) -> int:
    """
    Solves part 2 puzzle
    """
    offset = 3
    groups = [" ".join(input_file[i:i + offset]) for i in range(0, len(input_file), offset)]
    same_items = list()
    for group in groups:
        chunks = group.split(" ")
        first = Counter(chunks[0])
        second = Counter(chunks[1])
        third = Counter(chunks[2])
        intersection = first & second & third
        same_items.extend(list(intersection))
    total_priority_items = sum_priority_items(item_type_priority, same_items)
    return total_priority_items


def sum_priority_items(priority_conf: dict, items: list) -> int:
    """
    Counts total priority value of the items according to given priority config
    """
    partial_func = partial(check_priority_item, priority=priority_conf)
    result = map(partial_func, items)
    return sum(list(result))


def check_priority_item(item: str, priority: dict) -> int:
    """
    Checks priority value of the item type according to given priority config
    """
    return priority[item]


if __name__ == "__main__":
    print("Advent of Code 2022 - Day 3")
    fp = "input"
    start_time = time.time()
    process_data(fp)
    end_time = time.time()
    exc_time = (end_time - start_time) * 1000
    print("Total Execution time: {} ms".format(exc_time))
