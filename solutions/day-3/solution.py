def read_input(file_path) -> str:
    with open(file_path, "r") as file:
        raw_data = file.read()

    return raw_data


class Tokenizer: ...


def main():
    data = read_input("./solutions/day-3/input.txt")


if __name__ == "__main__":
    main()
