country = input('Enter the name of your home country: ')
if country == 'canada':
	# string comparisons are case sensitive  字符串比较是大小写敏感的
	# if you typed in CANADA or Canada it will not match 你输入CANADA或者Canada和canada是不匹配的
	print('So you must like hockey!')
else:
	print('You are not from Canada')
