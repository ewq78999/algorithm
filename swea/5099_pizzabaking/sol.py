import sys
from pathlib import Path


file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())


for tc in range(1, T+1):
    # N 화덕의 크기
    # M 피자의 개수
    N, M = list(map(int, input().split()))
    Ci = list(map(int, input().split()))

    # 피자에 번호를 부여하는 과정
    # 화덕에서 굽기 전 피자
    before = []

    for i in range(M):
        before.append([Ci[i], i])
    
    # 화덕
    pit = [0] * N

    # 완성 피자
    after = []

    while len(after) != M:
        # 화덕 입구에 공간이 비었으면
        if pit[0] == 0:
            # 넣을 피자가 있으면
            if len(before) != 0:
                # 남은 첫번째 치즈와 번호
                cheeze, idx = before.pop(0)
                # 화덕에 넣기
                pit.append([cheeze, idx])
                # 화덕 돌리기
                pit.pop(0)
            # 넣을 피자가 없을 떄
            else:
                pit.pop(0)
                pit.append(0)
                # pit.append(pit.pop(0))

        # 화덕 입구에 공간이 없으면 (이미 구워지고 있는 피자가 있다면)
        else:
            # 치즈 절반 감소, pit의 0번째 pizza의 치즈양 [0]
            pit[0][0] //= 2

            # 치즈가 다 녹았는지 확인
            if pit[0][0] == 0:
                pizza = pit.pop(0)

                after.append(pizza)

                if len(before) != 0:
                # 남은 첫번째 치즈와 번호
                    cheeze, idx = before.pop(0)
                    # 화덕에 넣기
                    pit.append([cheeze, idx])
                else:
                    pit.append(0)

            # 아직 더 돌려야 하는 경우
            else:
                pit.append(pit.pop(0))

    print(after)














    # N, M = list(map(int, input().split()))
    # pizza = list(map(int, input().split()))
    # oven = []

    # for i in range(M):
    #     oven.append(pizza.pop())

    # while len(oven) > 1:
        
    #     if len(oven) < N and pizza:
    #         oven.append(pizza.pop())

    #     pizza.number
            
            
    


    # for _ in range(M):
    #     if _ in numbers.pop(0):
    #         numbers = numbers //2
    #     numbers.append(numbers.pop(0))

    #     print(numbers[0].index)



