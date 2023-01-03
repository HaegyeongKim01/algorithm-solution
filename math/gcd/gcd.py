def gcd(a, b):
    if b == 0:
        return a
    if a == 1 or b == 1:
        return 1
    
    if a > b:
        return gcd(b, a%b)
    else:
        return gcd(a, b%a)

def main():
    a, b = map(int, input().split())
    print(gcd(a, b))    

if __name__ == "__main__":
    main()
