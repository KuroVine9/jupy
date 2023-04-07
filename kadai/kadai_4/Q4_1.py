"""
Q4.1 Answer.
"""

if __name__ == '__main__':
    char = input("알파벳 입력 : ")
    print(f"{char} 은(는) ", end="")
    if char in ("a", "i", "u", "e", "o"):
        print("모음입니다")
    else:
        print("자음입니다")
