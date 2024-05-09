# Magnetic

# 모양만 보고 graph 문제인 것을 확인, 슥 읽고 bfs를 쓰려고 함.
# 그런데 def bfs() 적고 머리 좀 굴려보니 이게 순서에 따라 자성체 이동시 아직 이동하지 않은 자성체에 막히는 문제를 파악.
# 그래서 자성체를 잘 합치고 붙여주기만 하면 한 번만 돌려도 풀 수 있다는 점을 확인.
# 자성체 발견시 극에 맞는 방향으로 이동시키고, 그 때 같은 극이면 합치고 아니면 deadlock에 바로 추가함.
# 다만 이렇게 하면 1쌍의 교착상태의 자성체가 각각 deadlock을 증가시키므로 값이 실제의 2배가 되어서 2로 다시 나눠줘야함.

def magnetic_field_activate():
    deadlock = 0
    
    # 전체 그래프를 1회 탐색.
    for i in range(N):
        for j in range(N):
            # N극 자성체를 발견한 경우.
            if graph[i][j] == 1:
                cur = i + 1     # 비교를 위해 + 1한 위치에서 시작.

                while True:
                    # 자성체가 떨어지거나 같은 극 자성체를 만난 경우,
                    # 붙어버린 같은 극의 자성체는 1개로 간주하므로 이동중인 자성체의 원래 위치에 0을 할당해 없애버림.
                    if cur == N or graph[cur][j] == 1:
                        graph[i][j] = 0
                        break

                    # 빈 공간이면 계속해서 이동.
                    if graph[cur][j] == 0:
                        cur += 1

                    # 반대 극의 자성체를 만난 경우, 이 둘은 교착 상태이며 사이에 다른 자성체가 없음을 확인.
                    # 여기서 두 자성체를 다른 값으로 바꿔 고정시키는 방법 등도 고려해봤으나,
                    # 그렇게 하면 뒤에서 같은 극의 자성체가 붙게 되는 경우 곤란해짐. 그래서 그냥 deadlock + 1.
                    elif graph[cur][j] == 2:
                        deadlock += 1
                        break

            # S극 자성체를 발견한 경우. 위와 방향만 바꾸어 동일하게 진행.
            elif graph[i][j] == 2:
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
    
    # 1쌍의 교착상태를 이루는 두 자성체가 각각 deadlock을 증가시키므로 2로 나누어 반환.
    return deadlock // 2

if __name__ == "__main__":
    ans = []

    for t in range(1, 11):
        N = int(input())
        graph = [list(map(int, input().split())) for _ in range(N)]

        ans.append(f'#{t} {magnetic_field_activate()}')
    
    print("\n".join(ans))