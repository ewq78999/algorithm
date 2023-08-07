import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    tc = int(input())
    matrix = []
    total = 0
    

    for _ in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)

    
    # temp = 0 # integer 범위를 넘어가지 않게 하기 위한 임시 변수
    for row in range(len(matrix)):
        temp = 0
        for col in range(len(matrix)):
            temp += matrix[row][col]
        if total < temp:
            total = temp

    for col in range(len(matrix)):
        temp = 0
        for row in range(len(matrix)):
            temp += matrix[row][col]
        if total < temp:
            total = temp

    
    for i in range(100):
        temp = 0
        temp += matrix[i][i]

        if total < temp:
            total = temp
    
    for i in range(100):
        temp = 0
        temp += matrix[i][99-i]

        if total < temp:
            total = temp

    print(f'#{tc} {total}') 


    
