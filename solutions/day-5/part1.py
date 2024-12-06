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
        self._graph, self._inbounds = self._build_page_ordering_graph(ordering_rules)

    def check_update_order(
        self,
        update: list[int],
    ) -> bool:
        graph = self._graph.copy()
        inbounds = self._inbounds.copy()
        check_previous = []

        for curr_page_number in update:
            for page in check_previous:
                if page in graph[curr_page_number]:
                    return False

            if inbounds[curr_page_number]:
                check_previous.append(curr_page_number)
                continue

            for page in [page for page in graph[curr_page_number]]:
                inbounds[page] -= 1
                graph[page].remove(curr_page_number)

        return True

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
    ordering_rules, updates = read_input("./solutions/day-5/test_input.txt")
    printer = Printer(ordering_rules)

    total = reduce(
        lambda x, y: x + y,
        map(
            lambda arr: arr[len(arr) // 2],
            [update for update in updates if printer.check_update_order(update)],
        ),
    )
    print(total)


if __name__ == "__main__":
    main()
