# COnditional Statement - code instructions that have different outcomes based on the inputted data.
# input --> condition --> output

# Conditional Statement Syntax
# if keyword- controls the condition we want to satisfy

# else keyword - our default outcome. The thing that happens when our conditions are not SATISFIED

studentcredit = input('please enter the number of credits you have')

if int(studentcredit) >= 50:
    print('Congrats! You are eligible to graduate!')

else:
    print('sorry, you have not satisfied the required credit points.')

weather = 'sunny'

if weather == 'sunny':
    print('Have a great day an dbring sunglasses')
elif weather == 'rainning':
    print('remember to bring an umberella')
elif weather == 'snowing':
    print('Its snowy outside')