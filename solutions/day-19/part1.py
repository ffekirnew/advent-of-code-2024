from functools import cache, reduce
from sys import argv, setrecursionlimit

setrecursionlimit(10**6)


def main():
    args = argv[1:]
    test_file_name = "test_input" if args and args[0] == "test" else "input"
    available, new = _read_input(f"./solutions/day-19/{test_file_name}.txt")

    design = Design(available)

    print(
        reduce(
            lambda x, y: x + y,
            [design.build(new_design) for new_design in new],
        )
    )


class Design:
    def __init__(self, available_patterns: list[str]) -> None:
        self._available_patterns = available_patterns

    def build(self, new_pattern: str) -> bool:
        @cache
        def helper(start: int = 0, curr: int = 0):
            if curr == len(new_pattern):
                return start == curr

            possible = helper(start, curr + 1)
            for pattern in self._available_patterns:
                if self._check(pattern, new_pattern, start, curr):
                    possible |= helper(curr + 1, curr + 1)
                    break

            return possible

        return helper()

    def _check(self, pattern: str, new_pattern: str, start: int, curr: int):
        if len(pattern) - 1 != curr - start:
            return False

        i, j = 0, start
        while i < len(pattern):
            if pattern[i] != new_pattern[j]:
                return False

            i += 1
            j += 1

        return True


def _read_input(file_path: str):
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    available = []
    new_designs = []

    is_available = True

    for line in raw_data:
        if not line:
            is_available = False
            continue

        if is_available:
            available.extend(line.split(", "))
        else:
            new_designs.append(line)

    return available, new_designs


def pprint(grid: list[list[str]]):
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    main()
