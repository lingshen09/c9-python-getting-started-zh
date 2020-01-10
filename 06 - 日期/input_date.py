# import the datetime and timedelta modules  引入时间和时间差计算模块
from datetime import datetime, timedelta

# When you ask a user for a date tell them the desired date format  请求用户输入一个日期
birthday = input('When is your birthday (dd/mm/yyyy)? ')

# When you convert the string containing the date into a date object  当你转换字符串到日期对象时
# you must specify the expected date format  必须指定日期的格式
# if the date is not in the expected format Python will raise an exception 否则Python会报错
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print ('Birthday: ' + str(birthday_date))

# Because we converted the string into a date object   当我们转换时间字符串到日期对象后
# We can use date and time functions such as timedelta with the object 我们可以使用日期和时间的方法比如timedelta去操作这个对象
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))
