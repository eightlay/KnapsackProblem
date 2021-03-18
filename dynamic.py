from typing import List


def dynamic(I: list, w: list, v: list, K: int) -> tuple:
    """
        Solve knapsack problem with dynamic approach.

        Parameters:
        -----------
        - I : items
        - w : items' weights
        - v : items' value
        - K : knapsack size

        Result:
        -------
        result : (taken items, total weight, total value)
    """
    n = len(I)
    filled_table = _fill_table(n, I, w, v, K)
    backtraced = _backtrace(n, w, K, filled_table)

    total_weight = 0
    total_value = 0

    for item in backtraced:
        total_weight += w[item]
        total_value += v[item]

    return (backtraced, total_weight, total_value)


def _fill_table(n: int, I: list, w: list, v: list, K: int) -> List[List[int]]:
    """
        Fill table for dynamic algorithm.

        Parameters:
        -----------
        - n : number of items
        - I : items
        - w : items' weights
        - v : items' value
        - K : knapsack size

        Result:
        -------
        result : (taken items, total weight, total value)
    """
    rows = range(K + 1)

    filled_table = [[0 for _ in range(n + 1)] for _ in rows]

    for item in I:
        weight = w[item]
        value = v[item]

        for row in rows:
            if weight > row:
                filled_table[row][item] = filled_table[row][item - 1]
            else:
                if weight <= row:
                    filled_table[row][item] = max(
                        filled_table[row][item - 1],
                        filled_table[row - weight][item - 1] + value
                    )
                else:
                    filled_table[row][item] = max(
                        value,
                        filled_table[row][item - 1]
                    )

    return filled_table


def _backtrace(n: int, w: list, K: int, filled_table: List[List[int]]) -> tuple:
    """
        Select items for knapsack from filled dynamic algorithm table.

        Parameters:
        -----------
        - filled_table : filled dynamic algorithm table

        Result:
        -------
        backtraced : selected items
    """
    backtraced = []

    row = K

    items = range(n - 1, -1, -1)

    for item in items:
        if filled_table[row][item] != filled_table[row][item - 1]:
            backtraced.append(item)
            row -= w[item]

    return backtraced
