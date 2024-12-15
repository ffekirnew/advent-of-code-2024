import sys

TALL, WIDE = 103, 101
TIME = 100

MOVEMENTS = {
    "v": (1, 0),
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
}


def main():
    args = sys.argv[1:]
    test_file_name = "test_input" if args and args[0] == "test" else "input"
    input_data = _read_input(f"./solutions/day-15/{test_file_name}.txt")

    grid = Grid(input_data[0])

    for move in input_data[1]:
        x, y = get_robot_position(grid._grid)
        grid.move(x, y, move)

    total = 0
    for r, row in enumerate(grid._grid):
        for c, cell in enumerate(row):
            if cell == "O":
                total += 100 * r + c

    print(total)


def get_robot_position(grid):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "@":
                return r, c

    return 0, 0


def pprint(grid):
    for row in grid:
        print("".join(row))


class Grid:
    def __init__(self, grid):
        self._grid = grid

    def move(self, x, y, dir, robot=True):
        new_x, new_y = x + MOVEMENTS[dir][0], y + MOVEMENTS[dir][1]
        print(x, y, new_x, new_y, self._grid[new_x][new_y])

        if self._grid[new_x][new_y] == "#":
            return False

        if self._grid[new_x][new_y] == ".":
            self._grid[x][y] = "."
            self._grid[new_x][new_y] = "@" if robot else "O"
            return True

        if self.move(new_x, new_y, dir, False):
            return self.move(x, y, dir, robot)

        return False

    def _is_inbound(self, x, y):
        return 0 <= x < len(self._grid) and 0 <= y < len(self._grid[0])


def _read_input(file_path: str):
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    grid = []
    movements = []

    is_grid = True
    for line in raw_data:
        if not line:
            is_grid = False
            continue

        if is_grid:
            grid.append(list(line))
        else:
            movements.extend(list(line))

    return grid, movements


if __name__ == "__main__":
    main()
