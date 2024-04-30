n = int(input())
rect = []
for _ in range(n):
    rect.append(tuple(map(int, input().split())))
m = int(input())
answ = []
for _ in range(m):
    x, y = map(int, input().split())
    count = 0
    for r in rect:
        if r[0] <= x < r[2] and r[1] <= y < r[3]:
            count += 1
    answ.append(count)
print(*answ)