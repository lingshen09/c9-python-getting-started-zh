# I check to see if the requirements for honour roll are met
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

# Boolean variables allow you to remember a True/False value  布尔类型可记录真/假
if gpa >= .85 and lowest_grade >= .70:
	honour_roll = True
else:
	honour_roll = False

# Somewhere later in your code if you need to check if students is  当你需要检查一个学生是否满足条件时，只需要看之前设置的判断值是否为真
# on honour roll, all I need to do is check the boolean variable
# I set earlier in my code
if honour_roll:
	print('You made honour roll')
