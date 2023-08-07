import sys
sys.stdin = open('input.txt')

T = int(input())

memo = [0, 1, 3]
for tc in range(1, T+1):
    N = int(input()) // 10

    # memo 배열에 출력시킬 값이 없으면 추가
    while N >= len(memo):
        # n-2 배열에 가로로 작은 사각형 두개를 쌓거나 큰 사각형 쌓는 방법 (x2)
        # n-1 세로로 작은 사각형 쌓는 방법 하나
        temp = 2 * memo[len(memo)-2] + memo[len(memo)-1]
        memo.append(temp)

    print(memo[N])




# def paper(n):
#     if n==1:  # 20 x 10 cm : 경우의 수 1가지
#         return 1
#     elif n==2: # 20 x 20 cm : 경우의 수 3가지
#         return 3
#     return paper(n-1) + (2*paper(n-2)) 
#               # (20 x 20cm) + 2 * (20 x 10 cm)

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     count = paper(N // 10)


#     print(f'#{tc} {count}')






# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     result = []
#     num = [1, 2, 3]

#     n = N
#     def fibo(n):
#         if n % 10 == int():
#             1
        
# 30, 50, 70은 각각 1, 2, 3 번째 자리다.
# 1 + (4 ** 자리) = 구해야 될 값


# 0번째 = 1   0 + 4 ** 0(가상)

# 1번째 = 5   1 + 4 ** 1(순서)
# 2번째 = 21  5 + 4 ** 2(순서)   
# 3번째 = 85  21 + 4 ** 3(순서)





# import sys
# from pathlib import Path

# file_path = Path(file).parent
# input_path = file_path / 'input.txt'
# sys.stdin = open(input_path)

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     arr = [0 for i in range(7)]
#     arr[0] = 1
#     arr[1] = 3

# for i in range(2,7):
#     arr[i] = 2 * arr[i-2] + arr[i-1]


# print(arr)





# def factorial(n):
#     if n <= 1: 
#         return 1 
#     else:
#         return factorial(n-1) * n 

# T = int(input())


# for tc in range(1, T+1):
#     result = 0
#     length = int(input())
#     for i in range(0, length//20 + 1):
#         # i는 가로 구성에서 20의 개수
#         result += factorial((length-20i)/10 + i) / factorial((length-20i)/10) / factorial(i) * (2 ** i)
#         # (20 i 개와 10 들의 구성의 경우의 수) * 
#     print(f'#{tc} {int(result)}')

