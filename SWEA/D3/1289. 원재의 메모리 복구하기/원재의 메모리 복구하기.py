# 원재의 메모리 복구하기

def restore(data):
    if data[0] == '0':
        count = 0
    else:
        count = 1

    for i in range(len(data) - 1):
        if data[i] != data[i + 1]:
            count += 1

    return count


if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        memory = input().rstrip()

        ans.append(f'#{t} {restore(memory)}')
    
    print("\n".join(ans))