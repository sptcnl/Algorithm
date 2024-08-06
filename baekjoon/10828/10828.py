# https://www.acmicpc.net/problem/10828
# 아직 미완성

stack = []
N = input()

for i in N:
    command = input().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        if not stack:
            print(-1)
        