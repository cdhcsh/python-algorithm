import sys

def solve(gears:list[list[str]],commands:list[list[int]]) -> int:
    def rotate(gear:list,d:int)->None:
        if d == 1:
            gear.insert(0,gear.pop())
        elif d == -1:
            gear.append(gear.pop(0))

    left,right = 6,2
    for command in commands:
        n = command[0]-1
        d = command[1]
        directions = [0,0,0,0]
        directions[n] = d
        for i in range(n-1,-1,-1):
            if directions[i+1] == 0:
                break
            if gears[i+1][left] != gears[i][right]:
                directions[i] = -directions[i+1]
        for i in range(n+1,4):
            if directions[i-1] == 0:
                break
            if gears[i-1][right] != gears[i][left]:
                directions[i] = -directions[i-1]
        for i,d in enumerate(directions):
            rotate(gears[i],d)
    answer = 0
    for i,gear in enumerate(gears):
        answer += int(gear[0]) * (2**i)
    return answer

gears = [list(sys.stdin.readline().strip()) for _ in range(4)]
commands = [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
print(solve(gears,commands))