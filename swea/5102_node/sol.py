import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # V 노드 개수, E 간선 수
    V, E = list(map(int, input().split()))

    nodes = [ [0] * (V+1) for _ in range(V+1) ]

    # 인접행렬 방식으로 저장
    for line in range(E):
        start, end = list(map(int, input().split()))
        nodes[start][end] = 1
        nodes[end][start] = 1

    # S 출발 노드, G 도착 노드
    S, G = list(map(int, input().split()))

    # # 방문 체크용 리스트
    check_list = [False] * (V+1)

    # 거리계산을 위한 리스트
    distance = [0] * (V+1)

    # bfs를 구현하기 위한 queue
    queue = []

    # bfs 시작을 하기 위해 시작 노드를 queue에 저장
    now = S
    check_list[now] = True
    queue.append(now)


    # 큐가 비어있지 않으면 계속 반복
    while len(queue):
        now = queue.pop(0)
        check_list[now] = True

        # now와 연결된 다를 노드를 순회
        for link in range(V+1):
            if nodes[now][link] == 1:


                # 아직 방문하지 않은 node가 있다면
                if not check_list[link]:
                    # 큐에 추가
                    queue.append(link)

                    # 이전 노드의 거리 +1
                    distance[link] = distance[now] + 1

    # print(distance[G])

            












# T = int(input())

# def bfs(S, G):
#     x = [S]
#     while x:
#         now = x.pop(0)
#         if now == G: # 지금 도착해야 할 노드에 있다면 중지
#             return
        
#         for i in nodes[now]:
#             if not visited[i]:
#                 x.append(i)



# for tc in range(1, T+1):
#     # V 노드 개수, E 간선 수
#     V, E = list(map(int, input().split()))
#     # S 출발 노드, G 도착 노드
#     S, G = list(map(int, input().split()))
#     nodes = [ [] for _ in range(V+1) ]

#     visited = [0] * (V+1)

#     bfs(S)

#     # print(result)
    
