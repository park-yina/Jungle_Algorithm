import sys
input = sys.stdin.readline


n = int(input())
list=lst = [int(input()) for _ in range(n)]
print(sorted(list),sep="\n")
