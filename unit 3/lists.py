# List- is a type of collection system where we can store and organize multiple forms of data

# we create lists using the squre brackets and assigning it to a variable
example = [1,2,3,4,5,6,'name','dob','year',True,[1,2,3,4,False,1.2]]
# print(example)

# we use lists to structure data in large applications

videos = ['cat video','music video','dancing video']

# we can manipulate lsits to add, remove, sort, etc.

videos.append('coding video')

# print(videos)

# create a function that will add a seasoning to a ist of food seasonings.
# your function should take in a user input, and should use the apend() function to 
# add the season to the seasoning list

# def seasoningShelf():
#    seasonings = ['salt','pepper','paprika','oregeno']
#    newSeasonings = input('Please add a aseasoning to the list: ')
#    seasonings.append(newseasoning)
#    print(seasonings)

# seasoningShelf()


def gameStorage():
    games = ['cod','gta','rl','fortnite']
    gamePicker = input('Please select a game you would like to remove from storage: ')
    games.remove(gamePicker)
    print(games)

# gameStorage()

# Creat a function that adds a new number to the list and puts it in order

numbersList = [100, 20, 203, 3, 5, 1000, 243]

def addAndSort(newNumber):
    numbersList.append(newNumber)
    numbersList.sort()
    print(numbersList)

addAndSort(60)

# add new logic to this funnction so that the list prints out in reverse order

numbersList = [100, 20, 203, 3, 5, 1000, 243]

def addAndSort(newNumber):
    numbersList.append(newNumber)
    numbersList.sort(reverse=True)
    print(numbersList)

addAndSort(60)