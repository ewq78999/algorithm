import sys
sys.stdin = open('input.txt')

T = 10

######한 단계씩 진행할 때 마다 print하면서 확인하는 습관 들일 것 !!

for tc in range(1, T+1):
    # N 건물의 갯수
    # M N개 건물의 높이들
    N = int(input())
    M = list(map(int, input().split()))
    
    # print(M)
    
    total = 0
    for i in range(N):
        # print((i), M[i])
        now = M[1]

        if now == 0:
            continue

        else:
            # delta(dx)
            x = [-2, -1, 1, 2]
            max_tall = 0

            for j in range(4):
                # compare, x[j]는 0, 1, 2, 3 위치를 기준으로 -2, -1, 1, 2를 설정하게 함, 이후 i 와 합침
                # x[j] : 기준건물을 중심으로 좌우 index
                comp = M[i + x[j]]

                if max_tall < comp:
                    max_tall = comp

            if now > max_tall:
                view = now - max_tall
                total += view

    print(f'#{tc} {total}')







    # while current + M <= M_max:
    #     for step in range(M, 0, -2): # M이 갈 수 있는 범위에서 -2씩 줄여가면서 반복 계산
    #         if (current + step) in numbers:
    #             current += step
    #             count += 1
    #             break
            
    #         else:
    #             count = 0
    #             break

    #     for step in range(M, 0, 2):
    #         if (current + step) in numbers:
    #             current += step
    #             count += 1
    #             break

    #         else:
    #             count = 0
    #             break

    # print(f'#{tc}, {count}')
        

    # for j in range(i):
    #     left = [j]
    #     right  = [j+1]


    # while M >= M_min and M_max:
    #     if left <= M and right <= M:
    #         count += 1
    #         break

    #     else:
    #         count = 0
    #         break
    
    # print(f'#{i}, {count}')
        





