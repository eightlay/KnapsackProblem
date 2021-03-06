import sys as _sys


def dynamic_2rows_table(I: list, w: list, v: list, K: int) -> tuple:
    """
        Solve knapsack problem with dynamic programming.
        Memory cheaper and a little faster approach.
        2 rows table based.

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

    # TODO: add backtracking ?
    taken_items = []

    filled_table = [[0 for _ in range(K + 1)] for _ in range(2)]

    for item in range(1, n + 1):
        filled_table[0], filled_table[1] = filled_table[1], filled_table[0]

        for weight in range(K + 1):
            if w[item - 1] <= weight:
                taken = v[item - 1] + filled_table[0][weight - w[item - 1]]
                nottaken = filled_table[0][weight]

                if taken > nottaken:
                    filled_table[1][weight] = taken
                else:
                    filled_table[1][weight] = nottaken
            else:
                filled_table[1][weight] = filled_table[0][weight]

    total_weight = 0

    for item in taken_items:
        total_weight += w[item]

    return (taken_items, total_weight, filled_table[1][K])


def dynamic_recursion(I: list, w: list, v: list, K: int) -> tuple:
    """
        Solve knapsack problem with dynamic programming.
        Memory cheaper approach.
        Recursion with memoization.

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

    # Only available if size is less then current system recusion depth limit
    if n >= _sys.getrecursionlimit():
        return ([], 0, 0)

    memory = {}

    def _dynamic_recursion_sub(k: int, j: int) -> tuple:
        """
            Recurrent function.
        """
        if (k, j) in memory:
            return memory[k, j]
        if j == 0 or k == 0:
            memory[k, j] = 0
        elif w[j - 1] <= k:
            memory[k, j] = max(
                _dynamic_recursion_sub(k, j - 1),
                v[j - 1] + _dynamic_recursion_sub(k - w[j - 1], j - 1)
            )
        else:
            memory[k, j] = _dynamic_recursion_sub(k, j - 1)
        return memory[k, j]

    _dynamic_recursion_sub(K, n)

    items = range(n, 0, -1)
    k = K

    taken_items = []

    for item in items:
        if memory[k, item] != memory[k, item - 1]:
            taken_items.append(item - 1)
            k -= w[item - 1]

    total_weight = 0

    for item in taken_items:
        total_weight += w[item]

    taken_items = [1 if i in taken_items else 0 for i in I]

    return (taken_items, total_weight, memory[K, n])


def dynamic_table(I: list, w: list, v: list, K: int) -> tuple:
    """
        Solve knapsack problem with dynamic programming.
        Memory expensive approach.
        Fill table of size K+1 x |I|+1.

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

    backtraced = [1 if i in backtraced else 0 for i in I]

    return (backtraced, total_weight, total_value)


def _fill_table(n: int, I: list, w: list, v: list, K: int) -> list:
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
        filled_table : table of size K+1 x |I|+1
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
                filled_table[row][item] = max(
                    filled_table[row][item - 1],
                    filled_table[row - weight][item - 1] + value
                )

    return filled_table


def _backtrace(n: int, w: list, K: int, filled_table: list) -> tuple:
    """
        Select items for knapsack from filled dynamic algorithm table.

        Parameters:
        -----------
        - filled_table : filled dynamic algorithm table

        Result:
        -------
        backtraced : list of selected items
    """
    backtraced = []

    row = K

    items = range(n - 1, -1, -1)

    for item in items:
        if filled_table[row][item] != filled_table[row][item - 1]:
            backtraced.append(item)
            row -= w[item]

    return backtraced
