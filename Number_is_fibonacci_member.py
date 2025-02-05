def is_perfect(x):
    if x<0:
        return False
    i=0
    while i*i<=x:
        if i*i==x:
            return True
        i+=1
    return False 

def is_fibonacci(N):
    condition1=5*N*N+4
    condition2=5*N*N-4

    # return is_perfect(condition1) or is_perfect(condition2)

    if is_perfect(condition1) or is_perfect(condition2):
        return f"fibonacci series"
    else:
        return f"not fs"

N=13
result=is_fibonacci(N)
print(result)