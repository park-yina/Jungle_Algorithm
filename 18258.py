import sys
from collections import deque

def push(queue, x):
    queue.append(x)

def pop(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.popleft())

def size(queue):
    print(len(queue))

def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])

input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        push(queue, int(command[1]))
    elif command[0] == 'pop':
        pop(queue)
    elif command[0] == 'size':
        size(queue)
    elif command[0] == 'empty':
        empty(queue)
    elif command[0] == 'front':
        front(queue)
    elif command[0] == 'back':
        back(queue)



