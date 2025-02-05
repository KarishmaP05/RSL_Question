def first_non_repeated_character(s):
    char_count={}
    for char in s:
        char_count[char]=char_count.get(char,0)+1

    for char in s:
        if char_count[char]==1:
            return char
        
    return None


s="hello"
result=first_non_repeated_character(s)
print(result)


def first_non_repeated_character(s):
    char_count={}
    for char in s:
        char_count[char]=char_count.get(char,0)+1

    for char in s:
        if char_count[char]==1:
            return char
        
    return None


s="hello"
result=first_non_repeated_character(s)
print(result)



def non_repeated_character(string):
    char_count={}
    for i in string:
        if i in char_count:
            char_count[i]+=1
        else:
            char_count[i]=1
            
    for i in string:
        if char_count[i]==1:
            print(i)
            break
        # else:
        #     print("every char is repeated")
        


string="hello"
non_repeated_character(string)