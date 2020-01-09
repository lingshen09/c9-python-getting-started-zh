# Ask the user for their first and last name  
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# the capitalize function will return the string with  通过capitalize方法可以做到首字母大写其他字母小写 
# the first letter uppercase and the rest of the word lowercase
print ('Hello ' + first_name.capitalize() + ' ' \
       + last_name.capitalize())
