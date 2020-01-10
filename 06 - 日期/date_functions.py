#To get current date and time we need to use the datetime library   要获取当前日期和时间我们要用到datetime库
from datetime import datetime, timedelta
# The now function returns current date and time 使用now方法返回当前的日期和时间
today = datetime.now()

print('Today is: ' + str(today))
#You can use timedelta to add or remove days, or weeks to a date 你可以使用timedelta方法对某个日期增加或减少几天或几周
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))

