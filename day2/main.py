from dataclasses import dataclass
from enum import Enum


class OpponentMoves(str, Enum):
    Rock: str = "A"
    Paper: str = "B"
    Scissors: str = "C"


class ResponseMoves(str, Enum):
    Rock: str = "X"
    Paper: str = "Y"
    Scissors: str = "Z"


class Outcome(str, Enum):
    Victory: str = "Z"
    Loss: str = "X"
    Tie: str = "Y"


def who_won(opponent_move: OpponentMoves, your_move: ResponseMoves) -> Outcome:
    if opponent_move == OpponentMoves.Rock:
        if your_move == ResponseMoves.Rock:
            return Outcome.Tie
        elif your_move == ResponseMoves.Paper:
            return Outcome.Victory
        elif your_move == ResponseMoves.Scissors:
            return Outcome.Loss
    elif opponent_move == OpponentMoves.Paper:
        if your_move == ResponseMoves.Rock:
            return Outcome.Loss
        elif your_move == ResponseMoves.Paper:
            return Outcome.Tie
        elif your_move == ResponseMoves.Scissors:
            return Outcome.Victory
    elif opponent_move == OpponentMoves.Scissors:
        if your_move == ResponseMoves.Rock:
            return Outcome.Victory
        elif your_move == ResponseMoves.Paper:
            return Outcome.Loss
        elif your_move == ResponseMoves.Scissors:
            return Outcome.Tie


def which_move(opponent_move: OpponentMoves, outcome: Outcome) -> ResponseMoves:
    if opponent_move == OpponentMoves.Rock:
        if outcome == Outcome.Loss:
            return ResponseMoves.Scissors
        elif outcome == Outcome.Tie:
            return ResponseMoves.Rock
        elif outcome == Outcome.Victory:
            return ResponseMoves.Paper
    elif opponent_move == OpponentMoves.Paper:
        if outcome == Outcome.Loss:
            return ResponseMoves.Rock
        elif outcome == Outcome.Tie:
            return ResponseMoves.Paper
        elif outcome == Outcome.Victory:
            return ResponseMoves.Scissors
    elif opponent_move == OpponentMoves.Scissors:
        if outcome == Outcome.Loss:
            return ResponseMoves.Paper
        elif outcome == Outcome.Tie:
            return ResponseMoves.Scissors
        elif outcome == Outcome.Victory:
            return ResponseMoves.Rock


def what_score(your_move: ResponseMoves, outcome: Outcome) -> int:
    if your_move == ResponseMoves.Rock:
        move_score = 1
    elif your_move == ResponseMoves.Paper:
        move_score = 2
    elif your_move == ResponseMoves.Scissors:
        move_score = 3

    if outcome == Outcome.Loss:
        outcome_score = 0
    elif outcome == Outcome.Tie:
        outcome_score = 3
    elif outcome == Outcome.Victory:
        outcome_score = 6

    return move_score + outcome_score


def first_task():
    all_results = []
    f = open("input.txt")
    for line in f:
        opponent, response = line.strip().split()
        opponent_move = OpponentMoves(opponent)
        your_move = ResponseMoves(response)
        result: Outcome = who_won(opponent_move=opponent_move, your_move=your_move)
        all_results.append([your_move, result])

    total_score = 0
    for res in all_results:
        round_score = what_score(your_move=res[0], outcome=res[1])
        total_score += round_score

    print(total_score)


def second_task():
    all_results = []
    f = open("input.txt")
    for line in f:
        opponent, desired_outcome = line.strip().split()
        opponent_move = OpponentMoves(opponent)
        outcome = Outcome(desired_outcome)
        your_move: Outcome = which_move(opponent_move=opponent_move, outcome=outcome)
        all_results.append([your_move, outcome])

    total_score = 0
    for res in all_results:
        round_score = what_score(your_move=res[0], outcome=res[1])
        total_score += round_score

    print(total_score)


if __name__ == "__main__":
    second_task()
