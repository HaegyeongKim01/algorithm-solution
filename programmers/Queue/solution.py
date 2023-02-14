from queue import Queue
que = Queue()

def solution():
    cmd = input()
    #push 
    if len(cmd.split(' ')) > 1:
        _, n = cmd.split(' ')
        n = int(n)
        que.put(n)
    #pop
    else:
        if que.empty():
            print(-1)
        else:
            print(que.get())
        
def main():
    num = int(input())
    for _ in range(num):
        solution()

if __name__ =="__main__":
    main()