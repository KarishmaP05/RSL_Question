def check_order(num):
    num_str=str(num)

    ascending=True
    descending=True

    for i in range(len(num_str)-1):
        if num_str[i]>num_str[i+1]:
            ascending= False
            break
    
    for i in range(len(num_str)-1):
        if num_str[i]<num_str[i+1]:
            descending=False
            break
    
    if ascending:
        return "ascending"
    elif descending:
        return "descending"
    else:
        return "no proper sequence"
    
num=5434565421
result=check_order(num)
print(result)

