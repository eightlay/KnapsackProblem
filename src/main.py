import argparse
from datetime import datetime
import os
import json
import brutal
import greedy
import dynamic
import branchbound as bb


def main():
    # File to read data from
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', required=True,
                    type=str, help='name of file in data folder')
    args = vars(ap.parse_args())

    file_name = args['file']

    # Path
    path = os.getcwd()
    path = os.path.abspath(path)
    path = os.path.dirname(path)
    path = os.path.join(path, 'data', file_name)

    # Import data
    with open(path) as f:
        I, w, v, K = json.load(f).values()

    # Usage results
    results = {}

    # Brutal search
    # NOTE: 50 items takes 1,285,273,866 centuries to check each configuration,
    # if each check takes 1 millisecond.
    # So don't recommended if you're mortal.

    # timer = datetime.now()
    # result = brutal.brutal(I, w, v, K)
    # timer = str(datetime.now() - timer)

    # results['brutal'] = (result[2], timer)
    # print("brutal DONE")

    # Greedy algorithms
    for name in dir(greedy):
        if name[:1] != '_':
            func = getattr(greedy, name)

            timer = datetime.now()
            result = func(I, w, v, K)
            timer = str(datetime.now() - timer)

            results[name] = (result[2], timer)
            print(f"{name} DONE")

    # Dynamic programming
    for name in dir(dynamic):
        if name[:1] != '_':
            func = getattr(dynamic, name)

            timer = datetime.now()
            result = func(I, w, v, K)
            timer = str(datetime.now() - timer)

            results[name] = (result[2], timer)
            print(f"{name} DONE")

    # Branch and Bound algorithms
    for name in dir(bb):
        if name[:1] != '_':
            func = getattr(bb, name)
            
            for relaxation_func in ['simple']:
                timer = datetime.now()
                result = func(I, w, v, K, relaxation_func)
                timer = str(datetime.now() - timer)

                results[name + '-' + relaxation_func] = (result[2], timer)
                print(f"{name} with {relaxation_func} relaxation DONE")

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
