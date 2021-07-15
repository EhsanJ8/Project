level = None
emtiaz = 0
if emtiaz>=0 and emtiaz<=10:
    level = 'Beginner'
elif emtiaz>10 and emtiaz<=12:
    level = 'Beginner-Intermediate'
elif emtiaz>12 and emtiaz<=15:
    level = 'Intermediate'
elif emtiaz>15 and emtiaz<=17:
    level = 'Intermediate-Upper Intermediate'
elif emtiaz>17 and emtiaz<=19:
    level = 'Upper Intermediate'
elif emtiaz>19 and emtiaz<=21:
    level = 'UpperIntermediate-Advanced'
elif emtiaz==22:
    level = 'Advanced-Upper Advanced'
else:
    level = 'Upper Advanced'
