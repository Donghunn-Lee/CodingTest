# N과 M (8)

import sys
input = sys.stdin.readline

def backtracking(count):
    if count == M:
        print(" ".join(map(str, ans)))
        return 
    for i in seq:
        if not ans or ans[-1] <= i:
            ans.append(i)
            backtracking(count + 1)
            ans.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    seq.sort()
    ans = []

    backtracking(0)