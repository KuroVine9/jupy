"""
Q4.9 Answer.
"""

import turtle

if __name__ == '__main__':
    t = turtle.Turtle()
    t.shape("turtle")
    first = tuple(map(int, turtle.textinput("좌표 입력", "왼쪽 하단 모서리 좌표").split()))
    second = tuple(map(int, turtle.textinput("좌표 입력", "오른쪽 상단 모서리 좌표").split()))

    t.penup()
    t.goto(*first)
    t.pendown()
    t.goto(second[0], first[1])
    t.goto(second[0], second[1])
    t.goto(first[0], second[1])
    t.goto(*first)
    t.penup()

    point = tuple(map(int, turtle.textinput("좌표 입력", "점의 좌표 x, y").split()))
    t.goto(*point)
    t.pendown()
    t.circle(5.)

    if all(first[i] < point[i] < second[i] for i in range(len(point))):
        turtle.write("원 내부에 존재")
    else:
        turtle.write("원 외부에 존재")

    turtle.done()
