yourMinutes = int(input())
hours = yourMinutes//60
minutes = yourMinutes%60
if hours >= 24:
    hours2 = hours % 24
    print (hours2,":",minutes)
else:
    print (hours,":",minutes)
