# 패션왕 신해빈

# 실버 3 우습게 봤다가 수학적 사고에서 애를 쓴 문제.
# 딕셔너리로 만들긴 했는데 이후 각 원소의 개수를 곱하고 전체 옷의 수를 더했는데 답이 안 나옴. 당연함.
# 해답은 원소의 수, 즉 부위별 의상 수에 + 1을 더해서 곱해줘야 한다는 것. 그 옷을 선택하지 않는 경우의 수를 고려해야 함.
# 따라서 마지막에 -1을 해 주는 이유는 입지 않는 경우가 더해졌으므로, 모든 옷을 입지 않은 경우를 제외해야 하기 때문.
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        N = int(input())
        clothes = dict()
        passion = 1

        # 의상 부위를 키로 딕셔너리 생성.
        for i in range(N):
            name, types = input().rstrip().split()
            if types not in clothes:
                clothes[types] = [name]
            else:
                clothes[types].append(name)

        # 각 부위별 의상 수 + 1을 모두 곱하고, 알몸인 경우를 빼 줌.
        for i in clothes:
            passion *= len(clothes[i]) + 1
        
        ans.append(str(passion - 1))
    
    print("\n".join(ans))
