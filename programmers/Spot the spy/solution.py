def solution():
    
    n = int(input())
    arr = list(map(int, input().split()))
    if len(arr) < 3:   #input arr ERROR
        return -1   
    
    for a in arr:               #특정 int 값이 2개 이상이면 같은 수 
        if arr.count(a) > 1:
            same_num = a
            break

    for i in range(len(arr)):   #same_num과 다르다면 다른 한 개의 수
        if arr[i] != same_num:
            print(i+1)
            break

def main():
    t = int(input())
    for _ in range(t):
        solution()

if __name__ =="__main__":
    main()