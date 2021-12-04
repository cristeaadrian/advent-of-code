from collections import Counter

from src.utils import timer


@timer
def get_input() -> list[str]:
    with open("../../inputs/day_3_input.txt", "r") as f:
        values = f.read().splitlines()
        return values


@timer
def first_star(values: list[str]) -> int:
    digits = len(values[0])
    columns = ("".join(value[digit] for value in values) for digit in range(digits))
    bits_per_column = (Counter(column) for column in columns)
    most_common_bits = "".join("1" if column["1"] > column["0"] else "0" for column in bits_per_column)
    gamma = int(most_common_bits, 2)
    epsilon = gamma ^ (pow(2, digits) - 1)
    return gamma * epsilon


@timer
def second_star(values: list[str]) -> int:
    def calculate_ratings(distinct_values: set[str], digits: int, most_common_bit: bool = True) -> int:
        for index in range(digits):
            column = "".join(code[index] for code in distinct_values)
            if column.count("0") <= column.count("1"):
                bit = "1" if most_common_bit else "0"
            else:
                bit = "0" if most_common_bit else "1"
            distinct_values -= {code for code in distinct_values if code[index] == bit}
            if len(distinct_values) == 1:
                return int(distinct_values.pop(), 2)

    oxygen = calculate_ratings(set(values), len(values[0]))
    co2 = calculate_ratings(set(values), len(values[0]), False)
    return oxygen * co2


@timer
def main():
    input_values = get_input()
    print(f"Solution 1: {first_star(input_values)}")
    print(f"Solution 2: {second_star(input_values)}")


if __name__ == "__main__":
    main()
