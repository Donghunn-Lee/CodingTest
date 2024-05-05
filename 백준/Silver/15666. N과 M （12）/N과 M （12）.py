# N과 M (12)

import sys
input = sys.stdin.readline

def backtracking(count):
    if count == M:
        print(" ".join(map(str, ans)))
        return 
    
    last = -1

    for i in range(N):
        if last == seq[i]:
            continue

        if not ans or ans[-1] <= seq[i]:
            ans.append(seq[i])
            backtracking(count + 1)
            last = ans.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    seq.sort()
    ans = []

    backtracking(0)