import sys

def solve(li:list[int],n:int,l:int)-> bool:
    sw = [False for _ in range(n)]
    for i in range(n - 1):
        if li[i] == li[i + 1]:
            continue

        if abs(li[i] - li[i + 1]) > 1:
            return False

        if li[i] > li[i + 1]:
            tmp = li[i + 1]
            for j in range(i + 1, i + 1 + l):
                if 0 <= j < n:
                    if li[j] != tmp:
                        return False

                    if sw[j]:
                        return False

                    sw[j] = True

                else:
                    return False

        else:
            tmp = li[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if li[j] != tmp:
                        return False

                    if sw[j]:
                        return False

                    sw[j] = True

                else:
                    return False
    return True

n, l = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0

for i in arr:
    if solve(i,n,l):
        cnt += 1

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(arr[j][i])
    if solve(tmp,n,l):
        cnt += 1

print(cnt)