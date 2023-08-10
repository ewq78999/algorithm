import sys
from pathlib import Path


file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)


T = int(input())

for tc in range(1, T+1):
    # E 간선의 개수
    # N 부모 노드(시작 노드)
    E, N = list(map(int, input().split()))

    nodes = list(map(int, input().split()))

    left_node = [0] * (E+2)
    right_node = [0] * (E+2)

    # 0부터 시작해서 E*2 간격만큼 반복, 2칸씩
    for i in range(0, E*2, 2):
        parent = nodes[i]
        child = nodes[i+1] #해당 i의 오른쪽으로 한칸 위치

        if left_node[parent] == 0:
            left_node[parent] = child
        
        else:
            right_node[parent] == child

    # print(left_node)
    # print(right_node)

    stack = [N]
    count = 0

    while stack:
        now = stack.pop()
        count += 1

        # 왼쪽, 오른쪽에 자식이 있는지 확인
        if left_node[now]:
            stack.append(left_node[now])
        if right_node[now]:
            stack.append(right_node[now])

    print(count)














# def dfs(idx):
#     global count
#     count += 1

#     for i in node[idx]:
#         dfs(i)

# T = int(input())

# for tc in range(1, T+1):
#     # E 간선의 개수
#     # N 간선의 개수
#     E, N = list(map(int, input().split()))
#     temp_list = list(map(int, input().split()))
#     tree = [[] for _ in range(E+2)]
#     for idx, i in enumerate(range(0, E*2, 2)):
#         a = int(temp_list[i])
#         b = int(temp_list[i+1])

