import sys
from functools import reduce

sys.setrecursionlimit(1_000_000)


STARTING_DIRECTION = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}
NEXT_DIRECTION = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}
DOT = "."
OBSTACLE = "#"
ON_PATH = "X"


def read_input(file_path: str) -> list[list[str]]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return [list(row) for row in raw_data]


class PredictPath:
    def __init__(self, matrix: list[list[str]]) -> None:
        self._matrix = matrix

    def __call__(self) -> list[list[str]] | None:
        for r, row in enumerate(self._matrix):
            for c, cell in enumerate(row):
                if cell in [DOT, OBSTACLE]:
                    continue

                return self._dfs(r, c, STARTING_DIRECTION[cell])

    def _dfs(self, r: int, c: int, direction: tuple[int, int]) -> list[list[str]]:
        self._matrix[r][c] = ON_PATH
        next_r, next_c = self._get_next(r, c, direction)

        if not self._is_inbound(next_r, next_c):
            return self._matrix

        while not self._is_valid(next_r, next_c):
            direction = NEXT_DIRECTION[direction]
            next_r, next_c = self._get_next(r, c, direction)

        return self._dfs(next_r, next_c, direction)

    def _is_valid(self, r: int, c: int) -> bool:
        return self._matrix[r][c] != OBSTACLE

    def _is_inbound(self, r: int, c: int) -> bool:
        return 0 <= r < len(self._matrix) and 0 <= c < len(self._matrix[0])

    def _get_next(self, r: int, c: int, direction: tuple[int, int]) -> tuple[int, int]:
        return r + direction[0], c + direction[1]


def main():
    matrix = read_input("./solutions/day-6/input.txt")

    predict_path = PredictPath(matrix)
    if matrix := predict_path():
        total_on_path = reduce(
            lambda x, y: x + y,
            [row.count(ON_PATH) for row in matrix],
        )
        print(total_on_path)


if __name__ == "__main__":
    main()
