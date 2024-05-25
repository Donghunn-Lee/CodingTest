# 소가 길을 건너간 이유 6

# 길이 어떻게 되는건지 처음엔 이해가 잘 안돼서 좀 해멨던 문제.
# 길은 칸으로 구분 하는 것이 아니라, 두 점의 연결로 묶어 생각해야했음. 그 부분을 제외하면 평범.

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    deq = deque()
    visited_cow = set() # 소를 하나씩 이동시킬 것이므로, 이전에 이동시켰던 소를 체크.
    count = 0   # 길을 건너야만 만날 수 있는 소 쌍의 수

    # 소를 한 마리씩 이동시키며 탐색.
    for i in range(len(cows)):
        deq.append(cows[i])
        visited_graph = set()
        visited_graph.add(cows[i])
        visited_cow.add(cows[i])
        
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

                    deq.append((ni, nj))
                    visited_graph.add((ni, nj))
        
        # 현재 소부터 아직 탐색하지 않은 소들 간의 접촉 여부를 체크.
        for i, j in cows[i + 1:]:
            if (i, j) not in visited_graph:
                count += 1

    return count


if __name__ == "__main__":
    N, K, R = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]

    road = dict()
    for _ in range(R):
        a, b, c, d = map(int, input().split())

        if (a, b) in road:
            road[(a, b)].add((c, d))
        else:
            road[(a, b)] = {(c, d)}

        if (c, d) in road:
            road[(c, d)].add((a, b))
        else:
            road[(c, d)] = {(a, b)}

    cows = [tuple(map(int, input().split())) for _ in range(K)]

    print(bfs())
