country = 'CANADA'
# by converting the string entered to lowercase and comparing it to a string  将字符串全部转为小写再比较
# that is all lowercase letters I make the comparison case-insensitive
# If someone types in CANADA or Canada it will still be a match  即使有人输入了CANADA或则Canada也可以正确进行匹配了
if country.lower() == 'canada':
	print('Hello eh')
else:
	print('Hello')
