# 프로세서 연결하기

# 해야 할 작업이 많아서 상당히 어려웠던 문제.
# 그래도 혼자 풀 때 80% 근처까지 간 것 같은데, 문제는 있었음.
# 내 처음 방식은 모든 코어에 대해서 반복, 상하좌우 한 방향으로 전선을 뻗다가 못 가면 다시 되돌림.
# 그런데 값을 매번 바꿔가면서 반복을 돌았고, 갈 수 없는 방향에 대해서고 바꿔가다가 도달해야만 알 수 있었기에 시간초과.

# 해답은 바꾸진 않고 지정한 방향으로 1칸씩 이동하며 갈 수 있는지를 확인하고, 그 길이를 리턴하는 check함수를 사용.
# 이후 해당 함수에서 받은 가능한 연결 길이만큼 connect함수로 값을 변경. 비트연산자 ^= 를 활용해 되돌리기도 가능.
# 이를 모든 경우에 대해 반복하여 최대 연결 개수와 최소 연결 길이를 갱신.

# 현재 좌표에서 주어진 방향으로 연결 가능한지 탐색. 연결 가능하다면 연결 길이를 저장.
def check(i, j):
    direction = [0, 0, 0, 0]    # 각 방향으로 연결 가능한 길이.

    for d in range(4):
        ci, cj = i, j
        length = 0

        while 0 < ci < N - 1 and 0 < cj < N - 1:
            length += 1
            ci += di[d]
            cj += dj[d]

            if graph[ci][cj]:
                break

        # while 내에서 break 없이 조건을 만족해 종료된 경우.
        else:
            direction[d] = length
    
    return direction

# 주어진 방향으로 연결이 가능하다면 graph의 값을 변경하여 연결.
def connect(i, j, d):
    ci, cj = i, j

    while 0 < ci < N - 1 and 0 < cj < N - 1:
        ci += di[d]
        cj += dj[d]
        graph[ci][cj] ^= 1


# dfs 형식으로 재귀를 각 코어가 가질 수 있는 모든 연결 방법의 조합을 탐색.
def recur(cur, total_length, count):
    global max_core, min_length

    # 최대 연결 코어 갯수보다 많으면 갱신.
    if max_core < count:
        max_core = count
        min_length = total_length
    
    # 개수가 같다면 더 짧은 길이를 갱신.
    elif count == max_core:
        min_length = min(min_length, total_length)

    if cur == core_cnt:
        return
    
    # 현재 확인중인 코어 좌표
    ci, cj = core[cur]

    # 현재 코어가 연결 가능한 방향과 그 길이.
    direction = check(ci, cj)

    # 연결 가능한 방향이라면 연결하고, 길이와 개수를 더해 갱신.
    for d in range(4):
        if direction[d] == 0:
            continue

        # 연결하고, 해당 경로 탐색 후 다시 연결 해제. => 백트래킹
        connect(ci, cj, d)
        recur(cur + 1, total_length + direction[d], count + 1)
        connect(ci, cj, d)
    
    recur(cur + 1, total_length, count)


if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        N = int(input())
        graph = [list(map(int, input().split())) for _ in range(N)]
        di = [0, 1, 0, -1]  # 우 하 좌 상
        dj = [1, 0, -1, 0]
        core = []
        core_cnt = 0

        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if graph[i][j] == 1:
                    core.append((i, j))
                    core_cnt += 1
        
        max_core = 0
        min_length = 0

        recur(0, 0, 0)

        ans.append(f'#{t} {min_length}')

    print("\n".join(ans))
