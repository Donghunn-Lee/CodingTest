# 열쇠

# 그래프 탐색 문제임을 확인하고, 처음엔 bfs와 dfs 둘 다 가능한 듯 보여 dfs로 코드를 작성.
# 하지만 재귀 깊이 한계를 늘리면 될 줄 알았는데 IDE에서도 재귀를 끝까지 돌리지 못함.
# 이후 코드를 거의 그대로 가지고 bfs로 변경.
# 16%에서 계속 틀려서 뭘 고려하지 못했는지 찾다가 결국 찾아 냄. 같은 문이 여러 개 있을 때 문을 하나만 저장함.
# 또 처음엔 가장자리의 범위를 지정해 탐색을 진행했는데, 패딩을 추가해서 한 번에 탐색하도록 하는 방법이 있어 채용함.

# 다른 코드를 보면 열쇠 발견시 visited를 초기화하고 다시 탐색했던데 나는 처음부터 문 정보를 저장하는 방법을 사용함.
# 문을 발견한 경우, 맞는 열쇠가 있다면 사용해서 문을 통과해 탐색하고, 없다면 문 정보를 딕셔너리에 저장함.
# 이후 열쇠를 발견했을 때, 방문한 문들 중 열쇠에 맞는 문이 있다면 해당 좌표를 deq에 넣어 문을 통과해 탐색을 진행.
# 이 방법을 사용해 visited를 초기화할 필요가 없으므로 초기화하는 코드의 3할 수준으로 시간 단축.

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    deq = deque()
    deq.append((0, 0))      # 패딩을 추가했으므로 가장자리 아무데서나 시작 가능.
    visited = [[0] * (W + 2) for _ in range(H + 2)]
    visited[0][0] = 1
    count = 0

    while deq:
        ci, cj = deq.popleft()

        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj

            # 이미 방문했거나 벽이 아닌 경우.
            if 0 <= ni < H + 2 and 0 <= nj < W + 2 and not visited[ni][nj] and building[ni][nj] != '*':
                nxt = building[ni][nj]

                # 빈 공간이면 deq에 추가.
                if nxt == '.':
                    deq.append((ni, nj))
                
                # 문서를 찾은 경우 count += 1, deq에 추가.
                elif nxt == '$':
                    count += 1
                    deq.append((ni, nj))
                
                # 문을 찾은 경우
                elif 65 <= ord(nxt) <= 90:
                    # 맞는 열쇠가 있는지 확인 후 있다면 현 좌표를 deq에 추가.
                    if chr(ord(nxt) + 32) in visited_keys:
                        deq.append((ni, nj))

                    # 맞는 열쇠가 없다면 문의 정보를 딕셔너리에 문 이름을 key, 문 좌표들의 리스트를 deq으로 추가.
                    else:
                        if visited_door.get(nxt):
                            visited_door[nxt].append((ni, nj))
                        else:
                            visited_door[nxt] = [(ni, nj)]

                # 열쇠를 찾은 경우
                elif 97 <= ord(nxt) <= 122:
                    # 열쇠는 그냥 지나갈 수 있으므로 찾은 열쇠를 집합에 저장 후 좌표를 deq에 추가.
                    visited_keys.add(nxt)
                    deq.append((ni, nj))
                    
                    # 이 때 방문했던 문들을 확인하여 열쇠에 맞는 문이 있는 경우, 해당 문의 좌표를 deq에 추가.
                    if visited_door.get(chr(ord(nxt) - 32)):
                        for t_ni, t_nj in visited_door[chr(ord(nxt) - 32)]:                        
                            deq.append((t_ni, t_nj))
                    
                visited[ni][nj] = 1
    
    return str(count)


if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        H, W = map(int, input().split())
        building = ['.' + input().rstrip() + '.' for _ in range(H)]
        building = ['.' * (W + 2)] + building + ['.' * (W + 2)]
        visited_door, visited_keys = dict(), set()
        keys = list(input().rstrip())
        for k in keys:
            visited_keys.add(k)

        ans.append(bfs())
    
    print("\n".join(ans))
