distance=float(input("enter distance in kms:"))
speed=float(input("enter speed in kms/hr:"))
time=distance/speed
time_in_minutes=time*60
print("time taken in minutes:",round(time_in_minutes,2))