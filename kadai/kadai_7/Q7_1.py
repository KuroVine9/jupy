"""
Q7.1 Answer.
"""

if __name__ == '__main__':
    num_list = [i for i in range(100, 900, 100)]
    high, low = 6, 3

    print(num_list[high])
    print(num_list[high] - 2)
    print(num_list[high] - low)
    print(num_list[-1])
    print(num_list[-low])
    print(num_list[2 * 3])
    print(num_list[2] * 3)
    print(num_list[5 % 4])
    print(len(num_list))
    print(min(num_list))
    print(max(num_list))
    print(num_list[:3])
    print(num_list[1:5])
    print(num_list[-1:-5:-1])
    print(num_list[-5:-1:1])
