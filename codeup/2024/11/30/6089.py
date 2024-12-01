a, r, n = map(int, input().split())
r_list = [a]
x = 0
while True:
    rx = r_list[x]
    if x + 1 == n:
        print(rx)
        break
    r_list.append(rx * r)
    x += 1