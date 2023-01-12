def isPass():
    n, m = map(int, input().split())
    _str = input()
    _str = list(_str)  #리스트로 변환
    
    start = _str.index('@')
    end = _str.index('O')
    g = _str.index('G')
    cnt = 0

    if start<end:
        _str1 = _str[start:end]
        
    else:
        _str1 = _str[end:start]
        
    if _str1.count('#') <= m:
        print("HAHA!")
        return()

    if start < g:
        _str2 = _str[start:g]
    else:
        _str2 = _str[g:start]

    if _str2.count('#') <= m:
        print("HAHA!")
    else:
        print("HELP!")
    
def main():
    t = int(input())
    for _ in range(t):
        isPass()

if __name__ == "__main__":
    main()
