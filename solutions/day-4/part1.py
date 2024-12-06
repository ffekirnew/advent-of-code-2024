NEXT_LETTER = {"X": "M", "M": "A", "A": "S"}
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def read_input(file_path) -> list[str]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return raw_data


class XMAS_COUNTER:
    def __init__(self, matrix: list[str]) -> None:
        self._matrix = matrix

    def __call__(self) -> int:
        total = 0
        for r, row in enumerate(self._matrix):
            for c, cell in enumerate(row):
                if cell == "X":
                    total += self._bfs(r, c)

        return total

    def _bfs(
        self, r: int, c: int, directions: list[tuple[int, int]] = DIRECTIONS
    ) -> int:
        curr_char = self._matrix[r][c]

        if curr_char == "S":
            return 1

        total = 0
        for r_delta, c_delta in directions:
            next_r, next_c = r + r_delta, c + c_delta

            if self._is_expected(next_r, next_c, NEXT_LETTER[curr_char]):
                total += self._bfs(next_r, next_c, [(r_delta, c_delta)])

        return total

    def _is_expected(self, r: int, c: int, expected: str) -> bool:
        return self._is_inbound(r, c) and self._matrix[r][c] == expected

    def _is_inbound(self, r: int, c: int) -> bool:
        return 0 <= r < len(self._matrix) and 0 <= c < len(self._matrix[0])


def main():
    input = read_input("./solutions/day-4/test_input.txt")
    xmas_counter = XMAS_COUNTER(input)
    count = xmas_counter()

    print(count)


if __name__ == "__main__":
    main()
