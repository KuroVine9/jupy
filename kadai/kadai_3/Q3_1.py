"""
Q3.1 Answer.
"""

from typing import Callable


def square_table(func: Callable[[int, int], None]):
    def printHeader(start: int, end: int):
        print("a\t\tn\t\ta ** n")
        func(start, end)

    return printHeader


@square_table
def printValue(start: int, end: int):
    for i in range(start, end):
        print(f"{i}\t\t2\t\t{i ** 2}")


if __name__ == '__main__':
    printValue(2, 7)
