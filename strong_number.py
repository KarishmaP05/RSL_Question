def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result=result*i
    return result



def is_strong(n):
    num_str=str(n)
    result=0
    for i in num_str:
        result+=factorial(int(i))
        
    # print(result)
    if result==n:
        print("strong number")
    else:
        print("not a strong")
        


n=40585
is_strong(n)
