import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split()) 

deq = deque(range(1, n+1)) 

result = []
while len(deq) != 0:
    for _ in range(k-1):
        deq.append(deq.popleft())  # 왼쪽에서 값을 꺼내는 함수는 popleft() 입니다.
    result.append(str(deq.popleft()))

print('<' + ', '.join(result) + '>')
