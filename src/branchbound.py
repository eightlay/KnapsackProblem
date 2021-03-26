# TODO: linear relaxation, best-first, limited discrepancy


class _Node:
    def __init__(self, n: int, item: int, items: list, weight: int, val: int) -> None:
        self.n = n
        self.weight = weight
        self.item = item
        self.items = items.copy()
        self.val = val
        self.rel_val = 0

    def last_item(self) -> bool:
        return self.n == self.item

    def next(self, w: list, v: list, K: int) -> list:
        next_item = self.item + 1

        child2 = _Node(self.n, next_item, self.items, self.weight, self.val)

        child1_weight = self.weight + w[self.item]

        if child1_weight <= K:
            child1 = _Node(self.n, next_item, self.items, child1_weight,
                           self.val + v[self.item])

            return [child1, child2]

        return [child2]

    def __str__(self) -> str:
        return f"-------------\nitem={self.item}\nval={self.val}\nweight={self.weight}\nrel_val={self.rel_val}\nitems={str(self.items)}\n-------------"


def _simple_relaxation(node: _Node, v: list) -> None:
    node.rel_val = node.val + sum(v[i] for i in range(node.item, node.n))


def _linear_relaxation(node: _Node, v: list) -> None:
    pass


def depthfirst(I: list, w: list, v: list, K: int, rel_func: str) -> tuple:
    """
        Solve knapsack problem with depth-first branch and bound.

        Parameters:
        -----------
        - I : items
        - w : items' weights
        - v : items' value
        - K : knapsack size
        - rel_func : relaxation function name ['simple', 'linear']

        Result:
        -------
        result : (taken items, total weight, total value)
    """
    if rel_func not in ['simple', 'linear']:
        raise ValueError('Not valid relaxation function')

    if rel_func == 'simple':
        rel_func = _simple_relaxation
    else:
        rel_func = _linear_relaxation

    n = len(I)

    nodes = []

    current = _Node(n, 0, [0 for _ in range(n)], 0, 0)
    rel_func(current, v)

    best = _Node(n, 0, [], 0, 0)

    while True:
        if current.rel_val > best.val:
            children = current.next(w, v, K)

            if len(children) == 2:
                # TODO: check if it's ok with linear relaxation
                children[0].rel_val = current.rel_val
                children[1].rel_val = current.rel_val - v[current.item]

                children[0].items[current.item] = 1

                current = children[0]

                if current.last_item():
                    best = current
                elif children[1].rel_val > best.val:
                    nodes.append(children[1])
            else:
                children[0].rel_val = current.rel_val - v[current.item]
                current = children[0]
                if children[0].rel_val > best.val and current.last_item():
                    best = current
        else:
            ind = -1
            val = 0

            for i in range(len(nodes)):
                if nodes[i].rel_val > val:
                    val = nodes[i].rel_val
                    ind = i

            if val <= best.val:
                break

            current = nodes.pop(ind)

    return (best.items, best.weight, best.val)
