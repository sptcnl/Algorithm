box = [[0]*11 for i in range(11)]
for i in range(1, 11):
    a = input().split()
    for j in range(1, 11):
        if a[j-1] == '1':
            box[i][j] = 1
        elif a[j-1] == '2':
            box[i][j] = 2

x = 2
y = 2
while True :
    if box[x][y] == 0 :
        box[x][y] = 9
    elif box[x][y] == 2 :
        box[x][y] = 9
        break

    if (box[x][y+1]==1 and box[x+1][y]==1) or (x==9 and y==9) :
        break

    if box[x][y+1] != 1 :
        y += 1
    elif box[x+1][y] != 1 :
        x += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(box[i][j], end=' ')
    print()
# 개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
# (오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)
