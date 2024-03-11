# 후위 표기식2
import sys
input = sys.stdin.readline

# 후위 표기식이 뭔지 몰라서 검색해서 방법을 알고 난 후 푼 문제.
# 피연산자와 전체 식을 입력받아 계산한 값을 리턴하는 함수.
def postfix(operand, equation):
    stack = []    # 계산할 숫자들을 넣어두는 스택.
    variables = dict()  # 식의 변수에 맞는 값을 할당할 딕셔너리.

    for i in equation:
        if i  == '+':
            # 두 값을 계산 후 그 결과도 다시 마지막 인덱스에 남아있어야 함.
            # stack[-2], pop, 그리고 [-1]에 할당 순으로 실행되어 [1, 2, 3]에서 * 인 경우 [1, 6].
            stack[-1] = stack[-2] + stack.pop()
        elif i  == '-':
            stack[-1] = stack[-2] - stack.pop()
        elif i  == '*':
            stack[-1] = stack[-2] * stack.pop()
        elif i  == '/':
            stack[-1] = stack[-2] / stack.pop()
        else:
            # i가 변수라면 variables에 있는지 먼저 확인.
            # 없다면 i를 key, 피연산자pop의 결과를 value로 하여 딕셔너리에 저장후 스택에도 추가.
            # 같은 변수가 식에서 다수 등장할 경우 때문에 딕셔너리를 사용함.
            if i not in variables:
                variables[i] = operand.pop()
                stack.append(variables[i])
            else:
                # 이미 있는 경우 그대로 스택에 추가.
                stack.append(variables[i])
    
    return stack[0]

if __name__ == "__main__":
    N = int(input())
    equation = input().rstrip()

    # 입력 후 reverse 하는 것보다 입력시 바로 역순 할당하는 게 조금 더 빠를 거라고 생각함. 맞는진 모름.
    operand = [0] * N
    for i in range(N - 1, -1, -1):
        operand[i] = int(input())

    # 자리수 출력은 처음 해보는 것 같은데, format을 사용해 {:.(원하는 자리수)f} 형태로 사용 가능.
    print(f"{postfix(operand, equation):.2f}")