import pytest

from day6 import find_first_marker

@pytest.fixture
def single_input():
    return {
        "data": "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
        "marker_pos_packet": [3, 7],
        "marker_pos_msg": [5, 19]
    }

@pytest.fixture
def input_datastreams():
    return [
        {
            "data": "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
            "marker_pos_packet": [3, 7],
            "marker_pos_msg": [5, 19]
        },
        {
            "data": "bvwbjplbgvbhsrlpgdmjqwftvncz",
            "marker_pos_packet": [1, 5],
            "marker_pos_msg": [9, 23]
        },
        {
            "data": "nppdvjthqldpwncqszvftbrmjlhg",
            "marker_pos_packet": [2, 6],
            "marker_pos_msg": [9, 23]
        },
        {
            "data": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            "marker_pos_packet": [6, 10],
            "marker_pos_msg": [15, 29]
        },
        {
            "data": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
            "marker_pos_packet": [7, 11],
            "marker_pos_msg": [12, 26]
        }
    ]

@pytest.fixture
def offset_packet_marker():
    """
        Offset for start-of-packet marker
    """
    return 4

@pytest.fixture
def offset_msg_marker():
    """
        Offset for start-of-message marker
    """
    return 14


def test_find_first_marker_packet(single_input, offset_packet_marker):
    assert find_first_marker(single_input["data"], offset_packet_marker) == single_input["marker_pos_packet"]


def test_find_first_marker_msg(single_input, offset_msg_marker):
    assert find_first_marker(single_input["data"], offset_msg_marker) == single_input["marker_pos_msg"]


def test_find_first_marker_packet_multi(input_datastreams, offset_packet_marker):
    for datastream in input_datastreams:
        assert find_first_marker(datastream["data"], offset_packet_marker) == datastream["marker_pos_packet"]


def test_find_first_marker_msg_multi(input_datastreams, offset_msg_marker):
    for datastream in input_datastreams:
        assert find_first_marker(datastream["data"], offset_msg_marker) == datastream["marker_pos_msg"]