"""
Q9.3 Answer.
"""
import re

if __name__ == '__main__':
    input_string = input("문자열을 입력하시오 : ")
    capital_pattern = re.compile(r"[A-Z]")
    lowercase_pattern = re.compile(r"[a-z]")
    number_pattern = re.compile(r"[0-9]")
    special_pattern = re.compile(r"[^\w\s]")

    print("대문자, 소문자, 숫자, 특수문자의 개수")
    print(f"대문자 = {len(capital_pattern.findall(input_string))}")
    print(f"소문자 = {len(lowercase_pattern.findall(input_string))}")
    print(f"숫자 = {len(number_pattern.findall(input_string))}")
    print(f"특수문자 = {len(special_pattern.findall(input_string))}")
