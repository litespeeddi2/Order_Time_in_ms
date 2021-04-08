import datetime
import time


today = datetime.date.today()
print('Today    :', today)

one_day = datetime.timedelta(days=1)
print('One day  :', one_day)

yesterday = today - one_day
print('Yesterday:', yesterday)

tomorrow = today + one_day
print('Tomorrow :', tomorrow)

print('tomorrow - yesterday:', tomorrow - yesterday)
print('yesterday - tomorrow:', yesterday - tomorrow)

print('Now    :', datetime.datetime.now())
print('Today  :', datetime.datetime.today())
now = datetime.datetime.utcnow()
print('UTC Now:', now)

d = datetime.datetime.now()
for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print(attr, ':', getattr(d, attr))

t = datetime.time(1, 2, 3)
print('t :', t)

d = datetime.date.today()
print('d :', d)

dt = datetime.datetime.combine(d, t)
print('dt:', dt)

format = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()
print('ISO     :', today)

s = today.strftime(format)
print('strftime:', s)

d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format))


dt = datetime.datetime.now()
print(dt)
print(int(round(dt.microsecond/1000)))

date_string = "Wed, 18 Dec 2013 09:30:00 GMT"
date = datetime.datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %Z")
end_date_string = "Wed, 18 Dec 2013 10:15:00 GMT"
end_date = datetime.datetime.strptime(end_date_string, "%a, %d %b %Y %H:%M:%S %Z")
#print (end_date - date).total_seconds()
diff = end_date - date
print(diff)

