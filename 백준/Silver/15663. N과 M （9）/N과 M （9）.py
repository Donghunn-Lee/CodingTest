# N과 M (9)

import sys
input = sys.stdin.readline

def dfs(n, count):
    if count == M:
        result.add(tuple(tmp))
        return
    
    for i in range(len(seq)):
        if not tmp or i not in tmp2:
            tmp.append(seq[i])
            tmp2.add(i)
            dfs(n + 1, count + 1)
            tmp.pop()
            tmp2.remove(i)
        

if __name__ == "__main__":
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    seq.sort()
    result, tmp, tmp2 = set(), [], set()
    ans = []

    dfs(0, 0)

    result = sorted(list(result))

    for i in result:
        ans.append(' '.join(map(str, i)))

    print("\n".join(map(str, ans)))