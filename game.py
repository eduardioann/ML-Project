from random import shuffle


def shuffle_list(my_list):
    shuffle(mylist)
    return my_list


def user_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number from 0 to 2: ")
    return int(guess)


def check_guess(mylistt, guess):
    if mylistt[guess] == 'O':
        print("Correct!")
        print(mylistt)
    else:
        print("Wrong guess!")
        print(mylistt)

# INITIAL LIST


mylist = [' ', 'O', ' ']


# SHUFFLE LIST

shuffled_list = shuffle_list(mylist)

# USER GUESS

user_guessing = user_guess()

# CHECK GUESS

check_guess(shuffled_list, user_guessing)


# https://docs.google.com/document/d/181AMuP-V5VnSorl_q7p6BYd8mwXWBnsZY_sSPA8trfc/edit?usp=sharing
