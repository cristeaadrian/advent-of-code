def get_results() -> tuple[int, int]:
    with open("../../inputs/day_2_input.txt", "r") as f:
        position, depth, aim = 0, 0, 0

        for line in f.read().splitlines():
            match line.split():
                case ("forward", x):
                    position += int(x)
                    depth += aim * int(x)
                case ("up", x):
                    aim -= int(x)
                case ("down", x):
                    aim += int(x)

    return position * aim, position * depth


if __name__ == "__main__":
    first_star, second_star = get_results()
    print(f"Solution 1: {first_star}")
    print(f"Solution 2: {second_star}")
