import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    