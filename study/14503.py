import sys

def solve(n:int,m:int,start:(int,int),sd:int,data:list[list:int])->int:
    d = [[-1,0],[0,1],[1,0],[0,-1]]
    answer = 0
    x,y = start
    while True:
        if data[x][y] == 0:
            data[x][y] = -1
            answer += 1
        for _ in range(4):
            sd = (sd + 3) % 4
            tx,ty = x+d[sd][0],y+d[sd][1]
            if 0 <= tx < n and 0 <= ty < m and data[tx][ty] == 0:
                x,y = tx,ty
                break
        else:
            tx,ty = x-d[sd][0],y-d[sd][1]
            if 0 <= tx < n and 0 <= ty < m and data[tx][ty] <= 0:
                x,y = tx,ty
            else: break
    return answer


n,m = map(int,sys.stdin.readline().split())
x,y,d = map(int,sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
print(solve(n,m,(x,y),d,data))
