import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    towers = list(map(int, input().split()))

    stack = []
    result = []

    for i, h in enumerate(towers, 1):
        while stack and stack[-1][1] < h:
            stack.pop()

        if stack:
            result.append(stack[-1][0])
        else:
            result.append(0)

        stack.append((i, h))

    print(*result)

solve()