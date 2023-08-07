memo = [0, 1]

def fibo(n):
    if n >= 2 and len(memo) <= n: # n번째 숫자
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]


print(fibo(100))