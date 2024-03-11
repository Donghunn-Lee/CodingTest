# 후위 표기식2
import sys
input = sys.stdin.readline

def postfix(operand, equation):
    num = []
    variables = dict()

    for i in equation:
        if i  == '+':
            num[-1] = num[-2] + num.pop()
        elif i  == '-':
            num[-1] = num[-2] - num.pop()
        elif i  == '*':
            num[-1] = num[-2] * num.pop()
        elif i  == '/':
            num[-1] = num[-2] / num.pop()
        else:
            if i not in variables:
                variables[i] = operand.pop()
                num.append(variables[i])
            else:
                num.append(variables[i])
    
    return num[0]

if __name__ == "__main__":
    N = int(input())
    equation = input().rstrip()
    operand = [0] * N

    for i in range(N - 1, -1, -1):
        operand[i] = int(input())

    print(f"{postfix(operand, equation):.2f}")