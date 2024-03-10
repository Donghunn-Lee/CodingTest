# 접미사 배열

def subffix(s):
    sfx = []

    for i in range(len(s)):
        sfx.append(s[i:])
    
    return sorted(sfx)


if __name__ == "__main__":
    S = input().rstrip()

    result = subffix(S)
    print('\n'.join(result))