#Calculate the tax  计算税收
# Anything purchased for more than $1.00 is charged a 7% tax
price = input('how much did you pay? ')

# Convert the string to a number 将字符串转数字
price = float(price)

# Check if the price is greater than 1.00  判断价格是否高于1.00
if price >= 1.00:
	# Everything over $1.00 is charged 7% tax
	tax = .07
	print('Tax rate is: ' + str(tax))
