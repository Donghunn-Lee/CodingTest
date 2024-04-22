# 숨바꼭질 2

# 전에 이 문제를 dp로 풀었던 기억이 어렴풋이 있어서 당연히 재귀를 이용한 dp로 풀려고 첫 시도.
# 그러나 코드를 써 내려 갈수록 생각 이상으로 코드가 복잡해져서 뭔가 이상하다고 생각.
# 힌트로 알고리즘 분류를 확인. dp가 아니라 bfs였음.
# 돌아가서 가짓수 말고 최소 시간만 구했던 그냥 '숨바꼭질'문제를 찾아 확인해보니, 이 땐 내가 bfs로 풀었음.
# 아무튼 가짓수도 구해야 하는 이번 문제는 dp와 bfs를 같이 사용해야 한다는 사실을 깨달은 뒤는 풀 수 있었음.

# +++ 는 가짓수를 구할 때 초기화 하는 방식에서 조금 더 고민함.
# target에서만 가짓수를 저장하는 것이 아니라 1에서 2로 가는 방법 역시 + 1과 *2가 있다는 걸 고려해야 함.

import sys
from collections import deque
input = sys.stdin.readline
INF = 1e6

def bfs(start, target):
    deq = deque()
    deq.append(start)
    visited = [INF] * 100001    # 최소 시간을 구하기 위한 리스트.
    visited[start] = 0
    ways = 0         # 가짓수를 구하기 위한 리스트.

    # N이 K보다 클 땐 뒤로 1씩 이동하는 수밖에 없음.
    if N > K:
        return N - K, 1
    
    # N과 K가 같으면 이동하지 않아도 되고, 가짓수는 1임.
    if N == K:
        return 0, 1
    
    while deq:
        cur = deq.popleft()

        # 코드 반복을 줄이기 위해 다음 위치를 계산한 리스트를 생성.
        move = [cur - 1, cur + 1, cur * 2]

        for m in move:
            if 0 <= m <= 100000:

                # 다음 위치에 더 적은 시간으로 갈 수 있는 경우, 시간값을 초기화 하고 가짓수를 1로 초기화.
                if visited[m] > visited[cur] + 1:
                    visited[m] = visited[cur] + 1
                    
                    # 이동한 지점이 target이면 덱에 추가하지 않음.
                    if m == target:
                        ways = 1
                    else:
                        deq.append(m)

                # 다음 위치로의 이동하는 시간이 저장된 최소 시간과 같음 == 가짓수가 1개 이상.
                elif visited[m] == visited[cur] + 1:
                    
                    # m이 target이면 +1, 아닌 경우는 target에서의 가짓수를 더해주기 위해 덱에 추가해야함.
                    if m == target:
                        ways += 1
                    else:
                        deq.append(m)

    return visited[target], ways
                

if __name__ == "__main__":
    N, K = map(int, input().split())
    
    ans = bfs(N, K)

    print("\n".join(map(str, ans)))
