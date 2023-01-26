def count_building(arr, is_righting):
    cnt = 0
    max_layer = 0
    
    if is_righting:
        arr.reverse()
    
    for a in arr:
        if max_layer < a:
            max_layer = a
            cnt +=1 
            
    return cnt

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_building(arr, False), count_building(arr, True))

if __name__ == "__main__":
    main()