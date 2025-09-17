# how to create a function

# step 1. function definition

def bnbRefund(name,amount): # amount = placeholder / parameter
    print(name +' you will receive '+ str(amount) + ' back to your bank account')

# step 2. function call (invocation)
bnbRefund('Bob,',1500) #argument = real data thats passed.

def birthday(name,date):
    print('My name is '+ str(name) +' and my birthday is ' +  str(date))
birthday('Tyheem','November 1st')

def money(dollar):
    pennies = dollar * 100
    print('My '+str(dollar)+' is equal to '+ str(pennies) +' pennies')

money(60)

def area(len,wid,hei):
    print(len * wid * hei)
area(10,10,10)


# Activity 3

def aot(length,width,height):
    print(length*width*height)
aot(20,6,52)


# Activity 4

def temp(far):
    print(far - 32  * 5/9)
temp(89)