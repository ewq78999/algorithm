import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    tc = int(input())
    matrix = []

    for i in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)

    total = 0

    
    # 가로 우선 탐색
    for row in range(len(matrix)):
        temp = 0 # 임시 변수, 가로줄이 한 번 돌면 0으로 다시 돌아옴
        for col in range(len(matrix[0])):
            temp += matrix[row][col]
        if total < temp:
            total = temp

    # 세로 우선 탐색
    for col in range(len(matrix[0])):
        temp = 0 # 임시 변수, 가로줄이 한 번 돌면 0으로 다시 돌아옴
        for row in range(len(matrix)):
            temp += matrix[row][col]
        if total < temp:
            total = temp

    # 좌상단 => 우하단 대각선 반복
    temp = 0
    for i in range(100):
        temp += matrix[i][i]

    if total < temp:
        total = temp

    # 우상단 => 좌하단 대각선 반복
    for i in range(100):
        temp += matrix[i][99-i]

    if total < temp:
        total = temp


    print(f'#{tc} {total}')    
