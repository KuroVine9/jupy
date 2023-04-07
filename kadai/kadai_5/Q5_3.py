"""
Q5.3 Answer.
"""

if __name__ == '__main__':
    menus = ["햄버거", "치킨", "피자"]
    print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
    for idx, menu in enumerate(menus, start=1):
        print(f"{idx}) {menu}")
    select = int(input(f"1에서 {len(menus)}까지의 메뉴를 선택하세요 : "))

    while not (1 <= select <= len(menus)):
        select = int(input("메뉴를 다시 입력하세요 : "))
    print(f"{menus[select - 1]}을 선택하였습니다. ")
