week = []
day = ('MON','TUE','WED','THUR','FRI','SAT','SUN')
for i in range(len(day)):
    morning = (int(input(f"Enter the minutes for Morning session {day[i]}: ")))/60
    afternoon = (int(input(f"Enter the minutes for Afternoon session {day[i]}: ")))/60
    evening = (int(input(f"Enter the minutes for Evening session {day[i]}: ")))/60
    total = morning+afternoon+evening
    hours = ["{:.2f}".format(morning),"{:.2f}".format(afternoon),"{:.2f}".format(evening),"{:.2f}".format(total)]
    week.append(hours)
print("Day >>>  morning   Afternoon  Evening  Total time")
for x,y in zip(day,week):
    print(f"{x}  >>>  {y[0]}   {y[1]}   {y[2]}   {y[3]}")