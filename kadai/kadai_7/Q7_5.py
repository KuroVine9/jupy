"""
Q7.5 Answer.
"""
from typing import *


def seat_id_gen(alphabet: Iterable[Text], number: Iterable[Union[int, str]]) -> list[str]:
    return [f"{prefix}{suffix}" for prefix in alphabet for suffix in number]


if __name__ == '__main__':
    alphabet = ('A', 'B', 'C')
    number_string = ('1', '2')
    number_int = (1, 2)

    print(seat_id_gen(alphabet, number_string))
    print(seat_id_gen(alphabet, number_int))
