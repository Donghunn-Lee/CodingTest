# N과 M (5)

import sys
input = sys.stdin.readline

def dfs(n, count):
    if count == M:
        ans.append(' '.join(map(str, tmp)))
        return
    
    for i in range(len(seq)):
        if not tmp:
            tmp.append(seq[i])
            tmp2.add(seq[i])
            dfs(n + 1, count + 1)
            tmp.pop()
            tmp2.remove(seq[i])

        elif seq[i] not in tmp2:
            tmp.append(seq[i])
            tmp2.add(seq[i])
            dfs(n + 1, count + 1)
            tmp.pop()
            tmp2.remove(seq[i])
        

if __name__ == "__main__":
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    seq.sort()
    ans, tmp, tmp2 = [], [], set()

    dfs(0, 0)

    print("\n".join(ans))