# 최소공배수

T = int(input())
ans = []

def lcm(a, b):
    n = 2
    tmp = []
    result = 1
    
    if b == 1:
        return a
    
    while n <= b:
        if a % n == 0 and b % n == 0:
            a //= n
            b //= n
            tmp.append(n)
        else :
            n += 1
    
    if tmp:
        for i in tmp:
            result *= i
        return result * a * b
    else:
        return a * b



for i in range(T):
    A, B = map(int, input().split())
    if A > B:
        ans.append(lcm(A, B))
    else:
        ans.append(lcm(B, A))

for i in ans:
    print(i)