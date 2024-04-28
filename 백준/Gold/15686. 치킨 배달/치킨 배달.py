# 치킨 배달

# 골드 5치고 꽤 좋은 문제라고 생각함.
# 우선 보자마자 모든 경우의 수를 다 계산해야 하는 브루트포스 문제라고 생각.
# 다만 시간 효율을 위해 집의 위치와 치킨집의 위치를 먼저 다 구하고, 모든 거리를 다 계산한 다음 답을 구해야겠다고 생각.

import sys
sys.setrecursionlimit(10**3)
input = sys.stdin.readline
INF = 1e5

# 집과 치킨집의 좌표를 구해서 저장하는 함수.
def location(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                houses.append((i, j))
            elif graph[i][j] == 2:
                restaurants.append((i, j))

# 각각의 집과 치킨집 사이의 거리를 모두 구해 딕셔너리 형태로 저장하는 함수.
def cal_chicken_dist(houses, restaurants):
    for hi, hj in houses:
        chicken_dist[(hi, hj)] = []
        dist = INF

        for ri, rj in restaurants:
            dist = abs(hi - ri) + abs(hj - rj)
            chicken_dist[(hi, hj)].append(dist)

# M개 까지 치킨집을 고를 수 있는 모든 경우의 수를 구하고, 고른 치킨집과 각 집 사이의 치킨 거리를 계산하는 함수.
def choose_close_down(restaurants, chicken_dist, n, selected, count):
    global ans

    if 0 < count <= M:
        result = 0

        for c in chicken_dist:
            tmp = INF

            for i in selected:
                tmp = min(tmp, chicken_dist[c][i])

            result += tmp

        ans = min(ans, result)
    
    if count == M or n == len(restaurants):
        return

    
    selected.add(n)
    choose_close_down(restaurants, chicken_dist, n + 1, selected, count + 1)
    selected.remove(n)

    choose_close_down(restaurants, chicken_dist, n + 1, selected, count)
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    houses, restaurants = [], []
    chicken_dist = dict()
    ans = INF

    location(graph)
    cal_chicken_dist(houses, restaurants)
    
    choose_close_down(restaurants, chicken_dist, 0, set(), 0)

    print(ans)