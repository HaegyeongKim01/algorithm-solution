def getResult():
    n, m, k = list(map(int, input().split())) 
    k=k-1                #index 범위 재설정 
    a_lst = list(map(int, input().split()))   #주가 
    
    for i in range(k, len(a_lst)):
        if a_lst[i] - a_lst[k] >= m:
            print(i+1)
            return
    print("JB")

def main():
    t = int(input())
    for _ in range(t):
        getResult()

if __name__ == "__main__":
    main()
