# 행렬 제곱

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def DC (a,b):
    if b == 1:
        return a % C
    else :
        tmp = DC(a, b // 2)
        if b % 2 == 0:
            return tmp * tmp % C
        else:
            return tmp * tmp * a % C

ans = DC(A, B)

print(ans)
