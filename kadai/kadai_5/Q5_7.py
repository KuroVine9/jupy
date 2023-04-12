"""
Q5.7 Answer.
"""

if __name__ == '__main__':
    arm = filter(
        lambda num: num == ((num % 10) ** 3 + ((num - (num % 10)) // 10 % 10)**3 + (num//100)**3),
        range(100, 1000)
    )
    print(f"세 자리 암스트롱 수 : {' '.join(map(str, arm))}")
