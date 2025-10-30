# while loop - a while loop is a type of coonstruct where code
# instructions will keep on running so long as a condition is TRUE(boolean)

# NOTE - in order to stop a loop (or any program) from running in your terminal, click ctrl + c at the same time
# while loop syntax

def ageVerify():
    videoGameAge = 17
    purchaserAge = int(input('How old are you? '))

    while videoGameAge > purchaserAge: # this is a true statement
    #(17 > 15)
        print('You are not old enough to buy this game')
    else:
        print('Thank you! Please enjoy your game.')


#savedpw = 'mirfriedrice'
#userpw = input('Please enter your pasword: ')
#attempt = 0
#while savedpw != userpw:
 #   print('Incorrect password. Please try again.')
 #   attempt +=1
 #   userpw = input('Please type your password again: ')
  #  if attempt ==2:
  #      print('You have made too many failed attempts0. Please reset your password before trying again in a few mminutes')
   #     break
 #   else:
  #      print('Welcome back to your account.')

# create a cpuntdown timer using a while loop
# your timer should start at 30 and count down to 0 by 1

# activity 1

def listLoop():
    numbers = []
    userInput = input('Please type in a number: ')
    while userInput != 'quit':
        newNumber =int(userInput)
        numbers.append(newNumber)
        print(numbers)
        userInput = input('Please type in a number: ')
    else:
        print('Loop has stopped')
    
# istLoop()

# activirt 2

def addLoop():
    numbers = []
    userInput = input('Please enter a number: ')
    while userInput != 'quit':
        newNumber = int(userInput)
        numbers.append(newNumber)
        print(numbers)
        userInput = input('Please enter a number: ')
        x = sum(numbers)
        print(x)
    else:
        print('Loop has ended.')

    

# addLoop()

# activity 3

def guessingLoop():
    correctNumber = 7
    userInput = int(input('Please pick a number 1-10: '))
    while userInput != correctNumber:
        if userInput > correctNumber:
            print('You guessed to low, try again.')
            userInput = int(input('Please pick a number 1-10: '))
        else:
            print('Number is to low.')
            userInput = int(input('Please pick a number 1-10: '))
    else:
            print('You have guessed correctly')

guessingLoop()