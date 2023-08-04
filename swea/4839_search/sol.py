import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # P 책의 장수(마지막 페이지)
    # A A가 찾아야하는 목적페이지
    # B B가 찾아야하는 목적페이지
    P, A, B = list(map(int, input().split()))

    count_a = 0
    left = 1 # 첫번째 1페이지
    right = P

    while True:
        middle = int((left+right)/2)

        # 목적페이지가 가운데보다 왼쪽에 있는 경우
        if A < middle:
            right = middle
        # 목적페이지가 가운데보다 오른쪽에 있는 경우
        elif middle < A:
            left = middle
        # 둘 다 아니라면 목적페이지에 도착
        else:
            break

        count_a += 1


    count_b = 0
    left = 1 # 첫번째 1페이지
    right = P

    while True:
        middle = int((left+right)/2)

        # 목적페이지가 가운데보다 왼쪽에 있는 경우
        if B < middle:
            right = middle
        # 목적페이지가 가운데보다 오른쪽에 있는 경우
        elif middle < B:
            left = middle
        # 둘 다 아니라면 목적페이지에 도착
        else:
            break

        count_b += 1

    print(count_a, count_b)