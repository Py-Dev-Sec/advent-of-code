import string
import pytest

from day3 import set_priority, process_data_part_one, process_data_part_two, sum_priority_items, check_priority_item


@pytest.fixture
def example_priority():
    return {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
        'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37,
        'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49,
        'X': 50, 'Y': 51, 'Z': 52
    }


@pytest.fixture
def example_input_data():
    return ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']


@pytest.fixture
def example_items():
    return ['p', 'L', 'P', 'v', 't', 's']

@pytest.fixture
def example_all_items():
    items = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    items.extend(upper)
    return items


@pytest.fixture
def example_single_item():
    return "A"


def test_set_priority(example_priority):
    assert set_priority() == example_priority


def test_process_data_part_one(example_input_data, example_priority):
    assert process_data_part_one(example_input_data, example_priority) == 157


def test_process_data_part_two(example_input_data, example_priority):
    assert process_data_part_two(example_input_data, example_priority) == 70


def test_sum_priority_items(example_priority, example_items):
    assert sum_priority_items(example_priority, example_items) == 157


def test_check_priority_item(example_priority, example_single_item):
    assert check_priority_item(example_single_item, example_priority) == example_priority[example_single_item]


def test_check_priority_item_all(example_all_items, example_priority):
    for ascii_char in example_all_items:
        assert check_priority_item(ascii_char, example_priority) == example_priority[ascii_char]
