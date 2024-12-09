import sys
from collections import namedtuple
from functools import reduce

FreeSpace = namedtuple("FreeSpace", ["starting_index", "length"])
FileBlock = namedtuple("FileBlock", ["starting_index", "length", "file_id"])

DOT = "."


def main():
    args = sys.argv[1:]
    file_name = args[0] + "_" if args else ""
    input_data = _read_input(f"./solutions/day-9/{file_name}input.txt")

    print(_solve(input_data))


def _read_input(file_path: str) -> list[int]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return list(map(int, list(raw_data[0])))


def _solve(input_file: list[int]) -> int:
    is_file_block = True

    file: list[str] = []
    file_id = 0
    free_spaces: list[FreeSpace] = []
    file_blocks: list[FileBlock] = []
    for block in input_file:
        for _ in range(block):
            file.append(str(file_id) if is_file_block else DOT)

        if is_file_block:
            file_blocks.append(FileBlock(len(file) - block, block, file_id))
            file_id += 1
        else:
            free_spaces.append(FreeSpace(len(file) - block, block))

        is_file_block = not is_file_block

    _move_file_blocks(file, free_spaces, file_blocks)

    return reduce(
        lambda x, y: x + y,
        [
            index * int(file_bit)
            for index, file_bit in enumerate(file)
            if file_bit != DOT
        ],
    )


def _pprint(file: list[str]) -> None:
    print("".join(file))


def _move_file_blocks(
    file: list[str],
    free_spaces: list[FreeSpace],
    file_blocks: list[FileBlock],
) -> None:
    for file_block in reversed(file_blocks):
        for free_space_index, free_space in enumerate(free_spaces):
            if free_space.length < file_block.length:
                continue

            if free_space.starting_index >= file_block.starting_index:
                break

            i = 0
            for _ in range(
                file_block.starting_index,
                file_block.starting_index + file_block.length,
            ):
                file[free_space.starting_index + i] = str(file_block.file_id)
                file[file_block.starting_index + i] = DOT
                i += 1

            free_spaces[free_space_index] = FreeSpace(
                free_space.starting_index + file_block.length,
                free_space.length - file_block.length,
            )
            break


if __name__ == "__main__":
    main()
