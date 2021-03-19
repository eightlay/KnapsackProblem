import os
import json
import argparse
from random import randint


def generate_data(n: int) -> tuple:
    """
        Generate data of given size.

        Parameters:
        -----------
        n : size of problem

        Returns:
        --------
        result : (items, weights, values, knapsack size)
    """
    I = list(range(n))
    K = randint(10, 10 * n)
    return (
        # Items
        I,
        # Weights
        [randint(1, K) for _ in I],
        # Values
        [randint(1, K) for _ in I],
        # Knapsack size
        K
    )


def save_data(path: str, data_: tuple) -> None:
    """
        Save data.

        Parameters:
        -----------
        n : size of problem
    """
    data = dict(zip(('I', 'w', 'v', 'K'), data_))

    with open(path, 'w') as f:
        json.dump(data, f)


def generate_and_save(path: str, a: int, b: int, step: int) -> None:
    """
        Generate and save data.

        Parameters:
        -----------
        a : smallest size
        b : biggest size
        step : increment step
    """
    for size in range(a, b, step):
        if size != 0:
            data = generate_data(size)
            save_data(f'{path}\\size{size}.json', data)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-a', '--smallest', required=True,
                    type=int, help='smallest problem size')
    ap.add_argument('-b', '--biggest', required=True,
                    type=int, help='biggest problem size')
    ap.add_argument('-s', '--step', required=True,
                    type=int, help='step to increment form a to b')
    ap.add_argument('-p', '--path', required=False, default=None,
                    type=int, help='step to increment form a to b')
    args = vars(ap.parse_args())

    a, b, step, path = args.values()

    if path is None:
        path = os.getcwd()
        path = os.path.abspath(path)
        path = os.path.dirname(path)
        path = os.path.join(path, 'data')

    if not os.path.exists(path):
        os.mkdir(path)

    generate_and_save(path, a, b, step)


if __name__ == "__main__":
    main()
