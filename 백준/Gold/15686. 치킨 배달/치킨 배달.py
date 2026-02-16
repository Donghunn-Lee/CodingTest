import sys
from itertools import combinations

input = sys.stdin.readline
INF = 10**9

def get_locations(board):
    houses = []
    chickens = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                houses.append((i, j))
            elif board[i][j] == 2:
                chickens.append((i, j))
    return houses, chickens


def calc_city_chicken_distance(houses, selected_chickens):
    total = 0
    for hx, hy in houses:
        min_dist = INF
        for cx, cy in selected_chickens:
            min_dist = min(min_dist, abs(hx - cx) + abs(hy - cy))
        total += min_dist
    return total


# main
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

houses, chickens = get_locations(board)

answer = INF
for selected in combinations(chickens, M):
    dist = calc_city_chicken_distance(houses, selected)
    answer = min(answer, dist)

print(answer)
