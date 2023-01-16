def is_anagram(str1,str2):
    str1,str2 = sorted(str1), sorted(str2)
    return str1 == str2
    
def main():
    #input
    str1, str2 = input().split(' ')
    if is_anagram(str1,str2):
        print("True")
    else:
        print("False")

if __name__=="__main__":
    main()