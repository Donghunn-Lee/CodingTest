# 1, 2, 3 더하기

T = int(input())

nums = {1 : 1, 2 : 2, 3 : 4}

def DP(n):
    if n in nums:
        return nums[n]
    
    tmp = DP(n - 3) + DP(n - 2) + DP( n - 1)
    nums[n] = tmp

    return nums[n]


for i in range(T):
    N = int(input())
    print(DP(N))


