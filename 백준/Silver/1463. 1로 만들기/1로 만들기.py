# 1로 만들기

N = int(input())

def DP(n):
    count = [0] * (n + 1)

    for i in range(2, n + 1):
        count[i] = count[i - 1] + 1
        if i % 3 == 0:
            count[i] = min(count[i], count[i // 3] + 1)
        if i % 2 == 0:
            count[i] = min(count[i], count[i // 2] + 1)

    return count[n]

print(DP(N))