"""
Q10.1 Answer.
"""
import numpy as np

if __name__ == '__main__':
    num_arr = np.arange(1, 21)
    print(num_arr)
    print(num_arr[::-1])
    print(f"num_arr 내의 모든 원소의 합 : {num_arr.sum()}")
    print(num_arr.reshape(5, 4))
