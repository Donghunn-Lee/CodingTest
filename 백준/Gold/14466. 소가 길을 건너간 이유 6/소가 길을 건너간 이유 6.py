# 소가 길을 건너간 이유 6

# 길이 어떻게 되는건지 처음엔 이해가 잘 안돼서 좀 해멨던 문제.
# 길은 칸으로 구분 하는 것이 아니라, 두 점의 연결로 묶어 생각해야했음. 그 부분을 제외하면 평범.
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    deq = deque()
    visited_cow = set() # 소를 하나씩 이동시킬 것이므로, 이전에 이동시켰던 소를 체크.
    total, non_road = 0, 0  # 만날 수 있는 모든 소의 쌍, 길을 건너지 않고 만날 수 있는 소의 쌍.
    
    # 모든 경우의 수를 먼저 계산.
    # 이후 건너지 않고 만날 수 있는 쌍을 차감해서 길을 건너야만 하는 쌍의 수를 도출.
    for i in range(1, K):
        total += i

    # 소를 한 마리씩 이동시키며 탐색.
    for cow in cows:
        deq.append(cow)
        visited_graph = set()
        visited_graph.add(cow)
        visited_cow.add(cow)
        
        # bfs반복
        while deq:
            ci, cj = deq.popleft()

            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni, nj = ci + di, cj + dj

                if 0 < ni <= N and 0 < nj <= N and (ni, nj) not in visited_graph:

                    # 현재 방문한 목초지가 길이 있는 점이며, 그 길이 이전 목초지에서 이어진 길인 경우,
                    # 현재의 방문은 길을 건너온 셈이 되므로 continue.
                    if (ni, nj) in road and (ci, cj) in road[(ni, nj)]:
                        continue

                    # 길이 없는 목조치이거나 길이 있지만 건너지 않았으며,

                    # 현재 방문한 목초지에 소가 있고 그 소가 아직 탐색한 적 없는 소인 경우, non_road += 1.
                    if (ni, nj) in cows and (ni, nj) not in visited_cow:
                        non_road += 1

                    deq.append((ni, nj))
                    visited_graph.add((ni, nj))


    return total - non_road


if __name__ == "__main__":
    N, K, R = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]

    # 번거롭지만 in 을 사용할 때의 시간복잡도를 줄이기 위해 길과 소의 좌표를 dict와 set을 사용해 저장.
    road = dict()
    for _ in range(R):
        a, b, c, d = map(int, input().split())

        if (a, b) in road:
            road[(a, b)].add((c, d))
        else:
            road[(a, b)] = {(c, d)}     # 한 목초지에 여러 개의 길이 있을 수 있으므로 set.

        if (c, d) in road:
            road[(c, d)].add((a, b))
        else:
            road[(c, d)] = {(a, b)}

    cows = set()
    for _ in range(K):
        a, b = map(int, input().split())
        cows.add((a, b))

    print(bfs())