def without_repeating_character(str):
    
    string=""

    for i in str:
        if i not in string:
            string+=i
    return string 

str="programming"
result=without_repeating_character(str)
print("result",result)

def remove_duplicates(str):
    string=""
    for i in str:
        if i not in string:
            string+=i
    return string



str="helper"
result=remove_duplicates(str)
print(result)


