def without_repeating_character(str):

    string=""

    for i in str:
        if i not in string:
            string+=i
    return string 

str="helper"
result=without_repeating_character(str)
print("result",result)