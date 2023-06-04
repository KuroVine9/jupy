"""
Q10.5 Answer.
"""
import numpy as np

if __name__ == '__main__':
    a = np.arange(0, 32).reshape(4, 4, 2)
    a = a.flatten()
    print(f"10번째 원소 : {a[9]}")
    print(f"20번째 원소 : {a[19]}")
