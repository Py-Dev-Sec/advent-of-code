import pytest

from day2 import calculate_score, calculate_score_with_guide, process_score, process_score_with_guide


@pytest.fixture
def example_input_data():
    return [
        "A Y",
        "B X",
        "C Z"
    ]


@pytest.fixture
def example_processed_data():
    return [8, 1, 6]


@pytest.fixture
def example_processed_data_with_guide():
    return [4, 1, 7]


def test_calculate_score(example_input_data):
    assert calculate_score(example_input_data) == 15


def test_calculate_score_with_guide(example_input_data):
    assert calculate_score_with_guide(example_input_data) == 12


def test_process_score(example_input_data, example_processed_data):
    assert list(map(process_score, example_input_data)) == example_processed_data


def test_calculate_score_with_guide(example_input_data, example_processed_data_with_guide):
    assert list(map(process_score_with_guide, example_input_data)) == example_processed_data_with_guide
