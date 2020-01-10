price = input('how much did you pay? ')
price = float(price)

if price >= 1.00:
	# Anything that costs $1.00 or more is charged 7% tax  花费大于等于$1.00的收取7%的税
	# All statements indented are only executed if price is > = 1
	tax = .07
	print('Tax rate is: ' + str(tax))
else:
	# Anything else we do not charge any tax  其他情况则不收取任何税
	# All statements indented are only executed if price is NOT >= 1 
	tax = 0
	print('Tax rate is: ' + str(tax))


