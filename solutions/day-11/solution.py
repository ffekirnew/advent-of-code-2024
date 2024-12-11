import sys
from functools import cache


def main():
    args = sys.argv[1:]
    run_mode = "test_input" if args and args[0] == "test" else "input"
    blinks = int(args[1]) if args and len(args) > 1 else 75
    input_data = _read_input(f"./solutions/day-11/{run_mode}.txt")

    blinker = Blinker(input_data)
    print(blinker.solve(blinks))


def _read_input(file_path: str) -> list[int]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    return list(map(int, raw_data[0].split(" ")))


class Blinker:
    def __init__(self, data: list[int]) -> None:
        self._data = data

    def solve(self, blinks: int) -> int:
        total = 0
        for number in self._data:
            total += self._get_length_after_blink(number, blinks)

        return total

    def _get_length_after_blink(self, number: int, blinks: int) -> int:
        @cache
        def helper(number: int, blinks: int) -> int:
            if blinks == 0:
                return 1

            if number == 0:
                return helper(1, blinks - 1)

            num_str = str(number)
            mid, is_even = divmod(len(num_str), 2)
            if is_even == 0:
                return helper(int(num_str[:mid]), blinks - 1) + helper(
                    int(num_str[mid:]), blinks - 1
                )

            return helper(number * 2024, blinks - 1)

        return helper(number, blinks)


if __name__ == "__main__":
    main()
