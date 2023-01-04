def isSuccess(str):
    s_lst = list(str)
    cnt = 0
    for s in s_lst:
        if s == "#":
            cnt += 1
    if cnt <= 1:
        return True
    else:
        return False

def main():
    s = input()         
    
    if isSuccess(s):
        print("HAHA!")
    else:
        print("HELP!")

if __name__ == "__main__":
    main()
