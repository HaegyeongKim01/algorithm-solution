def isUmm(s):
    if len(s) < 3:
        return False
    
    if not(s[0] == 'U' and s[1] =='m' and s[2] =='m'):
        return False
    
    for i in range(3, len(s)):
        if s[i] != 'm':
            return False
        
    return True   

def getResult():
    n = map(int, input().split()) #input 1 
    s = input()                  #input 2
    a, b = map(int, input().split()) #input 3
    #index와 입력받는 a, b는 다르므로 주의! 
    a, b = a-1, b-1   #index형태로 변환 
    
    slice_s = s[a:b+1]
    
    if isUmm(slice_s):
        print("YES")
    else: 
        print("NO")
    
def main():
    t = int(input())
    for _ in range(t):
        getResult()

if __name__ == "__main__":
    main()
