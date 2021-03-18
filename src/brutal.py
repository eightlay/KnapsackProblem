def brutal(I: list, w: list, v: list, K: int) -> tuple:
    """
        Solve knapsack problem with brutal search.

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

    best = [[], 0, 0]

    for i in range(1, 1 << n):
        subset = [I[j] for j in range(n) if i & (1 << j)]

        total_weight = sum(w[item] for item in subset)

        if total_weight <= K:
            total_value = sum(v[item] for item in subset)

            if total_value > best[2]:
                best[0] = subset
                best[1] = total_weight
                best[2] = total_value

    return best
