"""
Q8.1 Answer.
"""

if __name__ == '__main__':
    fruit_name = ("사과", "배", "수박", "귤", "포도")
    fruit_input = tuple(map(int, input("사과, 배, 수박, 귤, 포도 가격을 공백 구분 입력 : ").split()))
    fruits_price = dict(((fruit_name[i], fruit_input[i]) for i in range(len(fruit_name))))

    print("==========오늘의 과일 가격==========")
    for key in fruits_price.keys():
        print(f"{key:7s}:  {fruits_price[key]:} 원")
