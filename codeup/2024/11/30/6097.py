h , w = map(int, input().split())
z_list = [[0]*(w+1) for i in range(h+1)]
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0: # 가로
                z_list[x][y+j] = 1
        else: # 세로
                z_list[x+j][y] = 1
for i in range(1, h+1):
    for j in range(1, w+1):
        print(z_list[i][j], end=' ')
    print()