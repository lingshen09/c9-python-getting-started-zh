# Create a function to return the first initial of a name  创建一个返回名字首字母的方法
# Parameters:
#   name: name of person  人名
#   force_uppercase: indicates if you always want the initial to be in upppercase: default is True  默认强制转换
# Return value
#   first letter of name passed in
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

# Ask for someone's name and return the initial
first_name = input('Enter your first name: ')

# Call get_initial function to retrieve first letter of name
# not passing a value for force_uppercase so default value is used  当不传入参数时会根据默认值强制转换大写
first_name_initial = get_initial(first_name) 

print('Your initial is: ' + first_name_initial)