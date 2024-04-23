# Σ

# 문제가 역대급으로 길었던 문제. swea 역량평가인줄.
# 골드 3인걸 보고 예상은 했지만, 지문 자체만 이해하면 구조는 그렇게 어려운 문제가 아니었음.
# 거듭제곱을 분할정복으로 구할 줄만 알면 되는 문제. 전에 비슷한 곱셈은 몇 번 풀어봐서 이 구조자체는 대충 파악하고 있음.
# 다만 나는 문제를 읽다가 포기했으므로 검색해서 알아봤다는 점.
#
import sys
input = sys.stdin.readline

mod = 1_000_000_007

# def cal_gcd(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return cal_gcd(b, a % b)

def cal_ans(N, S):
    return S * mul(N, mod - 2) % mod

def mul(b, x):
    if x == 1:
        return b
    
    if x % 2 == 0:
        tmp = mul(b, x // 2)
        return tmp * tmp % mod
    
    else:
        return b * mul(b, x - 1) % mod


if __name__ == "__main__":
    M = int(input())
    ans = 0

    for _ in range(M):
        N, S = map(int, input().split())
        # gcd = cal_gcd(N, S)
        # N //= gcd
        # S /= gcd
        ans += cal_ans(N, S)
        ans %= mod
    
    print(int(ans))