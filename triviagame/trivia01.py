#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=10&category=27"

def main():
    print("Are you ready to play a Trivia Game?")
    start_game = input("Enter Y to start the game OR N to exit: ")

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    

if __name__ == "__main__":
    main()
