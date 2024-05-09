# Ladder1

# 지난 준비때 풀다가 결국 못 풀고 남아 있던 문제. d4문제를 풀다가 추천 상위에 정답이 아닌 문제가 있는 것을 발견함.
# 분명 여타 문제과 다른 느낌의 구현 문제. 익숙치 않아서 조금 복잡하긴 했던 것 같음.
# 그래도 기본이 충실하다면 풀기 어려운 문제는 아니었고, 그 때의 내가 지나치게 버러지였을 뿐.

def ladder_down():

    # 맨 위의 100개를 돌며 시작점을 사다리 시작점을 찾아 탐색 시작.
    for j in range(100):
        if graph[0][j] == 1:
            # 찾은 이후로는 아래에서 사다리 끝까지 탐색이 이어지므로, 알기 쉽게 ci와 cj를 선언.
            ci, cj = 0, j

            # i가 끝에 이를 때까지 반복.
            while ci < 99:

                # 1칸씩 내려가면서 매번 왼쪽과 오른쪽에 이어진 다리가 있는지 확인.
                for dj in (1, -1):
                    nj = cj + dj

                    if 0 <= nj < 100 and graph[ci][nj] == 1:

                        # 이어진 다리가 있다면 다리 끝까지 이동.
                        while True:
                            nj = cj + dj

                            # 1이 아닌 지점에서 종료해야하며 인덱스 범위도 고려해야함.
                            if 0 <= nj < 100:
                                if graph[ci][nj] == 1:
                                    cj = nj

                                else:
                                    break
                            else:
                                break
                        
                        # 오른쪽(dj = 1)으로 이어진 다리를 찾았을 때,
                        # 이동 후 아래 break를 해주지 않으면 왼쪽(dj = -1)도 실행되어 다시 돌아감.
                        break
                
                # 아래로 1칸씩 이동.
                ci += 1

            # 반복이 끝났을 때 ci는 99가 되어 지정된 도착점에 도달했는지를 체크 후, 맞다면 종료.
            if graph[ci][cj] == 2:
                return j


if __name__ == "__main__":
    ans = []

    for t in range(1, 11):
        T = int(input())
        graph = [list(map(int, input().split())) for _ in range(100)]

        ans.append(f'#{t} {ladder_down()}')
    
    print("\n".join(ans))
