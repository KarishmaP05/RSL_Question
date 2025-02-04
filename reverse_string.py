# a="hello"
# print("abc"[::-1])

# def reverseString(s):
#     # code here
#     rev=""
#     for i in range(len(s)-1,-1,-1):
#         # print(i," ",arr[i])
#         rev=rev+s[i]
#     return rev
    
# s="karishma"
# r=reverseString(s)
# print(r)



def reverse():
    string="I Love My Country"
    print(string)

    s=string.split()
    print(s)
    word=''
    words=[]

    for i in string:
        if i==' ':
            words.append(word)
            word=''
        else:
            word+=i
    words.append(word)
    print(words)

    reversearray=words[::-1]
    print(reversearray)
    final=''
    for i in reversearray:
        if i== reversearray[-1]:
            final+=i
        else:
            final+=f"{i} "


    print(final)




reverse()