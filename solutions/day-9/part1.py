import sys
from functools import reduce

DOT = "."


def _read_input(file_path: str) -> list[int]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return list(map(int, list(raw_data[0])))


def _pprint(file: list[str]) -> None:
    print("".join(file))


def _solve(input_file: list[int]) -> int:
    file: list[str] = []
    is_file_block = True
    file_id = 0

    for block in input_file:
        for _ in range(block):
            file.append(str(file_id) if is_file_block else DOT)

        file_id += 1 if is_file_block else 0
        is_file_block = not is_file_block

    left, right = 0, len(file) - 1

    while left < right:
        if file[left] != DOT:
            left += 1
            continue

        if file[right] == DOT:
            right -= 1
            continue

        file[left], file[right] = file[right], file[left]
        left += 1
        right -= 1

    file_checksum = reduce(
        lambda x, y: x + y,
        [
            index * int(file_bit)
            for index, file_bit in enumerate(file)
            if file_bit != DOT
        ],
    )
    return file_checksum


def main():
    args = sys.argv[1:]
    file_name = args[0] + "_" if args else ""
    input_data = _read_input(f"./solutions/day-9/{file_name}input.txt")

    print(_solve(input_data))


if __name__ == "__main__":
    main()
