from typing import Literal


def read_input(file_path) -> list[tuple]:
    with open(file_path, "r") as file:
        raw_data = file.read().split("\n")

    data = []
    for line in raw_data:
        if not line:
            continue

        data.append(tuple(map(int, line.split(" "))))

    return data


def _is_report_safe(report: tuple) -> Literal[0, 1]:
    trend = 0 if report[0] > report[1] else 1  # 0 for decreasing, 1 for increasing

    report_is_safe = True
    for index in range(1, len(report)):
        level, prev_level = report[index], report[index - 1]
        report_is_safe &= level > prev_level if trend else level < prev_level
        report_is_safe &= 1 <= abs(level - prev_level) <= 3

    return 1 if report_is_safe else 0


def main():
    data = read_input("./solutions/day-2/input.txt")

    number_of_safe_reports = sum(map(_is_report_safe, data))
    print(number_of_safe_reports)


if __name__ == "__main__":
    main()
