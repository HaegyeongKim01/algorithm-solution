from string import ascii_lowercase

dic = {}
for elem in ascii_lowercase:
    dic[elem] = False

s = list(input().replace(' ', '').lower())  #input

for s_elem in s:
    dic[s_elem] = True

#lipogram인 경우 
if False in dic.values():
    print("YES")
    for key, value in dic.items():    #딕셔너리 items()메소드 사용하여 key, value가져옴 
        if value == False:
            print(key, end="")
else:
    print("NO")
