# 비밀번호 찾기

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    passwards = dict()
    for _ in range(N):
        ad, pw = input().rstrip().split()
        passwards[ad] = pw
    
    ans = []

    for _ in range(M):
        target_domain = input().rstrip()
        ans.append(str(passwards[target_domain]))
    
    print("\n".join(ans))