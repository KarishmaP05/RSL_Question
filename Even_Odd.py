def even_odd(arr):
    result={
        "even":[],
        "odd":[]
    }
    

    for i in arr:
        if i % 2==0:
            result["even"].append(i)
        else:
            result["odd"].append(i)

    return result

arr=[1,5,3,4,6,8,2]
result=even_odd(arr)
print("result",result)
