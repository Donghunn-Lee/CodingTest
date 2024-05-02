# 미세먼지 안녕!

# 주요 계산식 자체는 어렵지 않다고 하더라도 for문 작성이 번거로웠음. 더 간편한 방법이 있으려나?
# 데이터를 함수로 넘길 때 어떻게 넘겨야 바람직한지 의문이 들게 했던 문제.

# 미세먼지 군집들의 좌표를 구하고, 이를 바탕으로 미세먼지 확산을 graph에 반영.
# 공기청정기의 위치를 기준으로 상단과 하단의 공기 순환을 진행.
# 이를 T초 동안 반복.
import sys
input = sys.stdin.readline

# 미세먼지들의 좌표를 구하는 함수.
def find_fine_dust(graph):
    fine_dust = []

    for i in range(R):
        for j in range(C):
            if 0 < graph[i][j]:
                fine_dust.append((i, j))
    
    return fine_dust


# 공기청정기의 좌표를 구하는 함수.
def init_location(graph):
    for i in range(R):
        if graph[i][0] == -1:
            return (i, i + 1)


# 미세먼지 확산
def dust_diffusion(fine_dust):
    # 모든 미세먼지들의 확산이 동시에 일어나므로, 확산 결과가 아직 미확산된 미세먼지에 반영되지 않도록 새 grpah생성.
    nxt_graph = [[0] * C for _ in range(R)]

    # 입력받은 미세먼지의 좌표들을 바탕으로 확산을 진행.
    for md in fine_dust:
        ci, cj = md

        amount = graph[ci][cj] // 5

        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            
            # 벽이거나 공기청정기인 방향으로는 확산이 진행되지 않음.
            if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] != -1:
                graph[ci][cj] -= amount
                nxt_graph[ni][nj] += amount

        nxt_graph[ci][cj] += graph[ci][cj]

    # 전역변수 graph의 메모리 주소를 바꾸지 않고 nxt_graph의 값을 반영.
    graph[:] = nxt_graph[:]


# 공기청정기에 청정 작업.
def air_cleaning(air_cleaner_pos):
    # 공기청정기는 2칸을 차지함. 위와 아래의 좌표를 분리.
    top_part, lower_part = air_cleaner_pos
    
    # 상단부의 공기 순환을 진행. top, bottom, right, left / up, down, left, right
    # tr => top-right : 상단에서 우측으로 부는 바람.
    # bu => bottom-up : 하단에서 상단으로 부는 바람.

    # 상단부 순환
    for td in range(top_part, 0, -1):
        graph[td][0] = graph[td - 1][0]
    
    for tl in range(C - 1):
        graph[0][tl] = graph[0][tl + 1]
    
    for ru in range(top_part):
        graph[ru][C - 1] = graph[ru + 1][C - 1]
    
    for br in range(C - 1, 0, -1):
        graph[top_part][br] = graph[top_part][br - 1]
    
    graph[top_part][:2] = [0, 0] # 공기청정기 위치와 새로운 바람이 나오는 곳은 0으로 초기화.

    # 하단부 순환
    for bu in range(lower_part, R - 1):
        graph[bu][0] = graph[bu + 1][0]
    
    for bl in range(C - 1):
        graph[R - 1][bl] = graph[R - 1][bl + 1]
    
    for rd in range(R - 1, lower_part, -1):
        graph[rd][C - 1] = graph[rd - 1][C - 1]
    
    for tr in range(C - 1, 0, -1):
        graph[lower_part][tr] = graph[lower_part][tr - 1]
    
    graph[lower_part][:2] = [0, 0]


# 미세먼지 확산과 청정 작업을 t초동안 반복하는 청정 순환.
def cleaning_circulation(graph, air_cleaner_pos, t):
    for _ in range(t):
        # 갱신된 graph를 바탕으로 매번 미세먼지 좌표를 구하여 확산 함수에 전달.
        fine_dust = find_fine_dust(graph)
        dust_diffusion(fine_dust)
        air_cleaning(air_cleaner_pos)


if __name__ == "__main__":
    R, C, T = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(R)]
    air_cleaner_pos = init_location(graph)

    cleaning_circulation(graph, air_cleaner_pos, T)

    print(sum(map(sum, graph[:])))