def read_input(file_path) -> list[tuple]:
    with open(file_path, "r") as file:
        raw_data = file.read().split("\n")

    data = []
    for line in raw_data:
        if not line:
            continue

        data.append(tuple(map(int, line.split(" "))))
        print(line, data[-1])

    return data


def main():
    data = read_input("./solutions/day-2/input.txt")

    # 1 2 3 4 5
    number_of_safe_reports = 0
    for report in data:
        trend = 0 if report[0] > report[1] else 1  # 0 for decreasing, 1 for increasing

        report_is_safe = True
        for index in range(1, len(report)):
            level, prev_level = report[index], report[index - 1]
            report_is_safe &= level > prev_level if trend else level < prev_level
            report_is_safe &= 1 <= abs(level - prev_level) <= 3

        # print(report, "SAFE" if report_is_safe else "UNSAFE")
        number_of_safe_reports += 1 if report_is_safe else 0

    print(number_of_safe_reports)


if __name__ == "__main__":
    main()
