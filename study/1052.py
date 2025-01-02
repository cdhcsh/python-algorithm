import sys

def solve(n:int,k:int)->int:
    res = 0
    while bin(n).count('1') > k:
        i = bin(n)[::-1].index('1')
        res += 2 ** i
        n += 2 ** i
    return res

if __name__ == '__main__':
    n,k = map(int,sys.stdin.readline().split())
    print(solve(n,k))