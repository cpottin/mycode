#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import time

URL= "https://opentdb.com/api.php?amount=10&category=27"

def main():
    print("Are you ready to play a Trivia Game?")
    start_game = input("Enter Y to start the game OR N to exit: ")

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

    print(data['results'][0]["correct_answer"])


if __name__ == "__main__":
    main()
