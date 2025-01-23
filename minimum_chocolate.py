def minimum_chocolate(compound,final_chocolate):
    chocolate=final_chocolate
    for i in range(compound):
        chocolate=(chocolate-1)*2
    return chocolate


compound=7
final_chocolate=3
result=minimum_chocolate(compound,final_chocolate)
print("result",result)