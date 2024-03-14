# 듣보잡

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    unheard = {input().strip() for _ in range(N)}
    never_see = {input().strip() for _ in range(M)}
    ans = list(unheard & never_see)
    
    ans.sort()
    print(len(ans))
    print('\n'.join(ans))
