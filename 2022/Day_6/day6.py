import time


def process_data(filepath: str) -> None:
    with open(filepath, "r") as file:
        input_datastream = file.readlines()
    
    process_data_part_one(input_datastream)
    process_data_part_two(input_datastream)


def process_data_part_one(input_datastream: str) -> None:
    offset = 4
    for line in input_datastream:
        result = find_first_marker(line, offset)
        print("First packet marker: {}".format(repr(line[result[0]:result[1]])))
        print("First marker after character: {}".format(result[1]))


def process_data_part_two(input_datastream: str) -> None:
    offset = 14
    for line in input_datastream:
        result = find_first_marker(line, offset)
        print("First start-of-message marker: {}".format(repr(line[result[0]:result[1]])))
        print("First start-of-message after character: {}".format(result[1]))


def find_first_marker(input: str, offset: int) -> list:
    start_pos = None
    end_pos = None
    for ch_ind in range(0, len(input)):
        marker = input[ch_ind:ch_ind+offset]
        if len(set(marker)) == len(marker):
            start_pos = ch_ind
            end_pos = ch_ind+offset
            break
    return [start_pos, end_pos]

if __name__ == "__main__":
    print("Advent of Code 2022 - Day 4")
    fp = "input"
    start_time = time.time()
    process_data(fp)
    end_time = time.time()
    exc_time = (end_time - start_time) * 1000
    print("Total Execution time: {} ms".format(exc_time))