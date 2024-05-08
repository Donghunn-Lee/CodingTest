# 양팔저울

# 꽤 어려운 문제중에 간만에 답 찾아보지 않고 푼 문제.
# 물론 최근 swea에서 푼 '가능한 시험 점수' 문제를 풀지 않았다면 이 방법은 분명 떠올리지 못했음.
# dp 테이블을 생성 후 무게 추들을 더한 값을 추가, 갱신된 테이블에 다음 무게 추 값을 더하며 추가를 반복.
# 이 때 어느 쪽 저울이 더 무거운지가 중요한 것이 아니라 같은지 아닌지가 중요하므로,
# 추를 더하기만 하지 않고 빼는(기준 저울의 반대쪽의 놓는 경우) 경우도 계산해줘야 함. 아니면 26%에서 컷.
# 따라서 dp[i] + w 만이 아닌 dp[i] - w의 절댓값도 테이블에 추가.
import sys
input = sys.stdin.readline

def weighing(weights, targets):
    dp = [0]
    visited = [0] * (sum(weights) + 1)  # 특정 무게가 나오는지 아닌지만이 중요. 체크리스트.
    result = {i : 'N' for i in targets} # 구하려는 무게를 알아냈는지 여부를 체크하는 딕셔너리.

    # 주어진 무게추들을 1번씩 반복.
    for w in weights:
        # 갱신된 dp테이블의 현재 길이만큼 반복. 갱신중 테이블 길이가 변하지 않게 하기 위해 len사용.
        for i in range(len(dp)):
            tmp = [dp[i] + w]   # 무게 추를 기준 저울에 올린 경우.
            tmp.append(abs(dp[i] - w))  # 무게 추를 기준 저울의 반대쪽에 올린 경우.
    
            for t in tmp:
                # 처음 구한 값이라면 visited 체크 후 dp에 추가.
                if visited[t] == 0:
                    visited[t] = 1
                    dp.append(t)

                # 방문한 값이면 target 확인 없이 continue.
                else:
                    continue
                
                # 구한 무게가 찾으려는 무게 중에 있다면 해당 값에 Y를 할당.
                # 이 때 in을 써야 하므로, 시간복잡도를 줄이기 위해 리스트가 아닌 집합으로 사용.
                if t in targets:
                    result[t] = 'Y'
    
    # 결과를 저장한 딕셔너리를 리턴.
    return result
            

if __name__ == "__main__":
    N = int(input())
    weights = list(map(int, input().split()))
    M = int(input())
    target_list = list(map(int, input().split()))
    ans = []

    result = weighing(weights, set(target_list))

    # 리턴받은 구하려는 무게의 측정 가능 여부를 사용해 결괏값 출력.
    for t in target_list:
        ans.append(result[t])
    
    print(" ".join(ans))