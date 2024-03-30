#공백으로 입력받기
#a,b,v=map(int,input().split())
#command와 해야할 숫자가 공백으로 주어지는 스택
# import sys
# n = int(sys.stdin.readline())

# stack=[]
# for i in range(n):
#     command = sys.stdin.readline().split()
#     if(command[0]=='push'):
#         stack.append(command[1])
#     elif(command[0]=='pop'):
#         if(len(stack)==0):
#             print("-1")
#         else:
#             print(stack.pop())
#     elif(command[0]=='size'):
#         print(len(stack))
#     elif(command[0]=='empty'):
#         if(len(stack)==0):print("1")
#         else:print("0")
#     elif(command[0]=='top'):
#         if(len(stack)==0):
#             print("-1")
#         else:
#             print(stack[-1])

# 스택 기본 구현 코드
# def push(stack, x):
#     stack.append(x)

# def pop(stack):
#     if len(stack) == 0:
#         print(-1)
#     else:
#         print(stack.pop())

# def size(stack):
#     print(len(stack))

# def empty(stack):
#     if len(stack) == 0:
#         print(1)
#     else:
#         print(0)

# def top(stack):
#     if len(stack) == 0:
#         print(-1)
#     else:
#         print(stack[-1])

# input = sys.stdin.readline

# N = int(input())
# stack = []

# for _ in range(N):
#     command = input().split()
#     if command[0] == 'push':
#         push(stack, int(command[1]))
#     elif command[0] == 'pop':
#         pop(stack)
#     elif command[0] == 'size':
#         size(stack)
#     elif command[0] == 'empty':
#         empty(stack)
#     elif command[0] == 'top':
#         top(stack)


#데크 구현 템플릿

# import sys
# from collections import deque

# def push(queue, x):
#     queue.append(x)

# def pop(queue):
#     if len(queue) == 0:
#         print(-1)
#     else:
#         print(queue.popleft())

# def size(queue):
#     print(len(queue))

# def empty(queue):
#     if len(queue) == 0:
#         print(1)
#     else:
#         print(0)

# def front(queue):
#     if len(queue) == 0:
#         print(-1)
#     else:
#         print(queue[0])

# def back(queue):
#     if len(queue) == 0:
#         print(-1)
#     else:
#         print(queue[-1])

# input = sys.stdin.readline

# N = int(input())
# queue = deque()

# for _ in range(N):
#     command = input().split()
#     if command[0] == 'push':
#         push(queue, int(command[1]))
#     elif command[0] == 'pop':
#         pop(queue)
#     elif command[0] == 'size':
#         size(queue)
#     elif command[0] == 'empty':
#         empty(queue)
#     elif command[0] == 'front':
#         front(queue)
#     elif command[0] == 'back':
#         back(queue)

# 일곱난쟁이(앞에랑 비교해서 인덱스 늘리기)기본코드
# def find_combination(array, target_sum):
#     array.sort()
#     for i in range(len(array)):
#         current_sum = array[i]
#         combination = [array[i]]
#         for j in range(i + 1, len(array)):
#             current_sum += array[j]
#             combination.append(array[j])
#             if len(combination) == 7 and current_sum == target_sum:
#                 for num in combination:
#                     print(num)
#                 return
#             elif current_sum > target_sum:
#                 break

# array = []
# for i in range(9):
#     array.append(int(input()))

# find_combination(array, 100)

# 직접 구현한 이진탐색


# target = 25
# m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
# length = len(m_list)

# m_list.sort()
# left = 0 
# right = length-1

# while left<=right:
#     mid = (left+right)//2
#     if m_list[mid] == target:
#         print(mid+1)
#         break
#     elif m_list[mid]>target:
#         right = mid-1
#     else :
#         left = mid+1