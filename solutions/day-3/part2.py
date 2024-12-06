NEXT_EXPECTED: dict[str, str] = {
    "m": "u",
    "u": "l",
    "l": "(",
    "(": "first_number",
    "first_number": ",",
}

NEXT_EXPECTED_FOR_DO: dict[str, str] = {"d": "o", "o": "(", "(": ")", ")": "Done"}
NEXT_EXPECTED_FOR_DONT: dict[str, str] = {
    "d": "o",
    "o": "n",
    "n": "'",
    "'": "t",
    "t": "(",
    "(": ")",
    ")": "Done",
}


def read_input(file_path) -> str:
    with open(file_path, "r") as file:
        raw_data = file.read()

    return raw_data


class Parser:
    def __init__(self, input: str) -> None:
        self._input = input
        self._curr_position = 0

    def parse_do(self, start_position: int) -> bool:
        return self._parse_do_or_dont(start_position, NEXT_EXPECTED_FOR_DO)

    def parse_dont(self, start_position: int) -> bool:
        return self._parse_do_or_dont(start_position, NEXT_EXPECTED_FOR_DONT)

    def _parse_do_or_dont(
        self,
        start_position: int,
        next_expected_dict: dict[str, str],
    ) -> bool:
        self._curr_position = start_position
        curr = self._input[self._curr_position]

        while len(next_expected_dict[curr]) == 1:
            if next := self.read_char(next_expected_dict[curr]):
                curr = next
            else:
                return False

        return True

    def parse(
        self,
        start_position: int,
    ) -> int | None:
        self._curr_position = start_position
        curr = self._input[self._curr_position]

        while len(NEXT_EXPECTED[curr]) == 1:
            if next := self.read_char(NEXT_EXPECTED[curr]):
                curr = next
            else:
                break

        num1, num2 = 0, 0
        if NEXT_EXPECTED[curr] == "first_number":
            if num1 := self.read_number(","):
                if num2 := self.read_number(")"):
                    return num1 * num2

        return

    def read_char(self, expected: str) -> str | None:
        self._curr_position += 1
        if self._input[self._curr_position] == expected:
            return expected

        return None

    def read_number(self, end_character: str) -> int | None:
        self._curr_position += 1
        start = self._curr_position
        while self._input[self._curr_position] != end_character:
            self._curr_position += 1

        number = self._input[start : self._curr_position]
        if number.isdigit():
            return int(number)
        return


def main():
    data = read_input("./solutions/day-3/input.txt")
    parser = Parser(data)

    total = 0
    enabled = True
    for i in range(len(data)):
        if data[i] == "d":
            if parser.parse_do(i):
                enabled = True
            if parser.parse_dont(i):
                enabled = False

        if data[i] == "m":
            result = parser.parse(i)

            if enabled:
                total += result if result else 0

    print(total)


if __name__ == "__main__":
    main()
