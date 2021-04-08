# Test update for git
import datetime
import time

dt1 = datetime.datetime.now()
#print(type(dt1))
#print(dt1)
#print(int(round(dt1.microsecond/1000)))

#time.sleep(1.211)

time.sleep(.211)

dt2 = datetime.datetime.now()
#print(type(dt2))
#print(dt2)
#print(int(round(dt2.microsecond/1000)))

timedifference = dt2 - dt1
print('difference in time:', timedifference)

time_in_millis = round(timedifference.total_seconds() * 1000)
print('milliseconds:', time_in_millis)

'''
time.strptime('08/02/2017 01:21:18.267', '%d/%m/%Y %H:%M:%S.%f')
time.strptime('08/02/2017 01:21:18.647', '%d/%m/%Y %H:%M:%S.%f')
time.strptime('08/02/2017 01:21:18.650', '%d/%m/%Y %H:%M:%S.%f')
time.strptime('08/02/2017 01:21:18.687', '%d/%m/%Y %H:%M:%S.%f')
time.strptime('08/02/2017 01:21:18.760', '%d/%m/%Y %H:%M:%S.%f')
'''
#date_string = "Wed, 18 Dec 2013 09:30:00 GMT"
#date = datetime.datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %Z")
#end_date_string = "Wed, 18 Dec 2013 10:15:00 GMT"
#end_date = datetime.datetime.strptime(end_date_string, "%a, %d %b %Y %H:%M:%S %Z")
#print (end_date - date).total_seconds()
#diff = end_date - date
#print(type(diff))
#print(diff.seconds * 1000) + (diff.microseconds / 1000)
