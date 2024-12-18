from sys import argv, setrecursionlimit

setrecursionlimit(10**6)


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def main():
    args = argv[1:]
    test_file_name = "test_input" if args and args[0] == "test" else "input"
    input_data = _read_input(f"./solutions/day-18/{test_file_name}.txt")

    ROWS, COLS = (71, 71) if test_file_name == "input" else (7, 7)
    HALF_WAY = 1024 if test_file_name == "input" else 12

    input_data = set(input_data[:HALF_WAY])
    grid = [
        ["#" if (r, c) in input_data else "." for c in range(COLS)] for r in range(ROWS)
    ]

    memory_space = MemorySpace(grid)
    print("Steps to escape:", memory_space.escape())


class MemorySpace:
    def __init__(self, grid: list[list[str]]) -> None:
        self._grid = grid

    def escape(self) -> int:
        level = [(0, 0, 0)]
        while level:
            next_level = []
            for row, col, steps in level:
                if (row, col) == (len(self._grid) - 1, len(self._grid[0]) - 1):
                    return steps

                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col + dc
                    if not self._is_inbound(new_row, new_col):
                        continue

                    if self._grid[new_row][new_col] == ".":
                        next_level.append((new_row, new_col, steps + 1))
                        self._grid[new_row][new_col] = "O"

            level = next_level

        return -1

    def _is_inbound(self, row: int, col: int) -> bool:
        return 0 <= row < len(self._grid) and 0 <= col < len(self._grid[0])


def _read_input(file_path: str):
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return [tuple(map(int, row.split(","))) for row in raw_data]


def pprint(maze: list[list[str]]):
    for row in maze:
        print("".join(row))


if __name__ == "__main__":
    main()
