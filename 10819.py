import sys
from itertools import permutations
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
per=permutations(arr)
answer=0
for i in per:
    temp=0
    for j in range(1,n):
        temp+=abs(i[j]-i[j-1])
        if answer<temp:
            answer=temp
print(answer)
