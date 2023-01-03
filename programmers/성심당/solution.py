def main():
    bread = {}        #dictonary initialize
    for _ in range(2):
        name = input()
        price = int(input())
        bread[name] = price
        
    print(max(bread, key=bread.get))    #print

if __name__ == "__main__":
    main()
