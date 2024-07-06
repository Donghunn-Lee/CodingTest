# 요세푸스 문제 0

import sys
input = sys.stdin.readline

def sol(n, k):
    seq = list(range(1, N + 1))
    ans = []

    cur, cnt, total = 0, 0, 0

    while total < n:
        if n <= cur:
            cur = 0
        
        if seq[cur]:
            cnt += 1

            if cnt == k:
                ans.append(seq[cur])
                seq[cur] = 0
                total += 1
                cnt = 0
        
        cur += 1
    
    return '<' + ", ".join(map(str, ans)) + ">"


if __name__ == "__main__":
    N, K = map(int, input().split())
    
    print(sol(N, K))