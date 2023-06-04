"""
Q9.1 Answer.
"""
import re

if __name__ == '__main__':
    name: str = ""
    pattern = re.compile(r"[A-Za-z]+ ([A-Za-z]+) [A-Za-z]")
    while not pattern.match(name):
        name = input("이름을 입력하시오 : ")
    print(f"중간 이름은 : {pattern.search(name).group(1)}")
