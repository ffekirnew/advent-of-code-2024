import sys
from functools import reduce

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def main():
    args = sys.argv[1:]
    test_file_name = "test_input" if args and args[0] == "test" else "input"
    input_data = _read_input(f"./solutions/day-12/{test_file_name}.txt")

    garden = Gargen(input_data)
    result = garden.solve()

    print(result)


class Gargen:
    def __init__(self, data: list[list[str]]):
        self._data = data
        self._visited = set()

    def solve(self) -> int:
        rows, cols = len(self._data), len(self._data[0])
        results = [self._dfs(r, c) for r in range(rows) for c in range(cols)]

        total = 0
        for result in results:
            total += result[0] * result[1]
        return total

    def _dfs(self, r: int, c: int) -> tuple[int, int]:
        if (r, c) in self._visited:
            return 0, 0

        self._visited.add((r, c))

        area, perimeter = 1, 0
        for r_delta, c_delta in DIRECTIONS:
            new_r, new_c = r + r_delta, c + c_delta
            if (
                self._is_inbounds(new_r, new_c)
                and self._data[new_r][new_c] == self._data[r][c]
            ):
                result = self._dfs(new_r, new_c)
                area += result[0]
                perimeter += result[1]
            else:
                perimeter += 1

        return area, perimeter

    def _is_inbounds(self, r: int, c: int) -> bool:
        return 0 <= r < len(self._data) and 0 <= c < len(self._data[0])


def _read_input(file_path: str) -> list[list[str]]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return [list(row) for row in raw_data]


if __name__ == "__main__":
    main()
