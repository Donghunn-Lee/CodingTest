# Magnetic

# 모양만 보고 graph 문제인 것을 확인, 슥 읽고 bfs를 쓰려고 함.
# 그런데 def bfs() 적고 머리 좀 굴려보니 이게 순서에 따라 자성체 이동시 아직 이동하지 않은 자성체에 막히는 문제를 파악.
# 그래서 자성체를 잘 합치고 붙여주기만 하면 한 번만 돌려도 풀 수 있다는 점을 확인.
# 자성체 발견시 극에 맞는 방향으로 이동시키고, 그 때 같은 극이면 합치고 아니면 deadlock에 바로 추가함.
# 다만 이렇게 하면 1쌍의 교착상태의 자성체가 각각 deadlock을 증가시키므로 값이 실제의 2배가 되어서 2로 다시 나눠줘야함.

def magnetic_field_activate():
    deadlock = 0
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                cur = i + 1

                while True:
                    if cur == N or graph[cur][j] == 1:
                        graph[i][j] = 0
                        break

                    if graph[cur][j] == 0:
                        cur += 1

                    elif graph[cur][j] == 2:
                        deadlock += 1
                        break

            if graph[i][j] == 2:
                cur = i - 1

                while True:
                    if cur == -1 or graph[cur][j] == 2:
                        graph[i][j] = 0
                        break

                    if graph[cur][j] == 0:
                        cur -= 1

                    elif graph[cur][j] == 1:
                        deadlock += 1
                        break
    
    return deadlock // 2

if __name__ == "__main__":
    ans = []

    for t in range(1, 11):
        N = int(input())
        graph = [list(map(int, input().split())) for _ in range(N)]

        ans.append(f'#{t} {magnetic_field_activate()}')
    
    print("\n".join(ans))
    
