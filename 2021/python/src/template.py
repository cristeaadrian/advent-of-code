from typing import Any


def get_input() -> list[Any]:
    with open("../../inputs/day_x_input.txt", "r") as f:
        return f.read().splitlines()


def first_star() -> int:
    ...


def second_star() -> int:
    ...


if __name__ == "__main__":
    input_values: list[Any] = get_input()
    print(f"Solution 1: {first_star()}")
    print(f"Solution 2: {second_star()}")
