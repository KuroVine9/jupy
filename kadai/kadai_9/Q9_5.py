"""
Q9.5 Answer.
"""
import re

if __name__ == '__main__':
    korea_p = re.compile(r"(KOREA|Korea|korea)")
    s = input("s = ")
    print(f"Korea의 출현 횟수 : {len(korea_p.findall(s))}")
