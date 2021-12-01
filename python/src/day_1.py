import itertools as it


def get_input() -> list[int]:
    with open("../../inputs/day_1_input.txt", "r") as f:
        return [int(value) for value in f.read().splitlines()]


def first_star(values: list[int]) -> int:
    return sum(it.starmap(lambda x, y: x < y, zip(values, values[1:])))


def second_star(values: list[int]) -> int:
    three_measurement_window = [x + y + z for x, y, z in zip(values, values[1:], values[2:])]
    return sum(it.starmap(lambda x, y: x < y, zip(three_measurement_window, three_measurement_window[1:])))


if __name__ == "__main__":
    input_values: list[int] = get_input()
    print(f"Solution 1: {first_star(input_values)}")
    print(f"Solution 2: {second_star(input_values)}")
