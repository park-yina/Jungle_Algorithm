def find_combination(array, target_sum, current_sum, idx, combination):
    if len(combination) == 7:  # 조합의 길이가 7인 경우
        if current_sum == target_sum:  # 합이 목표 합과 일치하는지 확인
            for num in combination:
                print(num)
            exit()  # 찾았으므로 종료
        return

    if idx == len(array):  # 모든 원소를 확인한 경우
        return

    # 현재 원소를 선택하는 경우
    combination.append(array[idx])
    find_combination(array, target_sum, current_sum + array[idx], idx + 1, combination)
    combination.pop()  # 재귀 호출 이후에는 해당 원소를 다시 제거하여 다른 경우를 확인

    # 현재 원소를 선택하지 않는 경우
    find_combination(array, target_sum, current_sum, idx + 1, combination)


array = []
for i in range(9):
    array.append(int(input()))

array.sort()
find_combination(array, 100, 0, 0, [])
