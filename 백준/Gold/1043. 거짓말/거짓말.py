# 거짓말

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    n_t, *truth = map(int, input().split())
    truth = set(truth)

    parties = []
    for _ in range(M):
        a, *b = map(int, input().split())
        parties.append(set(b))

    # people = [False] * (N + 1)
    count = 0

    for _ in range(50):
        for p in parties:
            if p & truth:
                truth |= p
    
    for p in parties:
        if p & truth:
            count += 1

    print(M - count)