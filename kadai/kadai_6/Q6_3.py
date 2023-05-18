"""
Q6.3 Answer.
"""
from typing import *


def max3(n1: int, n2: int, n3: int) -> int:
    return max(n1, n2, n3)


def min3(n1: int, n2: int, n3: int) -> int:
    return min(n1, n2, n3)


if __name__ == '__main__':
    nums: List[int]
    while len(nums := list(map(int, input("input 3 nums").split()))) != 3: pass
    print(f"가장 큰 수 : {max3(*nums)}")
    print(f"가장 작은 수 : {min3(*nums)}")
