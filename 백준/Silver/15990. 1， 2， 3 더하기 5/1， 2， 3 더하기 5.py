# 1, 2, 3 더하기 5

T = int(input())
nums = [[0] * 3 for _ in range(100001)]

nums[1] = [1, 0, 0]
nums[2] = [0, 1, 0]
nums[3] = [1, 1, 1]


for i in range(4, 100001):
    nums[i][0] = (nums[i - 1][1] + nums[i - 1][2]) % 1000000009
    nums[i][1] = (nums[i - 2][0] + nums[i - 2][2]) % 1000000009
    nums[i][2] = (nums[i - 3][0] + nums[i - 3][1]) % 1000000009

for _ in range(T):
    N = int(input())
    print(sum(nums[N]) % 1000000009)