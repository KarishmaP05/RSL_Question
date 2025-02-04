def sortmarklist(mark_list):
    n=len(mark_list)
    for i in range(n-1):
        for j in range (n-i-1):
            if mark_list[j]<mark_list[j+1]:
                mark_list[j+1],mark_list[j]=mark_list[j],mark_list[j+1]
    print("marklist",mark_list)
    return mark_list

def rank_new_mark(mark_list,new_mark):
    #sort the mark list first
    sorted_mark_list=sortmarklist(mark_list)
    rank=1
    for mark in sorted_mark_list:
        if new_mark < mark:
            rank+=1
        elif new_mark==mark:
            break
    return rank
new_mark=40
mark_list=[28,38,36,38,34,31,39]
result=rank_new_mark(mark_list,new_mark)
print(result)