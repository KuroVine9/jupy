"""
Q4.5 Answer.
"""

import random as r
from functools import reduce

if __name__ == '__main__':
    lott = [r.randint(0, 9) for i in range(3)]
    userNum = list(map(int, input("세 복권번호 입력 : ").split()))

    match reduce(lambda acc, prev: acc + int(prev in lott), userNum, 0):
        case 0:
            print("다음 기회에..")
        case 1:
            print("상금 1만원")
        case 2:
            print("상금 1천만원")
        case 3:
            print("상금 1억원")
