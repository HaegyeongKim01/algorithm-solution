def print_snow(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end="")
        print()

def main():
    n = int(input())
    
    r1, c1, r2, c2 = map(int, input().strip().split(' '))
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1   #position을 index0에 맞추어준다. 
    
    #arr Initialize
    arr = [["*" for _ in range(n)] for _ in range(n)] 
    
    #직사각형 오른쪽 위, 왼쪽 아래
    if c1 > c2:
        c1, c2 = c2, c1
    #직사각형 오른쪽 아래, 왼쪽 위
    elif r1 >r2:
        r1, r2 = r2, r1
    #default로 왼쪽위 오른쪽 아래     
    for y in range(r1, r2+1):           #눈 치우기 실행  
        for x in range(c1, c2+1):
            arr[y][x] = "."
            
    print_snow(arr)
    
if __name__ == "__main__":
    main()