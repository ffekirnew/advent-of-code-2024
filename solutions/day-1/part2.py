from functools import reduce
from typing import Counter


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
    right_freq = Counter(right)

    total_similarity_score = reduce(
        lambda x, y: x + y, [number * right_freq[number] for number in left]
    )

    print(total_similarity_score)


if __name__ == "__main__":
    main()
