n = int(input())
if (n < 0) and (n % 2 == 0):
    print('A')
elif (n < 0) and (n % 2 == 1):
    print('B')
elif (0 < n) and (n % 2 == 0):
    print('C')
elif (0 < n) and (n % 2 == 1):
    print('D')