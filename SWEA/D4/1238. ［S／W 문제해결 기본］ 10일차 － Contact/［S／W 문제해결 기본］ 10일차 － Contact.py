# Contact

# 길어야 30분이면 풀 수 있었던 문제를 이해를 살짝 잘못한 탓으로 1시간 20분이 걸려버림.
# 그 실수는 이 문제를 단순히 가장 많은 연락을 거친 마지막 노드를 찾고, 그 최댓값을 저장하는 문제로 이해한 것임.
# 예제에선 이 경우를 분명하게 설명하고 있음.

# "비상연락망이 가동되면 아래 그림과 같이 연락을 시작하는 당번인 2번은 연락 가능한 7번과 15번에 동시에 연락을 취한다 (다자 간 통화를 사용한다고 가정)."

# 처음의 난 이 부분을 잘못 이해해서 dfs나 bfs 둘 다 상관 없다고 생각하고, 더 의미에 적합하다고 생각한 dfs를 사용함.
# 그런데 깊이 우선 탐색인 dfs에서 발생한 문제점은 아래와 같음.

# 1 : {2, 3, 4}, 2 : {5}, 5 : {3} 이런 연락망이 주어졌고, 시작점이 1이라고 가정.
# 다자 간 통신을 사용하므로 1에서는 2와 3, 4에 동시에 연락을 함. 때문에 2, 3, 4 사이에선 연락을 할 수 없음.
# 하지만 dfs를 사용하면, 1 -> 2 -> 5 -> 3 이렇게 2가 5로 우회해서 2와 3이 연결되는 경우가 발생하고, depth가 깊어짐.
# 이 문제는 방문 체크를 하고 백트래킹을 사용해도 해결할 수 없었음.

# 아 근데 되겠네. 지금 생각난 건데 dfs를 굴릴 때 재귀호출을 하기 이전에 현재 번호와 연결된 번호를 모두 visited에 집어넣으면 해결 되는 문제였음. 다자 간 통신이라는 걸 조금 더 빨리 깨달았다면 dfs로도 풀 수 있었을 것임.
# 다만 bfs를 쓰면 이미 다자 간 통신이 지원되는 셈이므로 다른 동작을 더 넣지 않아도 됌.

# 아무튼 어려운 문제도 아니었는데 문제를 너무 쉽게 봐서 오래 걸린 경우였음.

from collections import deque

def bfs(start):
    deq = deque()
    deq.append((start, 0))
    visited = {start}
    max_depth, num = 0, 0

    while deq:
        cur, depth = deq.popleft()

        if max_depth < depth:
            max_depth = depth
            num = cur
        
        elif max_depth == depth:
            num = max(num, cur)

        for nxt in graph[cur]:
            if nxt not in visited:
                deq.append((nxt, depth + 1))
                visited.add(nxt)
    
    return num
        

if __name__ == "__main__":
    ans = []

    for t in range(1, 11):
        length, start = map(int, input().split())
        input_data = list(map(int, input().split()))
        graph = {i : set() for i in range(1, 101)}

        for i in range(0, length, 2):            
            graph[input_data[i]].add(input_data[i + 1])

        ans.append(f'#{t} {bfs(start)}')
    
    print("\n".join(ans))