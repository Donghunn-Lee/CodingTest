# 2 x n 타일링

n = int(input())

box = {1 : 1, 2 : 2}

def DP (n):
    if n in box:
        return box[n]
    tmp = DP(n - 1) + DP(n - 2)
    box[n] = tmp % 10007

    return box[n]

print(DP(n))