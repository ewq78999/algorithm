import sys
from pathlib import Path


file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)


def inorder(idx):
    global count
    if idx <= N:
        
        # 왼쪽 자식
        inorder(idx*2)

        # 현재 노드
        tree[idx] = count
        count += 1

        # 오른쪽 자식
        inorder(idx*2+1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 첫번째 노드 값은 사용 안할 것이므로 다 1씩 더해줌
    tree = [0] * (N+1)
    count = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')












# # 완전 이진 트리의 노드 번호는 루트 1번
# # 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트

# def make_tree(n):
#     global count
#     # n = 왼쪽 서브트리의 루트, N = 현재 노드
#     # 왼쪽 노드는 현재 index의 2배
#     if n <= N:
#         make_tree(n*2)

#         # tree가 n까지 다 내려감
#         tree[n] = count
#         count += 1

#         #오른쪽은 index 2배에 +1 해야함
#         make_tree(n*2 +1)

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#   # 첫번째 노드 값은 사용 안할 것이므로 다 1씩 더해줌
#     tree = [0 for _ in range(N+1)]
#     count = 1
#     make_tree(1)

#     print(f'#{tc} {tree[1]} {tree[N//2]}')



