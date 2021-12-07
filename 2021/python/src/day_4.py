import numpy as np
from numpy import ndarray


def get_input() -> tuple[list[int], list[ndarray]]:
    with open("../../inputs/day_4_input.txt", "r") as f:
        picked_numbers: list[int] = [int(number) for number in f.readline().split(",")]
        f.readline()
        boards: list[str] = f.read().split("\n\n")
        boards: list[ndarray] = [np.fromstring(board, dtype=int, sep=" ").reshape(5, 5) for board in boards]
    return picked_numbers, boards


def first_star(picked_numbers: list[int], boards: list[ndarray]) -> int:
    for picked_number in picked_numbers:
        for board in boards:
            if picked_number in board:
                picked_number_indices = np.argwhere(board == picked_number)[0]
                board[tuple(picked_number_indices)] = 0

            # check if there is a column or a row with all 0's.
            if (~board.any(axis=0)).any() or (~board.any(axis=1)).any():
                return board.sum() * picked_number


def second_star() -> int:
    ...


if __name__ == "__main__":
    input_picked_numbers, input_boards = get_input()
    print(f"Solution 1: {first_star(input_picked_numbers, input_boards)}")
    # print(f"Solution 2: {second_star()}")
