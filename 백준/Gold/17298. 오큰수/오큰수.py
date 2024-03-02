# 오큰수
import sys
input = sys.stdin.readline

# 수열 seq을 입력받아 각 원소의 NGE를 계산하여 반환하는 함수.
def NGE(seq):
    stack = [[0, seq[0]]]
    result = [0 for _ in range(len(seq))]

    # stack은 seq의 index와 value를 가짐.
    for i, j  in enumerate(seq):
        # stack에 마지막으로 넣은 원소보다 j가 더 큰 경우
        # stack 오른쪽에서부터 j보다 작은 값들을 확인하고 result의 해당 위치에 j값을 할당.
        # 사용한 stack 요소는 pop.
        if stack and stack[-1][1] < j:
            for k in range(len(stack) - 1, -1, -1):
                if stack[k][1] < j:
                    result[stack[k][0]] = j
                    stack.pop()
                else:
                    break
        # j가 아닌 j직전까지의 원소에 대한 NGE를 찾은 것이므로 stack에 추가.
        stack.append([i,j])

    # stack에서 사용되지 않고 남아있는 원소와 비교 대상이 없는 마지막 원소는 NGE가 없으므로 -1을 할당.
    for i, j in stack:
        result[i] = -1
    
    return ' '.join(map(str, result))

if __name__ == "__main__":
    N = int(input())
    sequnce_A = list(map(int, input().split()))

    print(NGE(sequnce_A))