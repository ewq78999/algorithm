import sys
sys.stdin = open('elecbus.txt')

T = int(input())

for tc in range(1, T+1):
    # K 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N 종점인 정류장
    # M 충전기가 설치된 정류장 번호
    K, N, M = list(map(int, input().split()))
    charge_station = list(map(int, input().split()))
    count = current = 0



    while current + K < N:
        for step in range(K, 0, -1): # K가 갈 수 있는 범위인 3에서 -1씩 줄여가면서 반복 계산
            if (current + step) in charge_station:
                current += step
                count += 1
                break

        else:
            count = 0
            break

    print(f'#{tc}, {count}')