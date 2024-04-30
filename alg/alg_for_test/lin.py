import time


def lin_alg():
    rect_file = "data/rects_session.txt"
    points_file = "data/points_session.txt"
    rect = []
    with open(rect_file) as f:
        for line in f:
            rect.append(tuple(map(int, line.split())))
    answ = []
    start_time_alg = time.time()
    with open(points_file) as f:
        for line in f:
            x, y = map(int, line.split())
            count = 0
            for r in rect:
                if r[0] <= x < r[2] and r[1] <= y < r[3]:
                    count += 1
            answ.append(count)
    end_time_alg = time.time()
    return end_time_alg - start_time_alg
