a="hello"
print("abc"[::-1])

def reverseString(s):
    # code here
    rev=""
    for i in range(len(s)-1,-1,-1):
        # print(i," ",arr[i])
        rev=rev+s[i]
    return rev
    
s="karishma"
r=reverseString(s)
print(r)
