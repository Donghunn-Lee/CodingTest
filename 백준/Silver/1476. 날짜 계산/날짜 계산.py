# 날짜 계산

E, S, M = map(int, input().split())

def bfs(e,s,m):
    count = 1

    while True:
        if (e, s, m) == (1, 1, 1):
            return count
        
        if e == 0:
            e = 15
        if s == 0:
            s = 28
        if m == 0:
            m = 19
        
        e -= 1
        s -= 1
        m -= 1
        count += 1

print(bfs(E, S, M))