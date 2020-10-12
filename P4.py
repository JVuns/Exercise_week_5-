import datetime
now = datetime.datetime.now()
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.strftime("%A")
print("year: ",year(now))
print("month: ",month(now))
print("day: ",day(now))
