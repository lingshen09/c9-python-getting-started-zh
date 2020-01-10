#To get current date and time we need to use the datetime library  要获取当前日期和时间我们要用到datetime库
from datetime import datetime

# The now function returns current date and time  使用now方法返回当前的日期和时间
today = datetime.now()

# use day, month, year, hour, minute, second functions  尝试使用day, month, year, hour, minute, second方法来展示部分日期字段
# to display only part of the date   
# All these functions return integers  所有这些方法都返回的整数类型
# Convert them to strings before concatenating them to another string 要和其他字符串拼接必须先转换为字符串类型
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))
