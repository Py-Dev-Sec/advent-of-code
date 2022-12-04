import pytest

from day4 import convert_assignment, convert_sections_to_set, convert_range_section_str, check_subset, check_intersection


@pytest.fixture
def example_input_data():
    return ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']


@pytest.fixture
def example_converted_data():
    return [[{2, 3, 4}, {8, 6, 7}], [{2, 3}, {4, 5}], [{5, 6, 7}, {8, 9, 7}], [{2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}],
            [{6}, {4, 5, 6}], [{2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}]]


@pytest.fixture
def example_section_str():
    return '2-4,6-8'

@pytest.fixture
def example_set_sections():
    return [{2, 3, 4}, {8, 6, 7}]


@pytest.fixture
def example_single_section_str():
    return '2-4'

@pytest.fixture
def example_pos_section():
    return [2, 4]


@pytest.fixture
def example_set_a():
    return {6, 7}


@pytest.fixture
def example_set_b():
    return {5, 6, 7, 8}


@pytest.fixture
def example_set_c():
    return {7, 8, 9}


def test_convert_assignment(example_input_data, example_converted_data):
    assert convert_assignment(example_input_data) == example_converted_data


def test_convert_sections_to_set(example_section_str, example_set_sections):
    assert convert_sections_to_set(example_section_str) == example_set_sections


def test_convert_range_section_str(example_single_section_str, example_pos_section):
    assert convert_range_section_str(example_single_section_str) == example_pos_section


def test_check_subset(example_set_a, example_set_b):
    assert check_subset(example_set_a, example_set_b)


def test_check_intersection(example_set_b, example_set_c):
    assert check_intersection(example_set_b, example_set_c)
