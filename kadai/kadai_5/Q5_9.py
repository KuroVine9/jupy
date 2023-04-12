"""
Q5.9 Answer.
"""

if __name__ == '__main__':
    max_num: int = -99
    min_num: int = -99
    count: int = 0

    while (user := int(input("정수를 입력하시오 : "))) != -99:
        if max_num == min_num == -99:
            max_num, min_num = user, user
        if user < 0:
            continue
        max_num, min_num = max(max_num, user), min(min_num, user)
        count += 1

    print(f"{count}개의 유효한 정수 중 가장 큰 정수는 {max_num}이고, 가장 작은 정수는 {min_num}입니다.")
