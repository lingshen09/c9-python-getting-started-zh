# Fix the mistakes in this code and test based on the description below  根据测试描述修复下面代码的错误
# If I enter 2.00 I should see the message "Tax rate is: 0.07"   输入2.00应该看到消息"Tax rate is: 0.07"
# If I enter 1.00 I should see the message "Tax rate is: 0.07"   输入1.00应该看到消息"Tax rate is: 0.07"
# If I enter 0.50 I should see the message "Tax rate is: 0"      输入0.50应该看到消息"Tax rate is: 0"
price = input('how much did you pay? ')

if price > 1.00:
	tax = .07
	print('Tax rate is: ' + str(tax))
else
	tax = 0
print('Tax rate is: ' + str(tax))