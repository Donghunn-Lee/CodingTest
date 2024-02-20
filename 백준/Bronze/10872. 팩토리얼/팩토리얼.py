# 팩토리얼

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

print(factorial(N))