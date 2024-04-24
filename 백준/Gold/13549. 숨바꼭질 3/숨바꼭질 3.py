# 숨바꼭질 3

# 분명 숨바꼭질 시리즈를 두 개 이상 풀어봤는데 조건이 조금만 달라져도 쉽게 풀지 못하는 내가 한심할 뿐.
# 이번 문제는 순간이동의 소요시간이 0초라는 조건이 더해짐.
# 그래서 처음엔 k를 2로 나누어가며 나온 수들을 집합에 넣고 그 안의 수가 나오면 점프하는 식으로 하려고 했으나,
# 2로 나눈다고 그 다음 수도 2로 나누어 떨어지는 게 아니라는 단순한 것도 생각하지 못 할 정도로 머리가 굳어 있었음.
# 정처기를 공부 해야 하므로 빠르게 검색.

# 해법은 INF값이 아닌 0값을 리스트에 넣고, 2배수로 순간이동을 할 때 그 값을 appendleft로 넣는 것.
# deque는 많이 써 봤지만 appendleft는 처음 써 봄. 너비 우선으로 도는 중간에 깊이 우선을 섞는 느낌인가?
# 그렇게 입력값의 배수들이 deq에서 비교적 먼저 꺼내지게 되고, 그 수 들에서도 +1과 -1 이동 역시 계산됨.
# 이처럼 해야 시간 초과와 메모리 초과 없이 답을 구할 수 있음.
import sys
from collections import deque
input = sys.stdin.readline
LIMIT = 100001

def bfs(start, target):
    deq = deque()
    time = [0] * LIMIT
    zero_start = 0

    # start가 target보다 큰 경우, -1씩 더해 target까지 갈 수밖에 없음.
    if start >= target:
        return start - target

    # start가 0이면 배수를 할 수 없으므로 1에서부터 시작. 이후 결과값에 시간 1을 더해줌.
    if start == 0:
        deq.append(1)
        zero_start = 1
    else:
        deq.append(start)

    while deq:
        cur = deq.popleft()

        if cur == target:
            return time[cur] + zero_start

        # 조건의 순서는 중요하게 생각하지 않았는데, cur - 1보다 cur + 1을 먼저 넣게 될 경우엔 4 6이 반례로 등장함.
        # if문으로 target에 도달하자마자 리턴하도록 해 놓았기 때문에,
        # cur + 1이 먼저 들어갈 경우 4 -> 5 -> 6이 4 -> 3 -> 6보다 먼저 실행되어 1이 아닌 2가 출력됨.
        for nxt in (cur - 1, cur + 1, cur * 2):

            # bfs에선 처음 값에 방문 했을 때가 최소 시간(비용)이므로, time[nxt] == 0 조건을 달아 무한 루프 제거.
            if 0 <= nxt < LIMIT and time[nxt] == 0:
                if nxt == cur * 2:
                    time[nxt] = time[cur]
                    deq.appendleft(nxt)
                else:
                    time[nxt] = time[cur] + 1
                    deq.append(nxt)


if __name__ == "__main__":
    N, K = map(int, input().split())

    print(bfs(N, K))