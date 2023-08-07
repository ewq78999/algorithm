import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0]*10 for _ in range(10)]
    purple = 0

    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int,input().split()))

        if color == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    matrix [i][j] += 1

        else:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    matrix [i][j] += 1

        
        for i in range(10):
            for j in range(10):
                if matrix [i][j] == 2:
                    purple += 1

    print(f'#{tc} {purple}')

