"""
Q8.3 Answer.
"""
import typing


def print_record(student_dict: dict[str, list[typing.Any]]):
    print("학생의 정보 목록")
    for record in student_dict.items():
        print(record)
    print()


if __name__ == '__main__':
    student_tup = (
        ("211101", "최성훈", "010-1234-4500"),
        ("211102", "김은지", "010-2230-6540"),
        ("211103", "이세은", "010-3232-7788")
    )
    student_dict = dict(map(lambda record: (record[0], [record[1], record[2]]), student_tup))

    print_record(student_dict)

    student_id = input("학번을 입력하세요 : ")
    print(f"이름 : {student_dict[student_id][0]}\n연락처 : {student_dict[student_id][1]}")

    student_dict["211101"].append(4.3)
    student_dict["211102"].append(3.9)
    student_dict["211103"].append(4.25)

    print_record(student_dict)

    print(f"전체 학생의 학점 평균 : {round(sum(list(map(lambda val: val[2], student_dict.values()))) / len(student_dict), 2)}")
