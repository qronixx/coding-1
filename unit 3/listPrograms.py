food = ['ribTips', 'Rice', 'Cabbage', 'oreos']
food.sort()
#print(food[0]) # first item in list
#print(food[1]) # last item in list

# replace the second list item with a new food, then print

time = input('Is it currently morning day or night? ')

def menu():
    morning = ['Sasuge and Pancakes', 'Sasuge and Waffles', 'Bacon and Eggs w Toast']
    afternoon = ['Tacos', 'Grilled Cheese', 'Burger and Fries']
    night = ['Alfredo', 'Soup', 'BBQ Chicken']
    if time == 'morning':
        print(morning)
    elif time == 'afternoon':
        print(afternoon)
    elif time == 'night':
        print(night)
    else:
        print('Time of day is not recognized. Please try again.')
menu()