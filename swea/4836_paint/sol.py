import sys
sys.stdin = open('input.txt')

T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     position = [set({}), set({})]

#     for i in range(N):
#         r1, c1, r2, c2, color = map(int, input().split())
#         for a in range(r1, r2+1):
#             for b in range(c1, c2+1):
#                 position[color-1].add((a, b)) 
#                 # color [1],[2]에서 각각 1씩 빼서 [0], [1]로 만든 후
#                 # 빨강, 파랑 점을 반복해 찍으면서 집합에 넣은 후 
#                 # set를 사용해서 x,y를 빼낸 다음 & 를 사용해 교집합
    
#     result = position[0] & position[1]
        
        
#     print(f'#{tc} {len(result)}')



# for tc in range(1, T+1):
#     grid = [[0]*10 for _ in range(10)]
#     N = int(input())
#     purple = 0

#     for i in range(1, N+1):
#         r1, c1, r2, c2, color = map(int, input().split())

#         for x in range(r1, r2+1):
#             for y in range(c1, c2+1):
#                 grid[x][y] += color

#                 # color 빨강 = 1, color 파랑 = 2 thus 1 + 2 = 3(purple)
#                 if grid[x][y] == 3:
#                     purple += 1

#     print(f'#{tc} {purple}')


for tc in range(1, T+1):
    
    N = int(input())

    board = [[0 for _ in range(10)] for _ in range(10)]  
            # [[0]*10 for _ in range(10)], 0으로 가득 찬 보드

    for i in range(N):
        # [2, 2, 4, 4, 1] => r1, c1, r2, c2, color
        color_data = list(map(int, input().split()))

        left_top_x = color_data[0]
        left_top_y = color_data[1]
        right_bottom_x = color_data[2]
        right_bottom_y = color_data[3]
        color = color_data[4]

        # 색칠시작
        for x in range(left_top_x, right_bottom_x+1):
            for y in range(left_top_y, right_bottom_y+1):
                board[x][y] += color

    count = 0

    for x in range(board):
        for y in range(board[0]):
            if board[x][y] == 3:
                count += 1

    print[board]



