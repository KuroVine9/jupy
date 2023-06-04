"""
Q9.7 Answer.
"""
import re
import string

if __name__ == '__main__':
    src_str = string.ascii_uppercase + string.ascii_lowercase
    to_chiper = re.compile(r"[A-Za-z]")
    plain_text = input("문장을 입력하시오 : ")
    to_move: int = int(input("이동시킬 칸 수를 입력하시오 : "))
    to_move %= len(src_str)
    new_str: str = ""
    for ch in plain_text:
        if to_chiper.match(ch):
            new_str += src_str[(src_str.find(ch) + to_move) % len(src_str)]
        else:
            new_str += ch

    print(f"암호화된 문장 : {new_str}")
