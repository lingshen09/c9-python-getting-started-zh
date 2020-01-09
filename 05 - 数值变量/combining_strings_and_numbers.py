days_in_feb = 28

# The print function can accept numbers or strings  打印这个方法可以接受数字或字符串
print(days_in_feb)

# The + operator can either add two numbers or it can concatenate two strings  使用+号可以连接两个数字或字符串
# it does not know what to do when you pass it one number and one string  但是当我们给出一个数字和一个字符串就不知道该如何操作
# This line of code will cause an error    下面这行代码会导致报错
print(days_in_feb + ' days in February')

# You need to convert the number to a string to display the value  你应该将数字转为字符串
# This line of code will work  下面的代码可以正常执行
print(str(days_in_feb) + ' days in February')

