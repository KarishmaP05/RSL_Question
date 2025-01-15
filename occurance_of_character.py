def occurance(str):
    dict={}
    for i in str:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    return dict

str="hello"
print(occurance(str))