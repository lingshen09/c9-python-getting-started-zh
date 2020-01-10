# Create function get_initial to accept a name and 创建一个获取首字母并返回其大写的方法
# return the first letter of the name in uppercase
# Parameters:
#   name: the name of a person
# Return value:
#   first letter of name passed in as a parameter in uppercase 
def get_initial(name):
    initial = name[0:1].upper()
    return initial

#Ask for someone's name and return the initials 请输入某人的名字
first_name = input('Enter your first name: ')
middle_name = input('Enter your middle name: ')
last_name = input('Enter your last name: ')

# Call get_initial function to return first letter of a name 调用get_initial方法返回名字的首字母
print('Your initials are: ' \
    + get_initial(first_name) \
    + get_initial(middle_name) \
    + get_initial(last_name))