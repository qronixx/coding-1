# For Loops - a type of construct that runs code instruction a finite amount of times over a group of data

# for loop syntax

#movies = ['action movie','scary movie','sci fi movie','romance movie']

#for genre in movies:
#    print(genre)

#numbers =[1,2,3,4,5,6,7,8]

#for digit in numbers:
#    multi = digit * 2
#    print('Here is te numbers multiplied by 2: '+ str(multi))

#for x in range(0,10):
#    print(x)

#trickortreat = ['Snickers','Hershey Bar','Twizzler','Candied Apple','Candy Corn']

#count = len(trickortreat)

#print(count)

#i is a variable and is short for iterator

#for i in trickortreat:
 #   print(i)
#print('I have this candy in my bag' + i)

def ex1():
   for i in range(1,5):
    print(i)

def act3():
   for x in range(5):
    word = input('Please type in a word: ')
    print(word)


def fed():
   for i in range(5):
    number = input('Please type in a number: ')
    print(number)
    print('We have completed' + int(x) + ' loop')

def abc():

   for x in range(3):
    print('true or false:3 is greater than 2')
    answer = input()
    if answer != 'true':
        print('wrong, try again')
        print('attemot: '+ str(x))
    else:
      print('great!')
      break
    
# looping through strings

def ex2():
   word = 'P y t h o n'
   for letter in word:
      print(letter)

#looping thorugh a list of numbers
shoppingprices= [2.00, 5.40, 7.20, 9.00]
total = 0
tax = 0.7
def ada():
   for items in shoppingprices:
      total += items * tax

print(total)

level = input('What floor would you like to go to? ')

def elavator():
  if int(level) == 1:
     print('Welcome to the first floor; the gym and sauna are on this floor')
  elif int(level) == 2:
    print('Welcome to the second floor') 

shipment = []
deffective = []

for x in range(10):
   print('Create an iphone.')
   print('Step 1. Get casing.')
   print('Step 2. Put in motherboard and hardware.')
   print('Step 3. Put on screen.')
   print('Step 4. Check tos see if it works.')
   screenison = input('Is the screen on? ')
   if screenison == False:
     print('Remove from production')
     phone = 'iphone serial number' + str(x)
     deffective.append(phone)
   else:
      print('Step 5. Put in box and place in shipment.')
      phone = 'iphone serial number ' + str(x)
      shipment.append(phone)
      
print(deffective)      
print(shipment)