# 오등큰수
import sys
input = sys.stdin.readline

# 오큰수 문제와 거의 동일한 구조로 풀이
# 값을 그대로 사용하는 대신 원소의 빈도수로 계산하면 간단함
def cal_NGE(seq, fre):
    result = [-1 for _ in range(N)]
    stack = [[0, fre[seq[0]]]]

    # 수열의 인덱스와 값을 사용해 빈도수를 비교
    # 최근 빈도수보다 지금 j의 빈도수가 더 적거나 같을 경우 스택에 쌓음
    # 오등큰수가 나타나면 스택 안의 수에 대해서도 오등큰수인지 비교하고 result에 저장
    for i, j in enumerate(seq):
        if stack and stack[-1][1] < fre[j]:
            for k in range(len(stack) - 1, -1, -1):
                if stack[k][1] < fre[j]:
                    result[stack[k][0]] = j
                    stack.pop()
                else:
                    break

        # 지금은 j와 이전 스택과의 비교이므로 계산 후에는 스택에 j도 넣어줘야 함
        stack.append([i, fre[j]])

    return ' '.join(map(str, result))


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    tmp = set(A)
    F = dict()

    # 집합으로 중복을 없앤 후, 이것을 키로 딕셔너리를 생성
    # count를 사용하면 O(N^2) 인 반면 이 방법이면 O(2N)으로 빈도수를 계산할 수 있음
    for i in tmp:
        F[i] = 0

    for i in A:
        F[i] += 1
    
    print(cal_NGE(A, F))