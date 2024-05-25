# 소가 길을 건너간 이유 6

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    deq = deque()
    visited_cow = set()
    total = 0
    non_road = 0
    
    for i in range(1, K):
        total += i

    for cow in cows:
        deq.append(cow)
        visited_graph = set()
        visited_graph.add(cow)
        visited_cow.add(cow)
        
        while deq:
            ci, cj = deq.popleft()

            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni, nj = ci + di, cj + dj

                if 0 < ni <= N and 0 < nj <= N and (ni, nj) not in visited_graph:
                    if (ni, nj) in road and (ci, cj) in road[(ni, nj)]:
                        continue

                    if (ni, nj) in cows and (ni, nj) not in visited_cow:
                        non_road += 1

                    deq.append((ni, nj))
                    visited_graph.add((ni, nj))


    return total - non_road


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

    cows = set()
    for _ in range(K):
        a, b = map(int, input().split())
        cows.add((a, b))

    print(bfs())
