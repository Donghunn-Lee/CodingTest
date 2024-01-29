T = int(input())
 
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    best_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for k in range(M):
                for l in range(M):
                    kill += arr[i+k][j+l]
            if kill > best_kill :
                best_kill = kill
 
    print("#%d %d" % (tc, best_kill))