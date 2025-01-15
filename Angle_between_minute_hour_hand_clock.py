
# def minute_hand_angle(minute):
#     minute_angle=6*minute
#     return minute_angle

# def hour_hand_angle(hour,minute):
#     hour = hour % 12
#     print(hour)
#     hour_angle=(30*hour)+(0.5*minute)
#     return hour_angle


# def difference_between_minute_hour(hour,minute):

#     minute_angle=minute_hand_angle(minute)
#     hour_angle=hour_hand_angle(hour,minute)

#     difference=hour_angle-minute_angle

#     if difference>180:
#         difference=360-difference

#     if difference<0:
#         difference=-difference

#     return difference

# hour=3
# minute=15

# difference=difference_between_minute_hour(hour,minute)
# print("difference",difference)


def minuteangle(minute):
    minangle=6*minute
    return minangle

def hourangle(hour,minute):
    hour=hour%12
    hangle=(30*hour)+(0.5*minute)
    return hangle

def smaller_angle(hour,minute):

    hour_angle=hourangle(hour,minute)
    minute_angle=minuteangle(minute)

    angle_diff=hour_angle-minute_angle

    if angle_diff>180:
        angle_diff=360-angle_diff
    if angle_diff<0:
        angle_diff=-angle_diff


    return angle_diff



hour=6
minute=00
result=smaller_angle(hour,minute)
print(result)