def LeapYear(year):
    if (year % 400 ==0)or(year % 4==0 and year % 100 !=0):
       return "leap year"
    else:
        return "not leap year"


year=2024
result=LeapYear(year)
print(result)