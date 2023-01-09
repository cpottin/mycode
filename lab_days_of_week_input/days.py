#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter your name: ")
    days_of_week = input("Please enter the day of the week: ")
    # display the input back to the user.
    print("Hello, " + user_input + "! Happy " + days_of_week)
    
# this calls main
main()
