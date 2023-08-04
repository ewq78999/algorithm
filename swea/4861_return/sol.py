import sys
from pathlib import Path
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    string_map = []
    result = []
    for string in range(N):
        string_map.append(input()) 
        # data가 띄어쓰기가 없기 때문에 split 사용 불가, 그래서 list 사용하면 쪼개기 가능 ['G', 'C', 'B' ...]

    # pprint(string_map)
    
    # 가로 기준점을 잡기 위한 코드
    ###### row : 행 / col : 렬 ######
    for row in range(N):
        for col in range(N-M+1):
            # pprint(string_map[row][col])

            
            for i in range(M//2): # 반복문 범위를 반으로 줄여줌
                # front : 앞글자, 현재 위치에서 i만큼 증가
                f = string_map[row][col+i]
                # back : 뒷글자, 뒤의 끝에서부터 -i만큼 감소
                b = string_map[row][col+M-1-i]
                
                # 앞뒤가 똑같다면
                if f == b:
                    continue
                # 똑같지 않다면
                else:
                    break
            # for문을 끝가지 도는 경우 / break를 만나지 않은 경우 = 회문을 찾았다 !!
            else:
                result = []
                for a in range(M):
                    result.append(string_map[row][col+a])

    # 세로 기준점 / 회문의 시작점을 잡기 위한 코드
    for col in range(N):
        for row in range(N-M+1):

            for i in range(M//2):
                # front : 앞글자, 현재 위치에서 i만큼 증가
                f = string_map[row+i][col]
                # back : 뒷글자, 뒤의 끝에서부터 -i만큼 감소
                b = string_map[row+M-1-i][col]
                
                # 앞뒤가 똑같다면
                if f == b:
                    continue
                # 똑같지 않다면
                else:
                    break
            # for문을 끝가지 도는 경우 / break를 만나지 않은 경우 = 회문을 찾았다 !!
            else:
                result = []
                for a in range(M):
                    result.append(string_map[row+a][col])
    
    X = ''.join(result)
    print(f'#{tc} {X}')



###################################

# for tc in range(1, T+1):
#     # N : NxN 배열 크기
#     # M : 회문 길이
#     N, M = list(map(int, input().split()))

#     numbers = [input() for _ in range(N)]
#     # for i in range(N):
#     #    (numbers.append(input())

#     result = []

#    # 가로
#     for row in range(N):
#         for col in range(N-M+1):
#             row_list = []
#             for r in range(M):
#                 row_list.append(numbers[row][col+r])
#             if row_list == row_list[::-1]:
#                 result.append(''.join(row_list))

# 세로
#     for row in range(N-M+1):
#         for col in range(N):
#             col_list = []
#             for c in range(M):
#                 col_list.append(numbers[row+c][col])
#             if col_list == col_list[::-1]:
#                 result.append(''.join(col_list))

###################################
# for tc in range(1, T+1):
#     # N : NxN 배열 크기
#     # M : 회문 길이
#     N, M = list(map(int, input().split()))

#     numbers = [input() for _ in range(N)]
#     # for i in range(N):
#     #    (numbers.append(input())

#     result = []
    
    
#     for row in range(N):
#         for col in range(N-M+1): 
#             temp_row = []
#             temp_col = []
#             for i in range(M):
#                 temp_row += numbers[row][col+i]
#                 temp_col += numbers[col+i][row]

#             if temp_row == temp_row[::-1]:
#                 result.append(''.join(temp_row))
#             if temp_col == temp_col[::-1]:
#                 result.append(''.join(temp_col))