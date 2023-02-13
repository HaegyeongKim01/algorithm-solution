stack = list()

def solution():
    command = input()
    #push는 한 줄에 두 개 입력 받음  
    if len(command.split(' ')) > 1:
        _, n = command.split(' ')
        stack.append(int(n))
    else:
        if len(stack) > 0:
            pop_elem = stack.pop()
            print(pop_elem)
        else:
            print(-1)

if __name__ == "__main__":
    num = int(input())
    for _ in range(num):
        solution()
