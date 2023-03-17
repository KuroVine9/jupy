"""
Q1.7 Answer.
"""
import math
import time
import turtle


def first(t: 'turtle'):
    """
    첫 번째 문제
    :param t: turtle
    :return: None
    """
    t.forward(100)
    t.left(135)
    t.forward(math.sqrt(2 * (100 ** 2)))
    t.left(135)
    t.home()


def second(t):
    """
    두 번째 문제
    :param t: turtle
    :return: None
    """

    def drawTri(t):
        for i in range(3):
            t.forward(100)
            t.left(120)

    drawTri(t)
    t.left(60)
    drawTri(t)


if __name__ == '__main__':
    t = turtle.Turtle()
    first(t)
    time.sleep(1)
    t.clear()
    second(t)
    turtle.done()
