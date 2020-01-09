# There are a number of string functions you can use 下面是一些字符串方法
# on string variables
sentence = 'The dog is named Sammy'

# upper will return the string in uppercase letters upper可以把字符串全部转大写返回
print(sentence.upper())

# lower will return the string in lowercase letters lower可以把字符串全部转小写返回
print(sentence.lower())

# capitalize will return the string with the first letter uppercase
# and the rest of the string in lowercase  capitalize可以把字符串首字母大写其他小写返回
print(sentence.capitalize())

# count will count the number of occurrences of the value specified
# in the string, in this case how many times the letter 'a' appears   count则可以统计出指定的字符（比如字母a）在字符串中出现的次数
print(sentence.count('a'))
