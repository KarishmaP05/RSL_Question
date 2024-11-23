
def minute_hand_angle(minute):
    minute_angle=6*minute
    return minute_angle

def hour_hand_angle(hour,minute):
    hour = hour % 12
    print(hour)
    hour_angle=(30*hour)+(0.5*minute)
    return hour_angle


def difference_between_minute_hour(hour,minute):

    minute_angle=minute_hand_angle(minute)
    hour_angle=hour_hand_angle(hour,minute)

    difference=hour_angle-minute_angle

    if difference>180:
        difference=360-difference

    if difference<0:
        difference=-difference

    return difference

hour=9
minute=00

difference=difference_between_minute_hour(hour,minute)
print("difference",difference)