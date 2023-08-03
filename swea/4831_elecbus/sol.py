import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K 최대 이동 가능한 정류장 수
    # N 종점 정류장
    # M 충전기가 설치된 정류장 수
    K, N, M = list(map(int, input().split()))
    charge_station = list(map(int, input().split()))
    count = 0 # count = 충전을 얼마나 했는지 저장
    current = 0
    now = 0

    # 충전할 필요가 없이 바로 도착하는 경우
    if K >= N:
        count = 0
    # 충전을 하면서 지나가야할 때
    else:
        # 버스가 아직 도착하지 않았다면 계속해서 반복
        while now < N:
            # 현재 위치(now)에서 최대로 갈 수 있는 범위를 찾는다.
            # 최대로 갈 수 있는 범위(now+K)부터 현재 위치까지 반복
            for i in range(now+K, now, -1):
                # 1. 최대범위가 종점을 넘는 경우
                if i >= N:
                    now = N
                    break

                # 2. 최대범위가 종점을 아직 넘지 않은 경우
                if i in charge_station:
                    # 가장 뒤에 있는 충전소로 이동
                    now = i
                    # 충전을 하고 이동을 했으니 카운트 증가
                    count += 1

                    # 마지막 충전소를 찾았으니 더 이상 후진할 필요 없음
                    break
            # 현재 위치에서 최대 거리를 찾았는데, 충전소가 없다면? => 도착 불가능
            else:
                count = 0
                now = N





    # while current + K < N:
    #     for step in range(K, 0, -1):
    #         if (current + step) in charge_station:
    #             current += step
    #             count += 1
    #             break
        
    #     else:
    #         count = 0
    #         break

    print(f'#{tc}, {count}')






# T = int(input())

# # T만큼 테스트 케이스 반복
# for tc in range(1, T+1):
#     # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
#     # N : 종점 정류장
#     # M : 충전기가 설치된 정류장 개수
#     K, N, M = list(map(int, input().split()))

#     # 충천지가 설치된 정류장 리스트 입력
#     charge_station = list(map(int, input().split()))
#     # 충전 횟수 count와 현재 위치 current 변수 초기화
#     count = current = 0

#     # 종점에 도착할 때까지 반복
#     while current + K < N:
#         # K 범위 안에서 현 위치를 조정하면서 이동
#         for step in range(K, 0, -1):
#             # 현재 위치 + 이동 거리만큼 이동했을 때 충전기가 있는 정류장일 경우
#             if (current + step) in charge_station:
#                 # 현재 위치를 변경
#                 current += step
#                 # 충전 횟수 +1
#                 count += 1
#                 # for 문을 종료
#                 break
#         # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우 count를 0으로 하고 while문을 종료
#         else:
#             count = 0
#             break

#     # 결과 출력
#     # print('#{} {}'.format(tc, count))