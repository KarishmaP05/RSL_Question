def occurance(str):
    dict={}
    for i in str:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print("dict",dict)
    compressed=''.join(dict)
    print("compressed",compressed)
    return dict

str="hello"
print(occurance(str))


