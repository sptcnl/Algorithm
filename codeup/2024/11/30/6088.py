a, d, n = map(int, input().split())
d_list = [a]
x = 0
while True:
    dx = d_list[x]
    if x + 1 == n:
        print(dx)
        break
    d_list.append(dx + d)
    x += 1