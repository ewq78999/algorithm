############인접 리스트 방식##############

import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # V : 노드 수 / E : 간선 수
    V, E = list(map(int, input().split()))

    nodes = [ [] for _ in range(V+1) ]
    # pprint(nodes)

    # 인접 리스트 방식으로 그래프를 저장
    # 간선의 갯수만큼 반복을 진행
    for line in range(E):
        start, end = list(map(int, input().split()))
        nodes[start].append(end)
    # pprint(nodes)

    # S : 출발노드 / G : 도착노드
    S, G = list(map(int, input().split()))

    check_list = [False] * (V+1)

    stack = []

    now = S
    check_list[now] = True
    stack.append(now)

    result = 0

    while len(stack):
        now = stack.pop()
        check_list[now] = True

        # 인접리스트를 기준으로 now와 연결된 link 노드들을 반복
        for link in nodes[now]:
            # 방문하지 않았다면
            if not check_list[link]:
                # 목적지가 연결되어 있다면
                if link == G:
                    result = 1

                # 스택에 추가
                stack.append(link)

    print(f'#{tc} {result}')
        





    # # 방문 체크용 리스트
    # check_list = [False] * (V+1)

    # # dfs를 구현하기 위한 stack
    # stack = []

    # now = S
    # check_list[now] = True
    # stack.append(now)

    # result = 0


    # while stack :
    #     # stack의 최상단 값을 꺼낸다.
    #     check_node = stack.pop()
    #     # 꺼낸 값이 목표와 같다면 도달할 방법이 있으므로 반복을 종료
    #     if check_node == G:
    #         is_Check = True
    #         break
    #     # 꺼낸 값이 목표와 다를 때 아직 방문하지 않은 노드라면 노드와 연결된 점들을 stack에 넣어준다.
    #     elif not check_list[check_node]:
    #         stack.extend(adj[check_node])
    #     # 방문했다는 표시를 해준다.
    #     check_list[check_node] = True
    # # 경로가 존재하면 1을 출력
    # if is_Check :
                    
        # print(f'#{i} {result}')


