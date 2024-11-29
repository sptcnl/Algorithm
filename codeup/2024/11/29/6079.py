# https://codeup.kr/problem.php?id=6079
my_n = int(input())
sum = 0
n = 0
while sum <= my_n:
    sum += n
    if sum >= my_n:
        print(n)
        break
    n += 1