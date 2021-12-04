from collections import Counter


def get_input() -> list[str]:
    with open("../../inputs/day_3_input.txt", "r") as f:
        return f.read().splitlines()


def first_star(values: list[str]) -> int:
    digits = len(values[0])
    columns = ("".join(value[digit] for value in values) for digit in range(digits))
    column_counter = (Counter(column) for column in columns)
    most_common_bits = "".join("1" if column["1"] > column["0"] else "0" for column in column_counter)
    gamma = int(most_common_bits, 2)
    epsilon = gamma ^ (pow(2, digits) - 1)
    return gamma * epsilon


def second_star(values: list[str]) -> int:
    ...


if __name__ == "__main__":
    input_values: list[str] = get_input()
    print(f"Solution 1: {first_star(input_values)}")
    print(f"Solution 2: {second_star(input_values)}")
