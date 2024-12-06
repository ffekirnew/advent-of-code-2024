from collections import defaultdict
from functools import reduce


def read_input(
    file_path: str,
) -> tuple[list[list[int]], list[list[int]]]:
    with open(file_path, "r") as file:
        raw_data = file.read().splitlines()

    ordering_rules, updates = [], []

    destination_list, separator = ordering_rules, "|"
    for line in raw_data:
        if not line:
            destination_list, separator = updates, ","
            continue

        destination_list.append(list(map(int, line.split(separator))))

    return ordering_rules, updates


class Printer:
    def __init__(self, ordering_rules: list[list[int]]) -> None:
        self._ordering_rules = ordering_rules

    def is_update_in_correct_order(
        self,
        update: list[int],
    ) -> bool:
        graph, inbounds = self._build_page_ordering_graph(self._ordering_rules)

        check_previous = []
        for page_number in update:
            for page in check_previous:
                if page in graph[page_number]:
                    return False

            if inbounds[page_number]:
                check_previous.append(page_number)
                continue

            for page in [page for page in graph[page_number]]:
                inbounds[page] -= 1
                graph[page_number].remove(page)

        return True

    def order_and_get_middle_element(self, update: list[int]) -> list[int]:
        graph, inbounds = self._build_page_ordering_graph(self._ordering_rules)

        check_previous = []
        for curr_index, curr_page_number in enumerate(update):
            for index in check_previous:
                check_page = update[index]
                if check_page in graph[curr_page_number]:
                    update[curr_index], update[index] = (
                        update[index],
                        update[curr_index],
                    )
                    inbounds[check_page] -= 1
                    graph[curr_page_number].remove(check_page)

            if inbounds[curr_page_number]:
                check_previous.append(curr_index)
                continue

            for check_page in [page for page in graph[curr_page_number]]:
                inbounds[check_page] -= 1
                graph[curr_page_number].remove(check_page)

        return update

    def _build_page_ordering_graph(
        self,
        ordering_rules: list[list[int]],
    ) -> tuple[dict[int, set[int]], dict[int, int]]:
        graph = defaultdict(set)
        inbounds = defaultdict(int)

        for first, second in ordering_rules:
            graph[first].add(second)
            inbounds[second] += 1

        return graph, inbounds


def main():
    ordering_rules, updates = read_input("./solutions/day-5/input.txt")
    printer = Printer(ordering_rules)

    total = 0
    for update in updates:
        if printer.is_update_in_correct_order(update.copy()):
            continue

        while not printer.is_update_in_correct_order(update):
            update = printer.order_and_get_middle_element(update.copy())

        total += update[len(update) // 2]

    print(total)


if __name__ == "__main__":
    main()
