"""
Q6.5 Answer.
"""


def cel2fah(cel: float) -> float:
    return cel * 1.8 + 32


if __name__ == '__main__':
    print("\n".join([f"섭씨 : {i}\t화씨 : {cel2fah(i)}" for i in range(0, 60, 10)]))
