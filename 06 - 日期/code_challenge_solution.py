from datetime import datetime, timedelta

# print today's date 打印出今天的日期
current_date = datetime.now()
print(current_date)

# print yesterday's date  打印出昨天的日期
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('Yesterday was: ' + str(yesterday))

# ask a user to enter a date  请求用户输入一个日期
date_entered = input('Please enter a date (dd/mm/yyyy): ')
date_entered = datetime.strptime(date_entered, '%d/%m/%Y')

# print the date one week from the date entered  打印出输入日期一周后的日期
one_week = timedelta(weeks=1)
one_week_later = date_entered + one_week
print('One week later it will be: ' + str(one_week_later))