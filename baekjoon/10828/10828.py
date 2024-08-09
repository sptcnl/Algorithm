# https://www.acmicpc.net/problem/10828
# 아직 미완성
stack = []
N = int(input())

for i in range(N):

    command = input().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif command[0] == 'pop':
        if not stack:
            print(-1)
        else:
            stack.pop()