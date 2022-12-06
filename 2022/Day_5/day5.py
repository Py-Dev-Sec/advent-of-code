import re
import time
from collections import deque


def process_data(filepath: str) -> None:
    with open(filepath, "r") as file:
        input_data = file.readlines()
    work_manifest = prepare_work_env(input_data)
    process_data_part_one(work_manifest)
    process_data_part_two(work_manifest)


def process_data_part_one(work_manifest: dict) -> None:
    stacks = dict()
    init_stacks(stacks, work_manifest["num_stacks"])
    init_load_stacks(stacks, work_manifest["crates_init_list"])
    move_crates_cratemover9000(stacks, work_manifest["moves_list"])
    answer_p1 = ""
    for stack_id in stacks.keys():
        answer_p1 += get_top_crate(stacks[stack_id]).replace("[", "").replace("]", "")
    print("Part 1 answer: {}".format(answer_p1))


def process_data_part_two(work_manifest: dict) -> None:
    stacks = dict()
    init_stacks(stacks, work_manifest["num_stacks"])
    init_load_stacks(stacks, work_manifest["crates_init_list"])
    move_crates_cratemover9001(stacks, work_manifest["moves_list"])
    answer_p2 = ""
    for stack_id in stacks.keys():
        answer_p2 += get_top_crate(stacks[stack_id]).replace("[", "").replace("]", "")
    print("Part 1 answer: {}".format(answer_p2))


def prepare_work_env(input_data: list) -> dict:
    num_stacks = 0
    moves_list = list()
    crates_init_list = list()
    for line in input_data:
        if contains_number(line) and num_stacks == 0:
            num_stacks = len(line.split())
        if "move" in line:
            moves_list.append(line)
        if not contains_number(line) and line != "\n":
            crates_init_list.append(line)
    return {
        "num_stacks": num_stacks,
        "moves_list": moves_list,
        "crates_init_list": crates_init_list
    }


def contains_number(input_line: str) -> bool:
    return any(char.isdigit() for char in input_line)


def init_stacks(stack_ref: dict, num_stacks: int) -> None:
    for st_id in range(num_stacks):
        stack_ref["stack_"+str(st_id+1)] = deque()


def init_load_stacks(stack_ref: dict, crates_init_list: list) -> None:
    for line in reversed(crates_init_list):
        crates = list()
        for ch_ind in range(1, len(line), 4):
            crate_id = line[ch_ind:ch_ind+1]
            crates.append(crate_id)
        for crate_id in range(len(crates)):
            if crates[crate_id] != " ":
                stack_ref["stack_"+str(crate_id+1)].append(crates[crate_id])


def move_crates_cratemover9000(stack_ref: dict, moves_list: list) -> None:
    regex_move = r"move [0-9]+"
    regex_from = r"from [0-9]+"
    regex_to = r"to [0-9]+"
    stack_id_code = "stack_"

    for move in moves_list:
        from_match = find_instruction(move, regex_from)
        src_stack_id = process_instruction(from_match, "from ", stack_id_code)
        to_match = find_instruction(move, regex_to)
        dest_stack_id = process_instruction(to_match, "to ", stack_id_code)
        move_match = find_instruction(move, regex_move)
        num_crates_to_move = int(process_instruction(move_match, "move ", ""))

        for move_nr in range(num_crates_to_move):
            crate_obj = stack_ref[src_stack_id].pop()
            stack_ref[dest_stack_id].append(crate_obj)


def move_crates_cratemover9001(stack_ref: dict, moves_list: list) -> None:
    regex_move = r"move [0-9]+"
    regex_from = r"from [0-9]+"
    regex_to = r"to [0-9]+"
    stack_id_code = "stack_"

    for move in moves_list:
        from_match = find_instruction(move, regex_from)
        src_stack_id = process_instruction(from_match, "from ", stack_id_code)
        to_match = find_instruction(move, regex_to)
        dest_stack_id = process_instruction(to_match, "to ", stack_id_code)
        move_match = find_instruction(move, regex_move)
        num_crates_to_move = int(process_instruction(move_match, "move ", ""))

        same_order_crates = list()
        for move_nr in range(num_crates_to_move):
            crate_obj = stack_ref[src_stack_id].pop()
            same_order_crates.append(crate_obj)
        stack_ref[dest_stack_id].extend(reversed(same_order_crates))


def find_instruction(line: str, instr_regex: str) -> re.Match:
    return re.search(instr_regex, line)


def process_instruction(instr_ref: re.Match, pre_instr: str, post_instr: str) -> str:
    return instr_ref.group().replace(pre_instr, post_instr)


def get_top_crate(stack: deque) -> str:
    return stack[-1]


if __name__ == "__main__":
    print("Advent of Code 2022 - Day 4")
    fp = "input"
    start_time = time.time()
    process_data(fp)
    end_time = time.time()
    exc_time = (end_time - start_time) * 1000
    print("Total Execution time: {} ms".format(exc_time))
