import sys


def read_input(file_path: str) -> list[tuple[int, list[int]]]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    data = []
    for row in raw_data:
        resuslt, numbers = row.split(": ")

        data.append(
            (
                int(resuslt),
                list(map(int, numbers.split(" "))),
            ),
        )

    return data


def backtrack(d: list[int], target: int, index: int = 0, total: int = 0) -> int:
    if index == len(d):
        return total == target

    if total > target:
        return False

    return backtrack(d, target, index + 1, total + d[index]) or backtrack(
        d, target, index + 1, total * d[index]
    )


def main():
    args = sys.argv[1:]
    file_name = args[0] + "_" if args else ""
    input_data = read_input(f"./solutions/day-7/{file_name}input.txt")

    total = 0
    for result, data in input_data:
        if backtrack(data, result):
            total += result

    print(total)


if __name__ == "__main__":
    main()
