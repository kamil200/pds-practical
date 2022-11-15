import datetime
from datetime import datetime
print("Datetime object for jan 15 2012:")
print(datetime(2012,1,11))
print("\n Specific date and time of 9:20 pm")
print(datetime(2011,1,11,21,20))
print("\n Local date and time:")
print(datetime.now())
print("\n A date without time:")
print(datetime.date(datetime(2012,5,22)))
print("\n Current date:")
print(datetime.now().date())
print("\n Time from a datatime:")
print(datetime.time(datetime(2012,12,15,18,12)))
print("\n Current local time :")
print(datetime.now().time())

