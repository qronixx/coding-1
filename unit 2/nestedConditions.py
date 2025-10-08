#def signup():
#    email = input('Please enter email: ')
#    password = input('Please create a password: ')
#    if email == 'heem@gmail.com':
#        print('You already have an account associated with this email.')
#    else:
#        username = input('Welcome! Please create a username: ')
#        if username == 'ian':
#            print('Sorry that user already exists!')
#        else:
#            print('Great, you are all set!')
#    
#signup()

def movieTicket():
    age = int(input('Please type in ur age: '))
    if age <= 12:
        print("Great what movie would you like to see?")
        print('1. Toy Story')
        print('2. Finding Nemo')
        print('3. Shrek')
        response = int(input('Please select a movie by nhumber: '))
        if response == 1:
            print('Here is your tickets for Toy Story')
        elif response == 2:
            print('Here is your tickets for Finding Nemo')
        elif response == 3:
            print('Here is your tickets for Shrek')
    else:
        print('Sorry we arent playing that movie')

movieTicket()


def atm():
    balance = 5000
    pin = 1234
    print('Welcome please type in your pin number')
    userPin = int(input())
    if userPin == pin:
        print('Welcome, what would you like to do?')
        print('1. Withdraw money')
        print('2. Deposit money')
        print('3. Check balance')
        select = int(input('Please selece an option: '))
        if select == 1:
            amount = int(input())
            if amount > balance:
                print('How much money would you like to widraw? ')
        elif select == 2:
            print('How much money would you like to deposit')
            amount = int(input())
            newBalance = balance + ammount
            print('You are addind to your account: ' + str(ammount))
        elif select == 3:
            print('Here is your balance: '+ str())

        else:
            print('Incorrect pin try again.')