"""
Q5.1 Answer.
"""


def foo511():
    print("1에서 100까지의 수 중에서 홀수는 : ")
    print(" ".join([str(i) for i in range(1, 101) if i % 2 == 1]))


def foo512():
    print("1에서 100까지의 수 중에서 홀수는 : ")
    i: int = 1
    while i <= 100:
        if i % 2 == 1: print(i, end=" ")
        i += 1


def foo513():
    print("1에서 100까지의 수 중에서 짝수는 : ")
    print(" ".join([str(i) for i in range(1, 101) if i % 2 == 0]))


if __name__ == '__main__':
    foo513()
