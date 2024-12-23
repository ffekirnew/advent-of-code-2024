import sys
from collections import namedtuple

Button = namedtuple("Button", ["dx", "dy"])
Prize = namedtuple("Prize", ["x", "y"])
Equation = namedtuple("Equation", ["a", "b", "result"])


class Machine:
    def __init__(self, button_a: Button, button_b: Button, prize: Prize) -> None:
        self._eq1 = Equation(button_a.dx, button_b.dx, prize.x)
        self._eq2 = Equation(button_a.dy, button_b.dy, prize.y)

    def solve(self) -> tuple[int, int] | None:
        a = (self._eq1.b * self._eq2.result - self._eq2.b * self._eq1.result) / (
            self._eq2.a * self._eq1.b - self._eq2.b * self._eq1.a
        )
        b = (self._eq1.result - self._eq1.a * a) / self._eq1.b

        if a % 1 == 0 and b % 1 == 0:
            return int(a), int(b)

        return None


def main():
    args = sys.argv[1:]
    test_file_name = "test_input" if args and args[0] == "test" else "input"
    input_data = _read_input(f"./solutions/day-13/{test_file_name}.txt")

    total = 0
    for machine in input_data:
        if result := machine.solve():
            total += result[0] * 3 + result[1] * 1

    print(total)


def _read_input(file_path: str) -> list[Machine]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    machines = []

    index = 0
    while index < len(raw_data):
        first_line = raw_data[index].split(" ")
        second_line = raw_data[index + 1].split(" ")
        third_line = raw_data[index + 2].split(" ")

        machines.append(
            Machine(
                button_a=Button(_get_num(first_line[2]), _get_num(first_line[3])),
                button_b=Button(_get_num(second_line[2]), _get_num(second_line[3])),
                prize=Prize(_get_num(third_line[1]), _get_num(third_line[2])),
            )
        )

        index += 4

    return machines


def _get_num(raw_data: str) -> int:
    return int("".join(filter(str.isdigit, raw_data)))


if __name__ == "__main__":
    main()
