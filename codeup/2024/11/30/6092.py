n = int(input())
random_num = map(int, input().split())
num_list = [0 for i in range(24)]
for i in random_num:
    num_list[i] += 1
num_list.pop(0)
for i in num_list:
    print(i, end=' ')