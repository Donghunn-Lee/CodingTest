# 단어 정렬

import sys
input = sys.stdin.readline

def word_sort(words):
    words.sort(key = lambda x : (len(x), x))
    tmp = set()
    ans = []

    for i in words:
        if i not in tmp:
            tmp.add(i)
            ans.append(i)

    return "\n".join(ans)

if __name__ == "__main__":
    N = int(input())
    words = [input().rstrip() for _ in range(N)]

    print(word_sort(words))