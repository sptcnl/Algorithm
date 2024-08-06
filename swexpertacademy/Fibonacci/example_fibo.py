# memoization(메모이제이션)

def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:   # n이 2보다 같거나 크고, 메모의 길이가 n과 같거나 작으면
        memo.append(fibo1(n-1) + fibo1(n-2))    # 재귀 시작
    return memo[n]      # n이 1 이하이거나 메모의 길이가 n보다 크면, 메모의 n번째를 리턴
    
memo = [0, 1]       # 0과 1은 굳이 계산 안해도 되니 미리 저장 - 메모이제이션


# DP

def fibo2(n):
    f = [0, 1]

    for i in range(2, n+ 1 ):
        f.append(f[i-1] + f[i-2])

    return f[n]