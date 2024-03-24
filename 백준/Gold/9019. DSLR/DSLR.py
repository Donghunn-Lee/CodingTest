# DSLR

# 거의 딱 1시간만에 푼 문제. 심지어 처음엔 대충 읽고 DLSR 명령어를 받아서 결과값을 출력하는 줄 알고 헛손질함.
# 알아차리고 다시 읽어보니 bfs로 4가지 명령어를 사용한 경우를 모두 대조해봐야겠다는 생각으로 코드 작성.
# b 값과 일치하도록 하는 명령어 조합이 나오면 저장하고, 계속 나오면 더 길이가 짧은 것을 넣다가 시간초과.
# 생각해보니 결과값이 처음 나오면 그게 최소 명령어임을 인지하고, 맞는 명령어 조합을 찾으면 바로 리턴하니 통과.
# 통과는 했지만 시간을 더 줄일 수 있을 것 같아서 검색해서 더 효율적인 계산식을 참고.
# 또 나처럼 cmd 리스트를 따로 만들지 않고 덱에 숫자와 명령어를 q.append([A, 'D']) 이렇게 더하기도 하던데
# 아무래도 10000 짜리 리스트를 하나 더 쓰는 만큼 내 방법이 더 비효율적이라고 생각함. 하지만 바꾸진 않겠음.

import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    q = deque()
    q.append(a)
    visited = [False] * 10000
    visited[a] = True
    cmd = ['' for _ in range(10000)]
    result = ''

    while q:
        cur = q.popleft()

        d = (cur * 2) % 10000
        s = (cur - 1) % 10000

        # 초기 코드. 앞과 뒤를 바꾸기 위해, 또 앞자리 0을 고려하기 위해 문자열을 만들 생각만 했음.
        # tmp = str(cur)
        # tmp = '0' * (4 - len(tmp)) + tmp
        # l = int(tmp[1:] + tmp[0])
        # r = int(tmp[-1] + tmp[:-1])
        
        # 찾아보니 그냥 자리수만 나누고 더해도 되는 계산임. 내게 조금 더 수학적 사고가 필요했다고 반성함.
        l = cur // 1000 + (cur % 1000)*10
        r = cur // 10 + (cur % 10) * 1000

        # if문을 4 개 나열하는게 조금 더 빠를 거라는 생각은 했지만 너무 안 예뻐서 for문으로 작성.
        for i, j in ((d, 'D'), (s, 'S'), (l, 'L'), (r, 'R')):
             if not visited[i]:
                cmd[i] = cmd[cur] + j

                if i == b:                
                    result = cmd[i]
                    return result
                
                    # 덱에 추가되는 값은 뒤로 들어가고, 빠지는 건 앞에서 빠짐.
                    # 고로 먼저 나오는 답이 최소 명령어 조합인데 그걸 생각 못하고 모든 조합을 확인했었음.
                    # if not result:
                    #     result = cmd[i]
                    # elif len(result) > len(cmd[i]):
                    #     result = cmd[i]
    
                q.append(i)
                visited[i] = True
    
    return result

if __name__ == "__main__":
    T = int(input())
    register = deque([0, 0, 0, 0, 0])
    ans = []

    for _ in range(T):
        A, B = map(int, input().split())
        ans.append(bfs(A, B))
    
    print('\n'.join(ans))