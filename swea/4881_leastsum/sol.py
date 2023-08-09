import sys
from pathlib import Path


file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

#### 최종 ####

T = int(input())

def search(idx, visited, SUM):
    global MIN_SUM

    # 재귀함수가 무한히 돌지 않게 방지
    if idx >= N:
        if SUM < MIN_SUM:
            MIN_SUM = SUM
        return
    
    if SUM > MIN_SUM:
        return

    for i in range(N):
        if visited[i] == False:

        # print(idx, 1, '=', numbers[idx][i])
            # result.append(numbers[idx][i])
            SUM += numbers[idx][i]
            visited[i] = True
            search(idx+1, visited, SUM)
            # result.pop()
            SUM -= numbers[idx][i]
            visited[i] = False

for tc in range(1, T+1):
    N = int(input())
    
    numbers = []
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number)

    result = []
    visited = [False] * N

    SUM = 0
    MIN_SUM = 10000000

    search(0, visited, SUM)

    print(f'#{tc}{MIN_SUM}')



































# def dfs(row):
#     global part_sum, min_sum

#     if part_sum > min_sum:
#         return
    
#     if row == N:
#         if part_sum < min_sum:
#             part_sum = min_sum

#     for col in range(N):
#         if not visited[col]:
#             visited[col] = True
#             # part_sum += graph[row][col]
#             # (row+1)
#             # # find_min이 바닥까지 가거나 pruning 된 후에야 위에 것이 끝나므로
#             # # 다시 현재 row로 올라와야 한다.
#             # visited[i] = False
#             # partial_sum -= arry[row][i]



# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     graph = [ [list(map(int, input().split()))] for _ in range(N+1) ]

#     visited = [False] * N
#     part_sum, min_sum = 0, 10000
    
#     dfs(0)


#     print(f'#{tc} {min_sum}')


































# def dfs(row):
#     global part_sum, min_sum

#     if part_sum > min_sum:
#         return
    
#     if row == N:
#         if part_sum < min_sum:
#             part_sum = min_sum

#     for col in range(N):
#         if not visited[col]:
#             visited[col] = True
#             # part_sum += graph[row][col]
#             # (row+1)
#             # # find_min이 바닥까지 가거나 pruning 된 후에야 위에 것이 끝나므로
#             # # 다시 현재 row로 올라와야 한다.
#             # visited[i] = False
#             # partial_sum -= arry[row][i]



# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     graph = [ [list(map(int, input().split()))] for _ in range(N+1) ]

#     visited = [False] * N
#     part_sum, min_sum = 0, 10000
    
#     dfs(0)


#     print(f'#{tc} {min_sum}')
