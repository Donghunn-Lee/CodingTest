# 동전 0
import sys
input = sys.stdin.readline

def min_coins(k):
    count = 0

    for i in range(N - 1, -1, -1):
        if coins[i] <= k:
            tmp = k // coins[i]
            count += tmp
            k -= coins[i] * tmp
        
        if k == 0:
            return count

if __name__ == "__main__":
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]

    print(min_coins(K))