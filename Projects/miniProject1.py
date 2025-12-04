q1 ='Summer is hot'
q2 ='It snows in summer.'
q3 ='School is important'
q4 ='The video game is more important than your health.'
q5 = 'Winter is cold'

print("Please answer these 5 questions with a True or False.")

def torf():
    print(q1)
    userinp = input('True or False? ')
    if userinp == 'True':
        print('Correct')
    elif userinp == 'False':
        print('You are incorrect')
        print(q2)
    elif userinp == 'False':
        print('Correct')
    elif userinp == 'True':
        print('Incorrect')
        print(q3)
    elif userinp == 'True':
        print('Correct')
    elif userinp == 'False':
        print('Incorrect')
        print(q4)
    elif userinp == 'False':
        print('Correcet')
    elif userinp == 'True':
        print('Incorrect')
        print(q5)
    elif userinp == 'True':
        print('Correct')
    else:
        print('Incorret')

torf()