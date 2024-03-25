import sys

top_list = []
stack = []
answer=[]

def input_data():
    n = int(sys.stdin.readline().rstrip())
    top_list = list(map(int, sys.stdin.readline().split()))
    return top_list, n

def solve(stack, top_list):
    for i in range(len(top_list)):
        while stack:
            if stack[-1][1] > top_list[i]:
                answer.append(stack[-1][0] + 1)
                break
            else:
                stack.pop()
        if not stack:
            answer.append(0)
        stack.append([i, top_list[i]])
    return stack

def print_answer():
    print(" ".join(map(str, answer)))

def main():
    global top_list, stack, answer
    top_list, n = input_data()
    stack = solve(stack, top_list)
    print_answer()

if __name__ == "__main__":
    main()
