# A student makes honour roll if their average is >=85   学生获得荣誉的条件是平均绩点不低于85同时最低分不低于70
# and their lowest grade is not below 70
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)

if gpa >= .85 and lowest_grade >= .70:
		print('You made the honour roll')

