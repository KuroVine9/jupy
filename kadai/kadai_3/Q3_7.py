"""
Q3.7 Answer.
"""

from typing import List

if __name__ == '__main__':
    num = int(input("세자리 정수 입력 : "))
    numToArr: List[int] = []

    while num:
        numToArr.insert(0, num % 10)
        num //= 10

    for idx, n in enumerate(numToArr):
        print(f"{100 // (10 ** idx)}의 자리 : {n}")
