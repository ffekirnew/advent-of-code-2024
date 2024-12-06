def read_input(file_path) -> list[list[int]]:
    with open(file_path, "r") as file:
        raw_data = file.read().split("\n")

    data = []
    for line in raw_data:
        if not line:
            continue

        data.append(list(map(int, line.split(" "))))

    return data


def check_report(report: list, trend: int, index: int = 0, removed: int = 0) -> bool:
    if index == len(report):
        return True

    level, prev_level = report[index], report[index - 1]

    level_is_safe = level > prev_level if trend else level < prev_level
    level_is_safe &= 1 <= abs(level - prev_level) <= 3

    report_is_safe = False
    if index == 0 or level_is_safe:
        report_is_safe = check_report(report, trend, index + 1, removed)

    report_is_safe_after_removal = False
    if not removed:
        report_is_safe_after_removal = check_report(
            report[:index] + report[index + 1 :], trend, index, removed + 1
        )

    return report_is_safe or report_is_safe_after_removal


def main():
    data = read_input("./solutions/day-2/input.txt")

    total = 0
    for report in data:
        report_is_safe = check_report(report, 1) or check_report(report, 0)

        print(report, "safe" if report_is_safe else "unsafe")

        total += report_is_safe

    print(total)


if __name__ == "__main__":
    main()
