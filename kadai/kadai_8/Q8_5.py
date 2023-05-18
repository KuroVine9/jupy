"""
Q8.5 Answer.
"""

if __name__ == '__main__':
    dictionary: dict[str, str] = {}
    print("사전 프로그램 시작... 종료는 q를 입력")

    while (command := input("$ ")) != "q":
        match command[0]:
            case "<":
                if len(command) <= 4:
                    print("Input Error! Check your Syntax")
                else:
                    op = command[1:].strip().split(":")
                    dictionary[op[0]] = op[1]

            case ">":
                op = command[1:].strip()
                if op in dictionary:
                    print(dictionary[op])
                else:
                    print(f"\"{op}\" not found in db")

            case "v":
                print("영어 사전에 있는 단어와 뜻을 출력합니다. ")
                for k, v in dictionary.items():
                    print(f"{k} : {v}")

            case _:
                print('입력 오류가 발생했습니다.')

    print("사전 프로그램을 종료합니다.")

