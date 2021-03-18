from datetime import datetime
import dynamic
import greedy


def main():
    # Test data
    n = 7
    I = list(range(n))
    w = [2, 2, 2, 5, 5, 8, 3]
    v = [1, 1, 1, 10, 10, 13, 7]
    K = 10

    # Usage results
    results = {}

    # Greedy algorithms
    for name in dir(greedy):
        if name[:1] != '_':
            func = getattr(greedy, name)

            timer = datetime.now()
            result = func(I, w, v, K)
            timer = str(datetime.now() - timer)

            results[name] = (result[2], timer)

    # Dynamic programming
    timer = datetime.now()
    result = dynamic.dynamic(I, w, v, K)
    timer = str(datetime.now() - timer)

    results['dynamic'] = (result[2], timer)

    # Print results in decreasing order
    results = dict(
        sorted(
            results.items(),
            key=lambda item: item[1][0],
            reverse=True
        )
    )
    print(results)


if __name__ == '__main__':
    main()
