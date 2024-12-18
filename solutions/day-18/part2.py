from sys import argv, setrecursionlimit

setrecursionlimit(10**6)


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def main():
    args = argv[1:]
    test_file_name = "test_input" if args and args[0] == "test" else "input"
    fall_positions = _read_input(f"./solutions/day-18/{test_file_name}.txt")

    ROWS, COLS = (71, 71) if test_file_name == "input" else (7, 7)
    HALF_WAY = 1024 if test_file_name == "input" else 12

    memory_space = MemorySpace([["." for _ in range(COLS)] for _ in range(ROWS)])
    for index, (row, col) in enumerate(fall_positions):
        memory_space.corrupt(row, col)

        if index < HALF_WAY:
            continue

        if not memory_space.escape():
            print("Escape no longer possible after corruping:", (row, col))
            return


class MemorySpace:
    def __init__(self, grid: list[list[str]]) -> None:
        self._grid = grid

    def corrupt(self, row: int, col: int) -> None:
        self._grid[row][col] = "#"

    def escape(self) -> int:
        level = [(0, 0, 0)]
        visited = set([(0, 0)])

        while level:
            next_level = []
            for row, col, steps in level:
                if (row, col) == (len(self._grid) - 1, len(self._grid[0]) - 1):
                    return steps

                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col + dc

                    if (new_row, new_col) in visited or not self._is_inbound(
                        new_row, new_col
                    ):
                        continue

                    if self._grid[new_row][new_col] == ".":
                        visited.add((new_row, new_col))
                        next_level.append((new_row, new_col, steps + 1))

            level = next_level

        return 0

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
