"""
Q3.9 Answer.
"""

if __name__ == '__main__':
    avgSpeed = float(input("평균 시속(kph) : "))
    time = float(input("이동 시간(h) : "))

    print(f"평균 시속 : {avgSpeed}km/h")
    print(f"이동 시간 : {int(time)}시간 {int((time - int(time)) * 60)}분 {int(time * 3600) % 60}초")
    print(f"이동 거리 : {avgSpeed * time}km")
