import pytest

from day1 import search_max_food, search_top_max_food, count_food_from_file


@pytest.fixture
def example_elves_data():
    return [
        {'elf_id': 1, 'total_food_calories': 6000},
        {'elf_id': 2, 'total_food_calories': 4000},
        {'elf_id': 3, 'total_food_calories': 11000},
        {'elf_id': 4, 'total_food_calories': 24000},
        {'elf_id': 5, 'total_food_calories': 10000}
    ]


def test_search_max_food(example_elves_data):
    assert search_max_food(example_elves_data) == {'elf_id': 4, 'total_food_calories': 24000}


def test_search_top_three_max_food(example_elves_data):
    assert search_top_max_food(example_elves_data) == 45000


def test_count_food_from_file(example_elves_data):
    filepath = "test_input"
    assert count_food_from_file(filepath) == example_elves_data
