def is_prime(N):
    if N <=1:
        return False
    for i in range(2,N):
        if N % i==0:
            return False
    return True

def Nearest_prime(N):

    if is_prime(N):
        return N , N
    
    lower_number=N-1
    upper_number=N+1

    # find lowest prime number

    while not is_prime(lower_number):
        lower_number-=1

    # find upper prime number

    while not is_prime(upper_number):
        upper_number-=1

    return lower_number,upper_number
N=12
lower,upper=Nearest_prime(N)
print("lower",lower,"  ","upper",upper)