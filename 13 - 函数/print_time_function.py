import datetime
# Create a function called print_time   创建一个print_time方法
# This function will print the message and current time  这个方法打印出消息和当前时间
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print() 

first_name = 'Susan'
# Call print_time() function to display message and current time
print_time()

for x in range(0,10):
    print(x)
# Call print_time() function to display message and current time
print_time()