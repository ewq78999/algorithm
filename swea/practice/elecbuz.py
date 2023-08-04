import sys
sys.stdin = open('elecbus.txt')

test = int(input())

for tc in range(1,test+1):
    # K 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N 종점인 정류장
    # M 충전기가 설치된 정류장 번호
    K,N,M = map(int,input().split())
    charge_station = list(map(int,input().split()))
    cha = [0]*(N+1)

    for i in charge_station:
        cha[i] += 1
    idx = 0 # current
    count = 0

    while idx < N:
        if cha[idx+K]:
            idx = idx + K
            count += 1
        else:
            for j in range(1,K): # j를 설정 후 K에서 빼면서 K가 갈 수 있는 범위를 1씩 줄여가면서 반복 계산
                if cha[idx+K-j]:
                    idx = idx + K -j
                    count += 1
                    break
            else:
                count = 0
                break

        if idx + K >=N:
            idx = N

    print(f'#{tc} {count}')