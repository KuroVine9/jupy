"""
Q7.7 Answer.
"""
from copy import copy


def foo771(fruit_list: list[str]) -> None:
    """
    1번 문제
    :param fruit_list: 과일 이름이 담긴 리스트
    :return: stdout으로 연산 결과를 출력함
    """

    fruit_len: dict[int, list[int]] = {}

    for index, fruit in enumerate(fruit_list):
        if fruit_len.get(l := len(fruit)):
            fruit_len[l].append(index)
        else:
            fruit_len[l] = [index]

    max_len_fruits_index: list[int] = sorted(fruit_len.items())[-1][1]
    max_len_fruits = tuple(map(
        lambda index: fruit_list[index],
        max_len_fruits_index
    ))

    print(f"가장 길이가 긴 문자열 : {', '.join(max_len_fruits)}")
    for index in max_len_fruits_index:
        fruit_list.pop(index)
    print(fruit_list)


def foo772(fruit_list: list[str]) -> None:
    """
    2번 문제
    :param fruit_list: 과일 이름이 담긴 리스트
    :return: stdout으로 연산 결과를 출력함
    """

    print("\n".join(f"{fruit}\t: 문자열의 길이 {len(fruit)}" for fruit in fruit_list))


if __name__ == '__main__':
    fruit_list: list[str] = ["banana", "orange", "kiwi", "apple", "melon"]

    foo771(copy(fruit_list))
    foo772(copy(fruit_list))
