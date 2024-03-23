import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())


set_list = list(set(lst))
set_list.sort()
set_list.sort(key=len)

# 흠...이거 length를 안써도 출력이 되다니 이상해
for word in set_list:
    print(word)
