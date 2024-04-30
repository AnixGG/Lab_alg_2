import time


def map_alg():
    rect_file = "data/rects_session.txt"
    points_file = "data/points_session.txt"
    rect = []
    x_cords = set()
    y_cords = set()
    start_time_prep = time.time()
    with open(rect_file) as f:
        for line in f:
            x1, y1, x2, y2 = tuple(map(int, line.split()))
            x_cords.add(x1)
            x_cords.add(x2)
            y_cords.add(y1)
            y_cords.add(y2)
            rect.append((x1, y1, x2, y2))
    x_cords = sorted(list(x_cords))
    y_cords = sorted(list(y_cords))
    map_ = [[0] * len(x_cords) for _ in range(len(y_cords))]
    for x1, y1, x2, y2 in rect:
        for ind_x, x in enumerate(x_cords):
            if not x1 <= x < x2:
                continue
            for ind_y, y in enumerate(y_cords):
                if y1 <= y < y2:
                    map_[ind_y][ind_x] += 1
    end_time_prep = time.time()
    answ = []
    start_time_alg = time.time()
    with open(points_file) as f:
        for line in f:
            x, y = map(int, line.split())
            if x >= x_cords[-1] or y >= y_cords[-1]:
                answ.append(0)
                continue
            l_ = 0
            r_ = len(x_cords)
            while l_ < r_:
                m_ = (l_ + r_) // 2
                if x_cords[m_] < x:
                    l_ = m_ + 1
                elif x_cords[m_] == x:
                    l_ = m_ + 1
                    break
                else:
                    r_ = m_
            x_coord = l_ - 1

            l_ = 0
            r_ = len(y_cords)
            while l_ < r_:
                m_ = (l_ + r_) // 2
                if y_cords[m_] < y:
                    l_ = m_ + 1
                elif y_cords[m_] == y:
                    l_ = m_ + 1
                    break
                else:
                    r_ = m_
            y_coord = l_ - 1
            answ.append(map_[y_coord][x_coord])
    end_time_alg = time.time()
    # print(*answ)
    return end_time_prep - start_time_prep, end_time_alg - start_time_alg
