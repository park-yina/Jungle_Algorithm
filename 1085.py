import sys
def input():
    global a, b, c,d
    a, b, c,d = map(int, sys.stdin.readline().split())
def solve(x,y,w,h):
    print(min(x,y,w-x,h-y))
def result():
    input()
    res=solve(a,b,c,d)
    print(res)
result()
