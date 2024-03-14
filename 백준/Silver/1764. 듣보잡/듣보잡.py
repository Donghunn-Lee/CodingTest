# 듣보잡

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    unheard = {input().strip() for _ in range(N)}
    never_see = {input().strip() for _ in range(M)}
    ans = sorted(list(unheard & never_see))

    print(len(ans))
    sys.stdout.write('\n'.join(ans))