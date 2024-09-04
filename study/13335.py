import sys

def solve(w:int,l:int,trucks:list[int])->int:
    weight = 0
    bridge = [-1]*w
    time = 1
    def _pop(bridge:list[int]):
        nonlocal weight,trucks,time
        time += 1
        v = bridge.pop()
        if v != -1:
            weight -= trucks[v]

    for t in range(len(trucks)):
        while weight+trucks[t] > l or bridge[0] != -1:
            _pop(bridge)
            bridge.insert(0,-1)
        bridge[0]=t
        weight += trucks[t]

    while weight > 0:
        _pop(bridge)
    return time


n,w,l = map(int,sys.stdin.readline().split())
trucks = list(map(int,sys.stdin.readline().split()))
print(solve(w,l,trucks))