import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # print(N, numbers)
    # # 정렬 후 큰 수, 작은 수 뽑아서 연산
    # numbers.sort()
    # result = numbers[-1] - numbers[0]

    # print(f'#{tc} {result}')

    # min_number = 100000000
    min_number = numbers[0]
    # max_number = 0
    max_number = numbers[0]

    for number in numbers:
        if min_number > number:
            min_number = number

        if max_number < number:
            max_number = number

result = max_number - min_number

print(f'#{tc} {result}')