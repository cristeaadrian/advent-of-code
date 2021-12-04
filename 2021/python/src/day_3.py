from collections import Counter

from src.utils import timer


@timer
def get_input() -> tuple[set[str], list[str], int]:
    with open("../../inputs/day_3_input.txt", "r") as f:
        values = f.read().splitlines()
        digits = len(values[0])
        distinct_values = set(values)
        columns = ["".join(value[digit] for value in values) for digit in range(digits)]
        return distinct_values, columns, digits


@timer
def first_star(columns: list[str], digits: int) -> int:
    column_counter = (Counter(column) for column in columns)
    most_common_bits = "".join("1" if column["1"] > column["0"] else "0" for column in column_counter)
    gamma = int(most_common_bits, 2)
    epsilon = gamma ^ (pow(2, digits) - 1)
    return gamma * epsilon


@timer
def second_star(values: set[str], columns: list[str], digits: int) -> int:
    ...


@timer
def main():
    input_distinct_values, input_columns, input_digits = get_input()
    print(f"Solution 1: {first_star(input_columns, input_digits)}")
    print(f"Solution 2: {second_star(input_distinct_values, input_columns, input_digits)}")


if __name__ == "__main__":
    main()
