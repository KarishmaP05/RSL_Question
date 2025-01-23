def time_difference(t1,t2):
    h1=int(t1[0:2])
    h2=int(t2[0:2])

    m1=int(t1[3:5])
    m2=int(t2[3:5])

    hour_diff=h2-h1
    if hour_diff <0:
        hour_diff+=24
    

    minute_diff=m2-m1
    if minute_diff<0:
        minute_diff+=60

    shortest_hour=min(hour_diff,24-hour_diff)
    shortest_minute=min(minute_diff,60-minute_diff)
    shortest_time_difference=shortest_hour+shortest_minute

    return shortest_time_difference

t1="03:56"
t2="03:58"
result=time_difference(t1,t2)
print(result)