def sum_of_integer(num):
    number = str(abs(num))
    # number=num_str.split()
    print("numifdd",number)
    sum=0
    for i in number:
        print(i)
        sum=sum+int(i) # we have to use int(i) here because i has type string . we cannot do sum of  int with string
    return sum


num=454
print(sum_of_integer(num))