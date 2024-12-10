import sys
from functools import reduce

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
Matrix = list[list[str]]


def main():
    args = sys.argv[1:]
    file_name = args[0] + "_" if args else ""
    input_data = _read_input(f"./solutions/day-10/{file_name}input.txt")

    dfs = DFS(input_data)

    print(dfs.solve())


def _read_input(file_path: str) -> Matrix:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return [list(row) for row in raw_data]


class DFS:
    def __init__(self, matrix: Matrix):
        self._matrix = matrix

    def solve(self) -> int:
        return reduce(
            lambda x, y: x + y,
            [
                self._dfs(r, c)
                for r, row in enumerate(self._matrix)
                for c, cell in enumerate(row)
                if cell == "0"
            ],
        )

    def _dfs(self, r: int, c: int) -> int:
        if self._matrix[r][c] == "9":
            return 1

        return reduce(
            lambda x, y: x + y,
            [
                self._dfs(new_r, new_c)
                for new_r, new_c in [
                    (r + r_delta, c + c_delta) for r_delta, c_delta in DIRECTIONS
                ]
                if self._is_valid(new_r, new_c)
                and int(self._matrix[new_r][new_c]) - int(self._matrix[r][c]) == 1
            ],
            0,
        )

    def _is_valid(self, r: int, c: int) -> bool:
        return (
            0 <= r < len(self._matrix)
            and 0 <= c < len(self._matrix[0])
            and self._matrix[r][c].isdigit()
        )


if __name__ == "__main__":
    main()
