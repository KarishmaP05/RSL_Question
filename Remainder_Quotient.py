def remainder_quotient(dividend,divisor):
    if divisor==0:
        return "division not allowed"
    
    quotient=dividend//divisor
    remainder=dividend-(quotient*divisor)  # remainder=dividend % divisor
    return quotient,remainder


dividend=23
divisor=5
quotient,remainder=remainder_quotient(dividend,divisor)
print(f"quotient is {quotient} and remainder is {remainder}")