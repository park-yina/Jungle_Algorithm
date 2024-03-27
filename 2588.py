import sys

class Mul:
    def util():
        input_data = sys.stdin.readline()
        return input_data

    def read():
        global n, m,num_list
        n = int(input())
        m = int(input())
        num_list = list(map(int, str(m)))


    def solve():
        one = n * num_list[0]
        two = (n *num_list[1])
        three = n * num_list[2]
        result = one+two+three
        return one, two, three, result

class Print:
    def print_values(one, two, three, result):
        print(one)
        print(two)
        print(three)
        print(result)

# 입력을 받고
Mul.read()
# 값을 계산하고
one, two, three, result = Mul.solve()
# 결과를 출력합니다.
Print.print_values(one, two, three, result)

