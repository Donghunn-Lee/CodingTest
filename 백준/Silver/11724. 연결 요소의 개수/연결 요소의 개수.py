import sys
input = sys.stdin.readline

node, edge = map(int, input().split())
seqnum = [0] * (node+1)
seq = 1
ans = node

for _ in range(edge):
    if ans==1:
        input()
        continue
    valid = True
    a, b = map(int, input().split())
    if seqnum[a]==0 and seqnum[b]==0:
        seqnum[a] = seqnum[b] = seq
        seq += 1
    elif seqnum[a]==0:
        seqnum[a] = seqnum[b]
    elif seqnum[b]==0:
        seqnum[b] = seqnum[a]
    else:
        if seqnum[a]==seqnum[b]:
            valid = False
        else:
            low_s = min(seqnum[a], seqnum[b])
            high_s = max(seqnum[a], seqnum[b])
            for i in range(1, node+1):
                if seqnum[i]==high_s:
                    seqnum[i] = low_s
    # print(seqnum) ###
    if valid:
        ans -= 1

print(ans)