from datetime import datetime

# Define a function to print the current time and task name  定义一个打印当前时间和任务名的方法
# Function the following parameters:  方法的参数
#   task_name: Name of the task to display to output screen  任务名： 显示在屏幕的任务名字
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Susan'
# Call print_time() function to display message and current time  调用print_time方法来展示消息和时间
# pass in name of task completed
print_time('first name assigned')

for x in range(0,10):
	print(x)
# Call print_time() function to display message and current time
# pass in name of task completed
print_time('loop completed')
