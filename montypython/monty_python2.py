#!/usr/bin/env python3


round = 0

while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')

    answer = input("Your guess--> ")
#if user enters brain return correct and exit code
    if answer.lower() == 'brain':
        print('Correct')
        break
#before allowing another guess check to see if they have reached 3 guesses
    elif round ==3:
        print("Sorry, the answer was Brain.")
        break
    #if guesses are not 3 then let them guess again
    else:
        print("Sorry! Try again!")


