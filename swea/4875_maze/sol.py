import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    # dfs를 동작하기 위한 스택
    stack = []
    stack.append(start) # 시작하기 위해 시작점 넣고 반복문 돌림

    # 상하좌우 델타값
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    result = 0
    # stack이 비어있을 때 까지
    while len(stack):
        now = stack.pop()
        x, y = now[0], now[1]

        # 한 칸씩 이동하며 통로를 1로 막으면서 진행한다
        maze[x][y] = 1

        # 상하좌우를 바라보는 코드
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 안에 있다면 진행
            if 0 <= nx < N and 0 <= ny < N:
                # 길이라면
                if maze[nx][ny] == 0:
                    stack.append((nx, ny)) # 내가 앞으로 가야할 좌표값을 tuple로 넣음
                # 도착지점이라면
                elif maze[nx][ny] == 3:
                    result = 1
                    break
                    
                    
    pprint(result)         








# move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# def boundary(x, y):
#     if x < 0 or y < 0 or x >= N or y >= N:
#         return True
#     return False

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     map_list = [[list(map(int, input().split()))] for _ in range(N)]
#     result = 0
#     x, y = 0, 0

#     for i in range(N):
#         if 2 in map_list[i]:
#             x = map_list[i].index(2)
#             y = i
#             break


#     stack = []
#     while stack:
#         x, y = stack.pop()
#         map_list[x][y] = 1

#         for X, Y in move:
#             dx = x + X
#             dy = y + Y

#             if boundary(dx, dy):
#                 continue
#             if map_list[dx][dy] == 3:
#                 result = 1
#                 break
#             elif not map_list[dx][dy]:
#                 stack.append((dx, dy))

#         else:
#             continue
#         break

#     print(result)







# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     miro = []
#     for _ in range(N):
#         miro.append(list(map(int, input()))) # 숫자가 붙어있으니깐 split 안됨
#     for j in range(N):
#         for i in range(N):
#             if miro[i][j] == 2:
#                 start = [i, j]
#             if miro[i][j] == 3:
#                 end = [i, j]
#     # print(miro)
#     # print(start)
#     # print(end)



#     check_list = [[[False] for _ in range(N)] for _ in range(N)]
#     stack = []
#     now = [] # 위치를 행과 열로 이루어진 리스트로 나타냄
#     now = start 
#     stack.append(now)

#     result = 0 
    
#     while len(stack): # 더이상 갈 곳이 없을 때 까지 
#         now = stack.pop()
#         check_list[now[0]][now[1]] = True

#        # 한 위치에서 4방향으로 갈 수 있음. 
#         a = [now[0]+1,now[1]]
#         b = [now[0]-1,now[1]]
#         l = [now[0],now[1]-1]
#         r = [now[0],now[1]+1]
#         directions = [a, b, l, r]
#         for dir in directions: # 그 방향들의 행과 열이 N 이하이고 이동했을 때 값이 0이여야 이동이 가능하다. 
#             if dir[0] < N and dir[1] > N and dir[0] >= 0 and dir[1] >= 0:
#                 if miro[dir[0]][dir[1]] == 0: # 왜 인덱스 아웃오브 에러가 나지... N 미만이여야 하는듯..  
#                     if not check_list[dir[0]][dir[1]]:
#                         if dir == end:
#                             result = 1
#                             break
#                         stack.append(dir)
#     print(result)
            





