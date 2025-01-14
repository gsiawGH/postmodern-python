# Note: This is copied from https://github.com/bloomberg/memray/blob/main/docs/tutorials/exercise_1/fibonacci.py

import operator
from functools import reduce
from itertools import chain
from typing import List


def fibonacci(length: int) -> List[int]:
    # edge cases
    if length < 1:
        return []
    if length == 1:
        return [1]
    if length == 2:
        return [1, 1]

    output = [1, 1]

    for i in range(length - 2):
        output.append(output[i] + output[i + 1])

    return output


def generate_fibonacci_hash(length_1: int, length_2: int, length_3: int):
    # We could have used sum(...) here instead of reduce(operator.add, ...),
    # but we choose to use reduce since it yields a more descriptive example
    # of the generated flamegraph for this specific example
    return (
        reduce(
            operator.add,
            chain(fibonacci(length_1), fibonacci(length_2), fibonacci(length_3)),
            0,
        )
        % 10000
    )


if __name__ == "__main__":
    # DO NOT CHANGE
    LENGTH_OF_SEQUENCE_1 = 33333
    LENGTH_OF_SEQUENCE_2 = 30000
    LENGTH_OF_SEQUENCE_3 = 34567
    # DO NOT CHANGE
    x = generate_fibonacci_hash(LENGTH_OF_SEQUENCE_1, LENGTH_OF_SEQUENCE_2, LENGTH_OF_SEQUENCE_3)
    print(x)


def main() -> None:
    print("Do CLI stuff")
