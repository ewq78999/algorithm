import sys
sys.stdin = open('input.txt', encoding = 'utf-8')

char = input()

if char.isupper():
    # 대문자인 경우
    result = char.lower()
else:
    
    # 소문자인 경우
    result = char.upper()

print(char, result)
print(ord(char), ord(result))