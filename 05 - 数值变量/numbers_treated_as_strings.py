# Python has to guess what datatype a variable should be  Python必须指定一个变量应该何种类型

# since the input function returns a string, the variables it populates input方法返回的是一个字符串
# will hold string values
first_num = input('Enter first number ')
second_num = input('Enter second number ')

# Because first_num and second_num are string variables the + operator 因为first_num和second_num是字符串类型而+号连接看起来像姓名拼接
# concatenates them just like concatenating first_name and last_name
print(first_num + second_num)