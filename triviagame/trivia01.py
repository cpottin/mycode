#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import time

URL= "https://opentdb.com/api.php?amount=10&category=27"

def main():
    print("Are you ready to play a Trivia Game?")
    start_game = input("Would you like to answer a question, Press Y or N: ")
    if(start_game == "Y"):
   # data will be a python dictionary rendered from your API link's JSON!
        data= requests.get(URL).json()
        print("Let's Begin")
        time.sleep(1)
        print()
        print(data['results'][0]["question"])
        print()
        print("You have 3 seconds to guess the answer")
        time.sleep(3)
        print("1")
        time.sleep(2)
        print("2")
        print()
        user_answer = input("Please enter your answer : ")

        if(user_answer == data['results'][0]['correct_answer']):
            print("Great Job! You got it right")
        else:
            print("Better Luck next time, that was not correct")
            print("The correct answer is : " , data['results'][0]["correct_answer"])
    else:
        print("Thank you")


if __name__ == "__main__":
    main()
