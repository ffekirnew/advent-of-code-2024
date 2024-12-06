from collections import defaultdict

NEXT_LETTER = {"M": "A", "A": "S"}
DIRECTIONS = [(1, 1), (-1, 1), (1, -1), (-1, -1)]


def read_input(file_path) -> list[str]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return raw_data


class XMAS_COUNTER:
    def __init__(self, matrix: list[str]) -> None:
        self._matrix = matrix

    def __call__(self) -> int:
        frequency_of_middle_a = defaultdict(int)
        for r, row in enumerate(self._matrix):
            for c, cell in enumerate(row):
                if cell != "M":
                    continue

                for middle_a in self._bfs(r, c):
                    frequency_of_middle_a[middle_a] += 1

        return sum([1 if count > 1 else 0 for count in frequency_of_middle_a.values()])

    def _bfs(
        self, r: int, c: int, directions: list[tuple[int, int]] = DIRECTIONS
    ) -> list[tuple[int, int]]:
        curr_char = self._matrix[r][c]

        if curr_char == "S":
            direction = directions[0]
            a_s_location = r - direction[0], c - direction[1]
            return [a_s_location]

        total_directions = []
        for r_delta, c_delta in directions:
            next_r, next_c = r + r_delta, c + c_delta

            if self._is_expected(next_r, next_c, NEXT_LETTER[curr_char]):
                total_directions.extend(
                    self._bfs(next_r, next_c, [(r_delta, c_delta)]),
                )

        return total_directions

    def _is_expected(self, r: int, c: int, expected: str) -> bool:
        return self._is_inbound(r, c) and self._matrix[r][c] == expected

    def _is_inbound(self, r: int, c: int) -> bool:
        return 0 <= r < len(self._matrix) and 0 <= c < len(self._matrix[0])


def main():
    input = read_input("./solutions/day-4/input.txt")
    xmas_counter = XMAS_COUNTER(input)
    count = xmas_counter()

    print(count)


if __name__ == "__main__":
    main()
