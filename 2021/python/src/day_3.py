def get_input() -> list[str]:
    with open("../../inputs/day_3_input.txt", "r") as f:
        return f.read().splitlines()


def first_star(values: list[str]) -> int:
    digits = [0] * len(values[0])
    for value in values:
        for index, digit in enumerate(value):
            if int(digit) == 1:
                digits[index] += 1
            else:
                digits[index] -= 1
    gamma_rate = int("".join(["1" if digit >= 0 else "0" for digit in digits]), 2)
    epsilon_rate = int("".join(["1" if digit < 0 else "0" for digit in digits]), 2)
    return gamma_rate * epsilon_rate


def second_star(values: list[str]) -> int:
    ...


if __name__ == "__main__":
    input_values: list[str] = get_input()
    print(f"Received the following input: {input_values}")
    print(f"Solution 1: {first_star(input_values)}")
    print(f"Solution 2: {second_star(input_values)}")
