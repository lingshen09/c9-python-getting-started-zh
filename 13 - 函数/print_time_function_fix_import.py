# Import datetime class from datetime library to simplify calls to datetime.now()  先引用（import） 需要的datetime库来调用需要的datetime.now()方法
from datetime import datetime

# Create a function called print_time   创建一个叫print_time的方法
# This function will print the message and current time 这个方法将打印出消息和当前时间
def print_time():
    print('task completed')
    print(datetime.now())
    print()

first_name = 'Susan'
# Call print_time() function to display message and current time  尝试调用print_time
print_time()

for x in range(0,10):
    print(x)
# Call print_time() function to display message and current time 尝试调用print_time
print_time()