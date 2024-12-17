import math
import sys
from typing import Callable

sys.setrecursionlimit(10**6)


def main():
    args = sys.argv[1:]
    test_file_name = "test_input" if args and args[0] == "test" else "input"
    registers, program = _read_input(f"./solutions/day-17/{test_file_name}.txt")

    assembly = Assembly(registers, program)
    output = assembly.run()

    print(output)


class Assembly:
    def __init__(self, registers: list[int], program: list[int]):
        self._registers = registers
        self._program = program
        self._ip = 0  # instruction pointer

        self._operations: dict[int, Callable[[int], int | None]] = {
            0: self._adv,
            1: self._bxl,
            2: self._bst,
            3: self._jnz,
            4: self._bxc,
            5: self._out,
            6: self._bdv,
            7: self._cdv,
        }

    def run(self) -> str:
        output = []
        while self._ip < len(self._program) - 1:
            op, operand = self._program[self._ip], self._program[self._ip + 1]

            value = self._operations[op](operand)
            if op == 5:
                output.append(value)
            if op == 3 and value:
                continue

            self._ip += 2

        return ",".join(map(str, output))

    def _adv(self, operand: int) -> None:
        self._registers[0] = math.floor(
            self._registers[0] / 2 ** self._get_combo_operand(operand)
        )

    def _bxl(self, operand: int) -> None:
        self._registers[1] = self._registers[1] ^ operand

    def _bst(self, operand: int) -> None:
        self._registers[1] = self._get_combo_operand(operand) % 8

    def _jnz(self, operand: int) -> int:
        if self._registers[0] == 0:
            return 0

        self._ip = operand
        return 1

    def _bxc(self, operand: int) -> None:
        self._registers[1] = self._registers[1] ^ self._registers[2]

    def _out(self, operand: int) -> int:
        return self._get_combo_operand(operand) % 8

    def _bdv(self, operand: int) -> None:
        self._registers[1] = math.floor(
            self._registers[0] / 2 ** self._get_combo_operand(operand)
        )

    def _cdv(self, operand: int) -> None:
        self._registers[2] = math.floor(
            self._registers[0] / 2 ** self._get_combo_operand(operand)
        )

    def _get_combo_operand(self, operand: int) -> int:
        if operand <= 3:
            return operand

        return self._registers[operand - 4]


def _read_input(file_path: str):
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    registers = []
    program = []
    for i, line in enumerate(raw_data):
        if i < 3:
            number = int(line.split(": ")[1])
            registers.append(number)
        if i > 3:
            program.extend(list(map(int, line.split(": ")[1].split(","))))

    return registers, program


def pprint(maze: list[list[str]]):
    for row in maze:
        print("".join(row))


if __name__ == "__main__":
    main()
