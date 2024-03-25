import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline
n = int(input())
arr1=list(map(int,input().split()))
m = int(input())
arr2   =list(map(int,input().split()))
arr1.sort()
for x in arr2:
    right_index = bisect_right(arr1, x) 
    left_index = bisect_left(arr1, x) 
    if right_index > left_index: 
        print(1)
    else: 
        print(0)
