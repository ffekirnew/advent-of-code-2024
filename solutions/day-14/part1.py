import sys
from collections import namedtuple

Robot = namedtuple("Robot", ["position", "velocity"])


TALL, WIDE = 103, 101
TIME = 100


def main():
    args = sys.argv[1:]
    test_file_name = "test_input" if args and args[0] == "test" else "input"
    input_data = _read_input(f"./solutions/day-14/{test_file_name}.txt")

    movements = RobotMovements(tile_size=(TALL, WIDE), time=TIME)

    movements._draw(input_data)
    final_locations = [movements.solve(robot) for robot in input_data]
    movements._draw(final_locations)

    mid_row, mid_col = TALL // 2, WIDE // 2
    quadrants = [0, 0, 0, 0]
    for robot in final_locations:
        if robot.position[0] < mid_row and robot.position[1] < mid_col:
            quadrants[0] += 1
        elif robot.position[0] < mid_row and robot.position[1] > mid_col:
            quadrants[1] += 1
        elif robot.position[0] > mid_row and robot.position[1] < mid_col:
            quadrants[2] += 1
        elif robot.position[0] > mid_row and robot.position[1] > mid_col:
            quadrants[3] += 1

    print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])


class RobotMovements:
    def __init__(self, tile_size: tuple[int, int], time: int) -> None:
        self._rows, self._cols = tile_size
        self._time = time

    def solve(self, robot: Robot):
        for _ in range(self._time):
            robot = self.move(robot)

        return robot

    def move(self, robot: Robot):
        position = robot.position
        velocity = robot.velocity

        new_position = (
            (position[0] + velocity[0]) % self._rows,
            (position[1] + velocity[1]) % self._cols,
        )
        robot = Robot(position=new_position, velocity=velocity)

        return robot

    def _draw(self, robots: list[Robot]):
        print("Draw")
        draw = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for robot in robots:
            draw[robot.position[0]][robot.position[1]] += 1

        for r, row in enumerate(draw):
            for c, cell in enumerate(row):
                if cell == 0:
                    draw[r][c] = "."
                else:
                    draw[r][c] = str(cell)

        self._print(draw)

    def _check_if_robots_form_a_tree(self, robots: list[Robot]):
        for row in range(self._rows):
            expected = row + 1
            start = self._cols // 2 - expected // 2
            for col in range(self._cols):
                if col >= start:
                    expected -= 1

            if expected != 0:
                return False

        return True

    def _print(self, draw):
        for row in draw:
            print("".join(row))


def _read_input(file_path: str):
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    robots = []
    for line in raw_data:
        position, velocity = line.split(" ")
        position = position.split("=")[1]
        velocity = velocity.split("=")[1]
        robots.append(
            Robot(
                position=(
                    int(position.split(",")[1]),
                    int(position.split(",")[0]),
                ),
                velocity=(
                    int(velocity.split(",")[1]),
                    int(velocity.split(",")[0]),
                ),
            )
        )

    return robots


if __name__ == "__main__":
    main()
