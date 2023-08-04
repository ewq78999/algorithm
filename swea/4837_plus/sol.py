import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(range(1, 13))
    N, K = list(map(int, input().split()))
    count = 0

    for i in range(1 << len(numbers)):
        
        temp = []
        for j in range(len(numbers)):
            if i & (1 << j):
                temp.append(numbers[j])

        if len(temp) == N and sum(temp) == K:
            count += 1

    print(count)
