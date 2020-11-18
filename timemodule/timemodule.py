import time
z=["L", "M", "Mi", "J", "V", "S", "D"]
print("time in seconds:", time.time())
print("Today", time.ctime())
t=time.localtime()
print("Year", t.tm_year)
print("Month", t.tm_mon)
print("Day", t.tm_mday)
print("Day of week", z[t.tm_wday])
print("Day from year", t.tm_yday)
print("Hour", t.tm_hour)
print("Min", t.tm_min)
print("Sec", t.tm_sec)
print("Data si ora exacta: Anul ", str(t.tm_year)+ ", luna " + str(t.tm_mon)+ ", ziua " + str(t.tm_mday)+", "+str(z[t.tm_wday])+", ora "+str(t.tm_hour)+ ", min "+ str(t.tm_min)+", sec "+ str(t.tm_sec) + ".")

# Both localtime and gmtime have one parameter (the number of seconds from 1970).
# If this parameter is provided the time object will be the time computed based on that number.
# Otherwise the time object will be the time based on time.time () (current time) value
print(time.localtime())
print(time.gmtime(time.time()))

#Use mktime to convert from a time object struct to a float number.
#Use asctime member to convert from a time object to a readable representation of the time (string format)
import time
t=time.time()
tobj=time.localtime()
tm=time.mktime(tobj)
print(tm)
print(t)
print(time.asctime(tobj))

#Use strftime to time object to a specified string representation:
# %H Hour in 24 hour format
# %I Hour in 12 hour format
# %Y Year (4 digits)
# %m Month (decimal)
# %B Month (name)
# Abreviation Description
# %M Minute
# %S Seconds
# %A Day of week (name)
# %d Day of month (decimal)
# %p AM or PM

import time
t=time.localtime()
print(time.strftime("%H:%M:%S"), t)
print(time.strftime("%Y.%m.%d"), t)
print(time.strftime("%d,%A,%B,%Y"),t)

#strftime if used without a time object applies the string format to the current time.
#Time module also has a function sleep that receives one parameter (the number of seconds the current script has to wait until it continues its execution).
import time
for i in range(0,4):
    print (time.strftime("%H:%M:%S"))
    time.sleep(2) #sleep 2 seconds