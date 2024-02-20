# 팩토리얼 0의 개수

N = int(input())

def factorial(n):
    result = 1
    while n != 0:
        if n != 0:
            result *= n
            n -= 1
    
    if result:
        return result
    else:
        return 1

def countZero(n):
    tmp = str(n)
    for i in range(1, len(tmp)):
        if tmp[-i] != '0':
            return i-1
    return 0

print(countZero(factorial(N)))