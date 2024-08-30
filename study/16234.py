import sys

def solve(N:int,L:int,R:int,cities:list[list[int]])->int:
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    q = []
    answer = 0
    while 1:
        change = True
        visit = [(int,int)]
        for i in range(N):
            for j in range(N):
                if (i,j) not in visit:
                    sum = 0
                    group = [(i,j)]
                    sum += cities[i][j]
                    q.append((i,j))
                    visit.append((i,j))
                    while q:
                        x,y = q.pop(0)
                        for tx,ty in d:
                            nx,ny = x+tx,y+ty
                            if (not (0 <= nx < N and 0 <= ny < N)
                                    or (nx,ny) in visit
                                    or (nx,ny) in group
                            ):
                                continue
                            c = abs(cities[x][y] - cities[nx][ny])
                            if L > c or R < c:
                                continue
                            group.append((nx,ny))
                            sum += cities[nx][ny]
                            visit.append((nx,ny))
                            q.append((nx,ny))
                    sum //=len(group)
                    for x,y in group:
                        cities[x][y] = sum
                    if len(group) > 1:
                        change = False

        if change:
            break
        else:
            answer += 1
    return answer

N,L,R = map(int,sys.stdin.readline().split())
cities = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
print(solve(N,L,R,cities))