#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi["sprites"]["front_default"])
    moves = pokeapi["moves"]
    for x in moves:
        print(x["move"]["name"])

    games_count = pokeapi["game_indices"]
    print("This Pokemon appeared in the following number of games:  ", len(games_count))
main()

