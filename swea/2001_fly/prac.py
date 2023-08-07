import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = []
    total = 0

    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_total = 0
            for row in range(M):
                for col in range(M):
                    temp_total += matrix[i+row][j+col]

            if total < temp_total:
                total = temp_total

    print(f'#{tc} {total}')

    
