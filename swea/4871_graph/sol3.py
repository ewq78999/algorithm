# 인접 리스트 방식으로 그래프 표현  => 재귀함수를 이용하여 풀이

import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())

def dfs(now):
    # 방문체크
    check_list[now] = True

    # 현재 위치를 기준을 연결된 노드 찾기
    for link in nodes[now]:
        # 방문 안한 노드들은 스택에 추가
        if not check_list[link]:
            dfs(link)
    

            

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

    dfs(S)

    if check_list[G]:
        result = 1
    else:
        result = 0

    print(result)


