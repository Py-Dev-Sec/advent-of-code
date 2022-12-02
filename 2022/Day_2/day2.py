import time

start_time = time.time()

# All possible scores for Rock, Paper, Scissors game with AoC rules.
# Oponent's moves: A, B, C
# Player's moves: X, Y, Z
# Shapes mapper:
#   ROCK -> A / X
#   PAPER -> B / Y
#   SCISSORS -> C /Z
# Shapes score:
#   ROCK -> 1
#   PAPER -> 2
#   SCISSORS -> 3
# Game round score:
#   LOSS -> 0
#   DRAW -> 3
#   WIN -> 6
# Player total score = Game round score + Shape score
# Ex.: Draw total score (Rock vs Rock -> A X): 3 + 1 = 4
POSSIBLE_SCORES = [
    {"A": "X", "total": 4},
    {"B": "Y", "total": 5},
    {"C": "Z", "total": 6},
    {"A": "Y", "total": 8},
    {"B": "Z", "total": 9},
    {"C": "X", "total": 7},
    {"A": "Z", "total": 3},
    {"B": "X", "total": 1},
    {"C": "Y", "total": 2}
]

# Strategy guide for the player's move:
# X -> LOSS
# Y -> DRAW
# Z -> WIN
STRATEGY_GUIDE = {
    "X": [
        {"A": "Z", "total": 3},
        {"B": "X", "total": 1},
        {"C": "Y", "total": 2}
    ],
    "Y": [
        {"A": "X", "total": 4},
        {"B": "Y", "total": 5},
        {"C": "Z", "total": 6}
    ],
    "Z": [
        {"A": "Y", "total": 8},
        {"B": "Z", "total": 9},
        {"C": "X", "total": 7},
    ]
}


def process_data(filepath: str) -> None:
    """
    Wrapper for processing input data from the file.
    """
    with open(filepath, "r") as file:
        rounds = [line.strip() for line in file.readlines()]
    total_score = calculate_score(rounds)
    print("PART 1 - Total score: {}".format(total_score))
    total_score = calculate_score_with_guide(rounds)
    print("PART 2 - Total score: {}".format(total_score))


def calculate_score(game_rounds: list) -> int:
    """
    Calculates total score for player (not an oponent) according to given input game rounds.
    """
    mapped = map(process_score, game_rounds)
    total_score = list(mapped)
    return sum(total_score)


def process_score(game_round: str) -> int:
    """
    Mapper for single game's round according to shape/round scoring rules and player/oponent decision.
    """
    oponent_move, player_move = game_round.split()
    for pos_score in POSSIBLE_SCORES:
        keys = pos_score.keys()
        if oponent_move in keys and pos_score[oponent_move] == player_move:
            return pos_score["total"]


def calculate_score_with_guide(game_rounds: list) -> int:
    """
    Calculates total score for player (not an oponent) according to given input game rounds and strategy guide.
    """
    mapped = map(process_score_with_guide, game_rounds)
    total_score = list(mapped)
    return sum(total_score)


def process_score_with_guide(game_round: str) -> int:
    """
    Mapper for single game's round according to shape/round scoring rules and player/oponent decision.
    Decides player's move according to the strategy guide.
    """
    oponent_move, player_move = game_round.split()
    for pos_score in STRATEGY_GUIDE[player_move]:
        keys = pos_score.keys()
        if oponent_move in keys:
            return pos_score["total"]


if __name__ == "__main__":
    print("Advent of Code 2022 - Day 2")
    fp = "input"
    process_data(fp)
    end_time = time.time()
    exc_time = (end_time - start_time) * 1000
    print("Execution time: {} ms".format(exc_time))
