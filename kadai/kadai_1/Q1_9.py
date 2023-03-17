"""
Q1.9 Answer.
"""

if __name__ == '__main__':
    result = [
        sum(range(1, 11)),
        2 * 3.14 * 5,
        20 * 4,
        20 ** 2,
        2 * (10 + 30),
        10 * 30
    ]

    for idx, val in enumerate(result, start=1):
        print(f'({idx}) {val}')
