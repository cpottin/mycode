#!/usr/bin/env python3
import random

print("Hello, I can tell the future. ")
print(".............................")
print()
print("All you have to do is ask a question")


def question():
    eightball_responses = ["Odds are not good", 
            "Absolutley", "Very Likely", "It's a No"]

    user_question =input("What is your question? : ")

    if user_question !="":
        random_rep = random.choice(eightball_responses)
     
         ##print(random_rep)
        if random_rep == "It's a No":
            print("I'm sorry ..." + random_rep)
        elif random_rep == "Absolutley":
            print("You are in luck..." + random_rep)
        elif random_rep == "Very Likely":
            print("Looks like it is ...." + random_rep)
        else:
            print("Better luck next time it looks like.." + random_rep)
    else:
        print("You did not ask a questions. Please try again")

question()

print()
user_secondq = input("Do you have another question? : ")

if user_secondq == "yes":
    question()
else:
    print("Thank you for playing. Goodbye.")

#count = 0
#while count < 3:
#    print("You have asked ")
#    print(count)
#    print("questions")
#    count += 1
#else:
#    print("I need a break you have asked your max number of questions")
