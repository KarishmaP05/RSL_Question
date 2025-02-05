def  reverse_with_underscores(s):
    underscore_position=[]
    non_underscore_char=[]
    
    for i in range(len(s)):
        if s[i]=='_':
            underscore_position.append(i)
        else:
            non_underscore_char.append(s[i])
            
            
    print(underscore_position)
    # print("non_underscore_char",non_underscore_char)
    
    reverse_non_underscore_char=non_underscore_char[::-1]
    print("reverse_non_underscore_char",reverse_non_underscore_char)
    result=list(s)
    print("result",result)
    non_underscore_index=0
    
    
    for i in range(len(s)):
        if i not in underscore_position:
            result[i]=reverse_non_underscore_char[non_underscore_index]
            non_underscore_index+=1
            
    # print(result)
    
    print(''.join(result))
            




input_string = "I_LOVE_INDIA"
output_string = reverse_with_underscores(input_string)
print(output_string) 