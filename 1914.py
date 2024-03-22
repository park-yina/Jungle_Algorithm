import sys
def hanoi_cnt(n,start,end):
    if n==1:
        print(start,end)
        return
    else:hanoi_cnt(n-1,start,6-start-end)
    print(start,end)
    hanoi_cnt(n-1, 6-start-end, end) # 3단계
n=int(sys.stdin.readline())
if(n>20):
    print(2**n-1)
else:
    print(2**n-1)
    hanoi_cnt(n,1,3)