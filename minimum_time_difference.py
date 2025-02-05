# 24 hour clock

# def time_difference(t1,t2):
#     h1=int(t1[:2])
#     h2=int(t2[:2])
#     period1=t1[-2:]
#     period2=t2[-2:]

#     m1=int(t1[3:5])
#     m2=int(t2[3:5])
    
#     if period1=="AM" and h1==12:
#         h1=0
#     if period1=="PM" and h1!=12:
#         h1+=12
        
#     if period2=="AM" and h1==12:
#         h2=0
#     if period2=="PM" and h1!=12:
#         h2+=12

#     hour_diff=h2-h1
#     minute_diff=m2-m1
    
  
#     if hour_diff <0:
#         hour_diff+=24
        
#     if minute_diff<0:
#         minute_diff+=60
#         hour_diff -= 1
        
#     # convert everything in minute
#     total_diff_minutes=hour_diff*60+minute_diff
    
#     shortest_time_diff = f"{hour_diff} hours and {minute_diff} minutes"
    
#     return total_diff_minutes, shortest_time_diff

# t1="03:56 PM"
# t2="03:58 PM"
# total_diff_minutes,shortest_time_diff=time_difference(t1,t2)
# print(total_diff_minutes)
# print(shortest_time_diff)

# 24 hour clock



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
t2="18:12"
result=time_difference(t1,t2)
print(result)