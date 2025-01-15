def is_prime(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number %i==0:
            return False
    return True
def prime_number(N):
    prime=[]
    if N>1:
        for i in range(2,N+1):
            prime_num=is_prime(i)
            if prime_num==True:
                prime.append(i)
        return prime
    else:
        return "no prime numbers"
N=10
result=prime_number(N)
print("result",result)
