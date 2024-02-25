# 이친수

N = int(input())
pinaryNums = [[0, 0] for _ in range(N + 2)]
pinaryNums[1][1] = 1
pinaryNums[2][0] = 1

def DP (n) :
    if n < 3:
        return sum(pinaryNums[n])
    for i in range(3, n + 1):
        pinaryNums[i][0] = pinaryNums[i - 1][0] + pinaryNums[i - 1][1]
        pinaryNums[i][1] = pinaryNums[i - 1][0]
    
    return sum(pinaryNums[n])

print(DP(N))