from dataclasses import dataclass
from enum import Enum


class Command(str, Enum):
    up = "up"
    down = "down"
    forward = "forward"


@dataclass
class SubmarineCommands:
    command: Command
    value: int


def get_input() -> list[SubmarineCommands]:
    with open("../../inputs/day_2_input.txt", "r") as f:
        inputs = map(str.split, f.read().splitlines())
        processed_commands = [SubmarineCommands(Command(command[0]), int(command[1])) for command in inputs]
        return processed_commands


def first_star(values: list[SubmarineCommands]) -> int:
    depth: int = sum(
        -x.value if x.command == Command.up else x.value
        for x in filter(lambda x: x.command == Command.up or x.command == Command.down, values)
    )
    horizontal_position: int = sum(x.value for x in values if x.command == Command.forward)
    return depth * horizontal_position


def second_star(values: list[SubmarineCommands]) -> int:
    ...


if __name__ == "__main__":
    input_values: list[SubmarineCommands] = get_input()
    print(f"Solution 1: {first_star(input_values)}")
    # print(f"Solution 2: {second_star(input_values)}")
