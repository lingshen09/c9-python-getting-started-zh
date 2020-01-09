# Ask a user to enter a number  让用户输入第一个数字
first_number = input('Enter a number: ')

# Ask a user to enter a second number 让用户输入第二个数字
second_number = input('Enter another number: ')

# Calculate the total of the two numbers added together  计算答案
answer = float(first_number) + float(second_number)

# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read 打印结果
# 4 + 6 = 10  
print(first_number + ' + ' + second_number + ' = ' + str(answer))

# If you do not want the decimal places you could round the answer 如果不希望保留小数部分，可以使用round对结果取整
print(first_number + ' + ' + second_number + ' = ' + str(round(answer)))