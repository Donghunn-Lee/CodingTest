# A -> B

# 의외로 조금은 생각을 해야 했던 문제. 실버 2여도 이런 문제는 사고의 범주를 넓힐 수 있을 것 같음.
# 자연스레 a를 b로 만드는 bfs 코드를 짜다가, 연산이 불가능한 경우는 어떻게 해야하는지에서 막힘.
# 좀 고민해보니 a에서 b로 갈 게 아니라 b에서 a로 가야 b가 a 이하가 되는 경우를 제외하며 종료가 가능했음.

import sys
from collections import deque
input = sys.stdin.readline

def change(a, b):
    deq = deque()
    deq.append((b, 1))      # 현재 수와 연산의 수를 deq에 추가.

    while deq:
        num, count = deq.popleft()

        # a보다 작아지면 continue
        if num < a:
            continue

        # a에 도달한 경우, bfs이므로 최단 시간 이므로 count를 리턴.
        if num == a:
            return count

        # 2가 짝수일 때, 2로 나누어 deq에 추가.
        if num % 2 == 0:
            deq.append((num // 2, count + 1))

        # 1의 자리가 1이고 10보다 큰 수인 경우, 1을 빼고 10을 나누어 deq에 추가.
        if num % 10 == 1 and num > 10:
            deq.append(((num - 1) // 10, count + 1))

    # continue 조건을 통해 deq의 원소를 소진하고 a를 발견하지 못한 채 탐색이 종료된 경우 -1를 리턴.
    return -1

if __name__ == "__main__":
    A, B = map(int, input().split())
    print(change(A, B))
