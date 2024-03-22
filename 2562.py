import sys

lines = list(map(int, sys.stdin.read().split()))  # 모든 입력을 배열로 받음

max_value = max(lines)  # 최댓값 계산
max_index = lines.index(max_value) + 1  # 최댓값의 인덱스 계산

print(max_value)
print(max_index)

