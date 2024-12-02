from functools import reduce


def read_input(file_path) -> tuple[list[int], list[int]]:
    with open(file_path, "r") as file:
        raw_data = file.read().split("\n")

    left, right = [], []
    for line in raw_data:
        line = line.split(" ")
        if len(line) == 1:
            continue

        left.append(int(line[0]))
        right.append(int(line[3]))

    return left, right


def main():
    left, right = read_input("./solutions/day-1/input.txt")

    total_distance = reduce(
        lambda left_value, right_value: left_value + right_value,
        [abs(line[0] - line[1]) for line in zip(sorted(left), sorted(right))],
    )

    print(total_distance)


if __name__ == "__main__":
    main()
