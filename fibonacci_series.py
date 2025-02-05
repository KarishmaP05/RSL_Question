def fibonacci(N):
    a = 0
    b = 1
    for i in range(N):
        print(a)
        
        # a,b=b,a+b
        
        temp=a
        a=b
        b=temp+b

N = 10
fibonacci(N)

