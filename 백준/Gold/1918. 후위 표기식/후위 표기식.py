# 후위 표기식

# 1시간쯤 건드려보다가 스택을 써야하는 것 말고는 그럴싸한 풀이가 떠오르지 않아서 검색.
# 전에 후위 표기식 2인가 하는 문제는 후위 표기식과 피연산자의 값을 줘서 계산하는 문제였는데, 만들려니까 어려움.
# 결국 풀이는 연산자의 우선순위를 정하고, 그에 따라 스택에 넣고 빼 주는 방법.
# 이 정도는 생각했는데, 곱셈과 덧셈의 우선순위 차이를 적절히 구분해서 넣는 것을 나는 구현하지 못했음.

import sys
input = sys.stdin.readline

def postfix(eq):
    stack = []
    result = ''

    # 입력 문자열에 별다른 조작 없이 순서대로 사용.
    for s in eq:

        # 변수라면 바로 추가.
        if s.isalpha():
            result += s

        else:
            # 여는 괄호인 경우는 바로 스택에 추가. 괄호 내부 계산을 우선시 하기 위함.
            if s == '(':
                stack.append(s)
            # *, /인 경우, 보다 낮은 우선순위인 +, - 을 만날 때까지 같은 *, /을 스택에서pop, 결과에 추가.
            elif s == '*' or s == '/':
                while stack and (stack[-1] == '*' or stack[-1] =='/'):
                    result += stack.pop()
                # 스택 내부의 동위 연산자를 다 넣고 현재 연산자도 스택에 추가.
                stack.append(s)
            
            # +, -의 경우엔 스택 전체를, 괄호가 열려있다면 괄호까지의 연산자를 모두 순서대로 pop.
            # 만약 반대로 해서 *, / 일때 이렇게 모두 추가한다면 * 보다 +의 연산이 먼저 이뤄지게 됨.
            elif s == '+' or s == '-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(s)

            # 닫는 괄호가 나오면 여는 괄호까지 모두 pop. 그리고 괄호는 추가하지 않고 여는 괄호도 제거.
            elif s == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()

    # 스택에 남아있는 연산자는 순서대로 pop.
    while stack :
        result+=stack.pop()

    return result


if __name__ == "__main__":
    equation = input().rstrip()

    print(postfix(equation))