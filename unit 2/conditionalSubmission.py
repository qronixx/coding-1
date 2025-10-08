# Activity 1

# def permitAgeCheck(age):
#   if age >= 16:
#        print('Congrats! You are eligible to get your driver permit.')
#   else:
 #        print('Sorry you are too young at this time.')

#permitAgeCheck(15)

num = input('Please enter any number to your liking.')

if int(num) >= 1:
     print('This number is a positive.')
elif int(num) <= -1:
     print('This number is a negative.')

gradeScore = input('What is your current grade score?')

if int(gradeScore) <= 70:
     print('Your current grade is a F')
elif int(gradeScore) >= 70 and int(gradeScore) <= 80:
     print('Your current grade is a C')
elif int(gradeScore) >= 80 and int(gradeScore) <= 90:
     print('Your current grade is a B')
elif int(gradeScore) >90:
     print('Your current grade is an A')