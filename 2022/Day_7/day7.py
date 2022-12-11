import time
import re
import json


def process_data(filepath: str) -> None:
    with open(filepath, "r") as file:
        input = file.readlines()
    answer_p1 = process_data_part_one(input)
    print("Part 1 answer: {}".format(answer_p1["total_size_dirs"]))
    files = answer_p1["filesystem"]
    answer_p2 = process_data_part_two(files)
    print("Part 2 answer: ", answer_p2)


def process_data_part_one(cli: str) -> dict:
    result = {
        "filesystem": None,
        "total_size_dirs": None
    }
    cmd_move_up = r"\$\s{1}cd\s{1}[.]{2}"
    cmd_ls_file = r"[0-9]+\s{1}[a-zA-Z.]+"
    cmd_ls_dir = r"\$\s{1}ls"

    files = dict()
    dirs_list = list()
    for line in cli:
        cmd_line = line.strip()
        if cmd_line.startswith("$ cd"):
            if not re.search(cmd_move_up, line):
                dir_name = get_args(cmd_line)[2]
                dirs_list.append(dir_name)
                absolute_path = get_absolute_path(dirs_list)
                if absolute_path not in files.keys():
                    files[absolute_path] = {"size": 0, "name": dir_name, "files": list()}
            else:
                dirs_list.pop()
        # TODO: you can remove below condition for ls dir content command or use it for future refactor/update
        if re.search(cmd_ls_dir, line):
            pass
        if re.search(cmd_ls_file, line):
            file_size, file_name = get_args(cmd_line)
            file_size = int(file_size)
            absolute_path = get_absolute_path(dirs_list)
            files[absolute_path]["files"].append({"name": file_name, "size": file_size})
            update_total_size(dirs_list, files, file_size)
    # DEBUG - uncomment if you're curious how filesystem helper dict looks
    #       key -> string representation of absolute path to dir
    #       value -> dict with some metadata like dir name, list of files and total_size of dir
    # print_filesystem(files)

    size_limit = 100000
    total_size = get_total_size(files, size_limit)
    result["filesystem"] = files
    result["total_size_dirs"] = total_size
    return result


def process_data_part_two(filesystem: dict) -> dict:
    total_disk_space = 70000000
    update_space_req = 30000000
    root_dir = "/"
    total_space = filesystem[root_dir]["size"]
    unused_space = total_disk_space - total_space

    if unused_space < update_space_req:
        missed_space = update_space_req - unused_space
    else:
        missed_space = 0

    selected_dirs = []
    for path in filesystem.keys():
        if filesystem[path]["size"] >= missed_space:
            selected_dirs.append(filesystem[path]["size"])
    return min(selected_dirs)


def get_args(cmd_line: str) -> list:
    return cmd_line.split()


def get_absolute_path(path: list) -> str:
    return "/".join(path)


def update_total_size(dir_path: list, filesystem: dict, file_size_to_add: int) -> None:
    update_path = list()
    for parent_dir in dir_path:
        update_path.append(parent_dir)
        absolute_path = get_absolute_path(update_path)
        filesystem[absolute_path]["size"] += file_size_to_add


def get_total_size(filesystem: dict, limit_dir_size: int) -> int:
    total_size = 0
    for path in filesystem.keys():
        if filesystem[path]["size"] <= limit_dir_size:
            total_size += filesystem[path]["size"]
    return total_size


def print_filesystem(filesystem: dict) -> None:
    print(json.dumps(filesystem, indent=4))


if __name__ == "__main__":
    print("Advent of Code 2022 - Day 4")
    fp = "input"
    start_time = time.time()
    process_data(fp)
    end_time = time.time()
    exc_time = (end_time - start_time) * 1000
    print("Total Execution time: {} ms".format(exc_time))