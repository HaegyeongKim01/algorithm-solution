from string import ascii_lowercase

s =list(input().replace(' ', '').lower())   #공백제거->lower->list화 
alphabet = {}
#alpabet 초기화
for i in ascii_lowercase:
    alphabet[i]=False

#알파벳 있다면 True로
for s_elem in s:
    alphabet[s_elem] = True

if False in alphabet.values():
    print("NO")
else:
    print("YES")
