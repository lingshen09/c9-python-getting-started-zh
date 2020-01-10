# When you join a hockey team you get your name on the back of the jersey 当你加入一个冰球队，你的运动衫背后会印上你的名字
# but the jersey may not be big enough to hold all the letters  但运动衫可能不够空间印上你名字所有字母
# Ask the user for their first name    请求用户输入姓

# Ask the user for their last name      请求用户输入名

# if first name is < 10 characters and last name is < 10 characters    当姓和名都小于10个字母
#       print first and last name on the jersey      印上姓名
# if first name >= 10 characters long and last name is < 10 characters  当姓大于10个字母而名字小于10个字母
#       print first initial of first name and the entire last name   印上姓的首字母和完整的名字
# if first name < 10 characters long and last name is >= 10 characters   当姓小于10个字母而名字大于10个字母
#       print entire first name and first initial of last name       印上完整姓和名字的首字母
# if first name >= 10 characters long and last name is >= 10 characters   当姓和名都大于10个字母
#       print last name only                                          只印上名字

# Test with the following values
# first name: Susan  last name: Ibach
# output: Susan Ibach
# first name: Susan  last name: ReallyLongLastName
# output: Susan R.
# first name: ReallyLongFirstName  last name: Ibach
# output: R. Ibach
# first name: ReallyLongFirstName  last name: ReallyLongLastName
# output: ReallyLongLastName