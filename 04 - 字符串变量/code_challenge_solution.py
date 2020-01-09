# ask a user to enter their first name and store it in a variable  让用户输入姓并存入变量first_name
first_name = input('What is your first name? ')
# ask a user to enter their last name and store it in a variable 让用户输入名字并存入变量last_name
last_name = input('What is your last name? ')

# print their full name  打印出完整姓名
# Make sure you have a space between first and last name
# Make sure the first letter of first name and last name is uppercase  
# Make sure the rest of the name is lowercase
# 使用capitalize来做到首字母大写其余小写
print(first_name.capitalize() + ' ' + last_name.capitalize())