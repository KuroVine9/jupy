"""
Q4.7 Answer.
"""

import random as r

if __name__ == '__main__':
    nums = [r.randint(1, 100) for i in range(2)]
    ans = int(input(f"{nums[0]} + {nums[1]} = "))
    if ans == sum(nums):
        print("정답")
    else:
        print(f"정답은 {sum(nums)} 입니다. ")
