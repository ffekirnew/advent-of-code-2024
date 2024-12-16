import heapq
import sys
from functools import cache
from math import inf

sys.setrecursionlimit(10**6)


def main():
    args = sys.argv[1:]
    test_file_name = "test_input" if args and args[0] == "test" else "input"
    input_data = _read_input(f"./solutions/day-16/{test_file_name}.txt")

    maze = Maze(input_data)
    x, y = 0, 0
    for r, row in enumerate(input_data):
        for c, cell in enumerate(row):
            if cell == "S":
                x, y = r, c

    print(maze.a_star(x, y, (0, 1)))


class Maze:
    def __init__(self, maze: list[list[str]]) -> None:
        self._maze = maze

    def a_star(self, r: int, c: int, dir: tuple[int, int]):
        queue = [(0, r, c, dir)]
        visited = set()

        while queue:
            steps, r, c, dir = heapq.heappop(queue)

            if self._maze[r][c] == "E":
                return steps

            new_r, new_c = r + dir[0], c + dir[1]
            if self._is_valid(new_r, new_c, dir, visited):
                visited.add((new_r, new_c, dir))
                heapq.heappush(queue, (steps + 1, new_r, new_c, dir))

            turn_directions = [(dir[1], dir[0]), (-dir[1], -dir[0])]
            for turn_dir in turn_directions:
                new_r, new_c = r + turn_dir[0], c + turn_dir[1]
                if self._is_valid(new_r, new_c, dir, visited):
                    visited.add((new_r, new_c, turn_dir))
                    heapq.heappush(queue, (steps + 1001, new_r, new_c, turn_dir))

    def _is_valid(self, r: int, c: int, dir: tuple[int, int], visited_set: set) -> bool:
        return (
            (0 <= r < len(self._maze) and 0 <= c < len(self._maze[0]))
            and self._maze[r][c] in [".", "E"]
            and (r, c, dir) not in visited_set
        )


def _read_input(file_path: str):
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return [list(row) for row in raw_data]


def pprint(maze: list[list[str]]):
    for row in maze:
        print("".join(row))


if __name__ == "__main__":
    main()
