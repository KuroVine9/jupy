"""
Q10.3 Answer.
"""
import numpy as np

if __name__ == '__main__':
    a = np.random.rand(3, 3, 3)
    print(a)

    print(f"a의 원소들 중 최댓값 : {a.max()}")

    print(f"a의 원소들 중 최댓값의 위치 : {a.argmax()}")
