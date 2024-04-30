n = int(input()) # проверяю мой 2 алгоритм
rect = []
x_cords = set()
y_cords = set()
for _ in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
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
m = int(input())
answ = []
for _ in range(m):
    x, y = map(int, input().split())
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
            l_ = m_+1
            break
        else:
            r_ = m_
    x_coord = l_-1

    l_ = 0
    r_ = len(y_cords)
    while l_ < r_:
        m_ = (l_ + r_) // 2
        if y_cords[m_] < y:
            l_ = m_ + 1
        elif y_cords[m_] == y:
            l_ = m_+1
            break
        else:
            r_ = m_
    y_coord = l_-1
    answ.append(map_[y_coord][x_coord])
print(*answ)
