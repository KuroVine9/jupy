"""
Q6.7 Answer.
"""
import functools


def factorial(n: int) -> int:
    return functools.reduce(
        lambda acc, now: acc * now,
        [i for i in range(1, n + 1)]
    )


if __name__ == '__main__':
    for i in (5, 7, 10):
        print(f"factorial({i}) : {factorial(i)}")
