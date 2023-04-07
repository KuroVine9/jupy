"""
Q4_3 Answer.
"""

if __name__ == '__main__':
    age = int(input("나이 입력 : "))

    if age >= 20:
        print("Adult")
    elif age >= 10:
        print("Youth")
    else:
        print("Kid")