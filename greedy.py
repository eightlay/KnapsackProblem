def _greedy(I: list, w: list, v: list, K: int, greedness: str) -> tuple:
    """
        Solve knapsack problem with asked greedness.

        Parameters:
        -----------
        - I : items
        - w : items' weights
        - v : items' value
        - K : knapsack size
        - greedness : parameter to be greedy
            - w: weight
            - v: value
            - vpw: value per weight unit

        Result:
        -------
        result : (taken items, total weight, total value)
    """

    if greedness in ['w', 'v', 'vpw']:
        items = None

        if greedness == 'vpw':
            vpw = [v[i] / w[i] for i in I]
            items = zip(I, w, v, vpw)
        else:
            items = zip(I, w, v)

        key = {'w': 1, 'v': 2, 'vpw': 3}.get(greedness, 0)
        reverse = {'w': False, 'v': True, 'vpw': True}.get(greedness, False)
        items = sorted(items, key=lambda x: x[key], reverse=reverse)

        taken_items = []
        total_weight = 0
        total_value = 0

        for item in items:
            if total_weight >= K:
                break
            if total_weight + item[1] > K:
                continue
            taken_items.append(item[0])
            total_weight += item[1]
            total_value += item[2]

        return taken_items, total_weight, total_value
    else:
        raise ValueError("'greedness' parameter must be 'w', 'v', or 'vpw'")


def greedy_weight(I: list, w: list, v: list, K: int) -> tuple:
    """
        Solve knapsack problem with weight greedness.
        Takes most lightweighted first.

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
    return _greedy(I, w, v, K, 'w')


def greedy_value(I: list, w: list, v: list, K: int) -> tuple:
    """
        Solve knapsack problem with value greedness.
        Takes most valuable first.

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
    return _greedy(I, w, v, K, 'v')


def greedy_value_per_weight_unit(I: list, w: list, v: list, K: int) -> tuple:
    """
        Solve knapsack problem with value per weight unit greedness.
        Takes most beneficial first.

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
    return _greedy(I, w, v, K, 'vpw')
