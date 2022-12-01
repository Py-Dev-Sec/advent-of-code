def process_data(file_path: str) -> tuple[dict, int]:
    """
        Manager. Processes data from the input file and returns solution for part 1 & 2 challenges
    """
    elves = list()
    try:
        elves = count_food_from_file(file_path)
    except Exception as err:
        print("Ups! Something went wrong")
        print("Exception: {}".format(err))
    max_food = search_max_food(elves)
    top_three_max_food = search_top_max_food(elves)
    return max_food, top_three_max_food


def count_food_from_file(filepath: str) -> list:
    """
    Counts how many calories are being carried by each elf from the file
    """
    result = list()
    with open(filepath, "r") as file:
        sum_calories = 0
        elf_id = 1
        for line in file:
            try:
                food_calories = int(line)
                sum_calories += food_calories
            except ValueError:
                if line == "\n":
                    result.append({
                        "elf_id": elf_id,
                        "total_food_calories": sum_calories
                    })
                    sum_calories = 0
                    elf_id += 1

        # include last elf when EOF
        result.append({
            "elf_id": elf_id,
            "total_food_calories": sum_calories
        })
    return result


def search_max_food(elves_list: list) -> dict:
    """
    Searches how many Calories are being carried by the elf carrying the most calories.
    """
    return max(elves_list, key=lambda x: x["total_food_calories"])


def search_top_max_food(elves_list: list, num_elves=3) -> int:
    """
    Searches the sum of the calories carried by given top number of elves
    """
    sorted_food = sorted(elves_list, key=lambda d: d["total_food_calories"], reverse=True)
    total_food = 0
    for i in range(num_elves):
        total_food += sorted_food[i]["total_food_calories"]
    return total_food


if __name__ == "__main__":
    print("Advent of Code 2022 - Day 1")
    fp = "input"
    answer_p1, answer_p2 = process_data(fp)
    print("PART 1 answer: {}".format(answer_p1))
    print("PART 2 answer: {}".format(answer_p2))
