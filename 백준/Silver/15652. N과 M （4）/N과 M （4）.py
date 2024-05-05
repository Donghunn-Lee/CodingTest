# N과 M (4)

import sys
input = sys.stdin.readline

def backtracking(count):
    if count == M:
        print(" ".join(map(str, ans)))
        return 
    
    for i in range(1, N + 1):
        if not ans or ans[-1] <= i:
            ans.append(i)
            backtracking(count + 1)
            ans.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    ans = []

    backtracking(0)