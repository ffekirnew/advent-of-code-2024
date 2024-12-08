import sys
from collections import defaultdict, deque

DOT = "."
ANTINODE = "#"


def read_input(file_path: str) -> list[list[str]]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return [list(row) for row in raw_data]


class Antenaes:
    def __init__(self, grid: list[list[str]]) -> None:
        self._grid = grid

    def get_total_antinodes_for_grid(self) -> int:
        total = 0

        antenaes = self._get_all_antenaes(self._grid)
        for same_frequency_antenaes in antenaes:
            total += self._get_total_antinodes(same_frequency_antenaes)

        return total

    def _get_total_antinodes(
        self, same_frequency_antenaes: list[tuple[int, int]]
    ) -> int:
        total = 0

        points_in_line = [
            (p1, p2)
            for p1 in same_frequency_antenaes
            for p2 in same_frequency_antenaes
            if p1 < p2
        ]

        for p1, p2 in points_in_line:
            for antinode in self._get_antinode_locations(p1, p2):
                if self._is_inbound(antinode):
                    total += self._grid[antinode[0]][antinode[1]] != ANTINODE
                    self._grid[antinode[0]][antinode[1]] = ANTINODE

        return total

    def _get_antinode_locations(
        self, p1: tuple[int, int], p2: tuple[int, int]
    ) -> list[tuple[int, int]]:
        direction = self._get_direction(p1, p2)
        points_in_line = deque([p1, p2])

        while new_p1 := self._get_point_before_p1(points_in_line[0], direction):
            if not self._is_inbound(new_p1):
                break
            points_in_line.appendleft(new_p1)

        while new_p2 := (self._get_point_after_p2(points_in_line[-1], direction)):
            if not self._is_inbound(new_p2):
                break
            points_in_line.append(new_p2)

        return list(points_in_line)

    def _get_point_before_p1(
        self, p1: tuple[int, int], direction: tuple[int, int]
    ) -> tuple[int, int]:
        return p1[0] + direction[0], p1[1] + direction[1]

    def _get_point_after_p2(
        self, p2: tuple[int, int], direction: tuple[int, int]
    ) -> tuple[int, int]:
        return p2[0] - direction[0], p2[1] - direction[1]

    def _is_inbound(self, point: tuple[int, int]) -> bool:
        return 0 <= point[0] < len(self._grid) and 0 <= point[1] < len(self._grid[0])

    def _get_direction(
        self, p1: tuple[int, int], p2: tuple[int, int]
    ) -> tuple[int, int]:
        return p1[0] - p2[0], p1[1] - p2[1]

    def _get_all_antenaes(
        self,
        grid: list[list[str]],
    ) -> list[list[tuple[int, int]]]:
        antenaes = defaultdict(list)
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell != DOT:
                    antenaes[cell].append((r, c))

        return list(antenaes.values())

    def pprint(self):
        for row in self._grid:
            print("".join(row))


def main():
    args = sys.argv[1:]
    file_name = args[0] + "_" if args else ""
    input_data = read_input(f"./solutions/day-8/{file_name}input.txt")

    antenaes = Antenaes(input_data)
    total = antenaes.get_total_antinodes_for_grid()

    print(total)


if __name__ == "__main__":
    main()
