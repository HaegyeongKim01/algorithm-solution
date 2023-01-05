def isPass():
    n, m = map(int, input().split())
    _str = input()
    cnt = 0
    _str_lst = list(_str)
    
    start = _str_lst.index("@")
    end = _str_lst.index("O")

    if start < end:            
        for i in range(start, end):
            if _str_lst[i] == "#":
                cnt += 1
    else:
        for i in range(start, end, -1):         #시작지점과 끝 지점이 역방향인 경우 
            if _str_lst[i] == "#":
                cnt += 1

    if cnt <= m:
        print("HAHA!")
    else:
        print("HELP!")

def main():
    t = int(input())        #testcase
    for _ in range(t):
        isPass()

if __name__ == "__main__":
    main()
