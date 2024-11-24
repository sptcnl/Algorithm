ymd = input()
print(ymd[0:2], ymd[2:4], ymd[4:6])

# 다른풀이1
a = 0
b = 2
ymd = input()
for i in range(len(ymd) // 2):
    print(ymd[a:b], end=' ')
    a += 2
    b += 2

# 다른풀이2
ymd = list(input())
while ymd:
    print(ymd.pop(0), ymd.pop(0), sep='', end=' ')