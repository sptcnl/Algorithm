n = int(input())
sum = 0
count = 1
while True:
    sum += count
    count += 1
    if sum >= n:
        break
print(sum)