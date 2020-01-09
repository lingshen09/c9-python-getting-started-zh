first_num = input('Enter first number ')
second_num = input('Enter second number ')
# If you have a string variable containing a number   如果你在字符串中包含数字
# And you want to treat it as a number  你希望当作数字处理
# You must convert it to a numeric datatype  你必须明确的转换他们的类型
# int() converts a string to an integer e.g. 5, 8, 416, 506  int()方法可以转换整数例如：5, 8, 416, 506
print(int(first_num) + int(second_num))

# float() converts a string to a decimal or float number e.g. 3.14159, 89.5, 1.0  float方法用于转换带小数的浮点数例如 3.14159, 89.5, 1.0
print(float(first_num) + float(second_num))

