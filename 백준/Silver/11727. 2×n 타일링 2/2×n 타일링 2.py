# 2xn 타일링 2
n = int(input())

box = {1 : 1, 2 : 3}

def DP (n):
    if n in box:
        return box[n]
    
    tmp = DP(n - 1) + DP(n - 2) * 2
    box[n] = tmp

    return box[n]

print(DP(n) % 10007)