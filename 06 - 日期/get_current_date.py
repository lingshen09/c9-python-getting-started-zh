#To get current date and time we need to use the datetime library  要获取当前日期和时间我们要用到datetime库
from datetime import datetime

current_date = datetime.now()
# The now function returns current date and time as a datetime object 使用now这个函数返回当前的日期和时间对象

# You must convert the datetime object to a string  当你要把这个时间和其他字符串拼接之前必须要将这个日期时间对象转为字符串
# before you can concatenate it to another string
print('Today is: ' + str(current_date))
