"""
Q5.5 Answer.
"""

from typing import *

if __name__ == '__main__':
    GOAL: Final[int] = 30
    now: int = 0
    day: int = 0

    while now <= GOAL:
        now += 7
        day += 1
        print("day: {0:>3} 달팽이의 위치: {1:>3} 미터".format(day, now))
        if now >= GOAL:
            print("축하합니다. 우물을 탈출하였습니다. ")
            print(f"우물을 탈출하는 데 걸린 날은 {day}일 입니다.")
            break
        now -= 5
