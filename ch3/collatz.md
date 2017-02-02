#!/usr/bin/env python3
'''
Chapter 3 of Automate the Boring Stuff
The assignment for this chapter is to write a program - collatz.py.
This program includes the function `collatz()` to process one step of the sequence.
It also includes a function to repeatedly run the function as needed to reduce a given int.
'''
# ch3 problem - https://automatetheboringstuff.com/chapter3/
# Written by Jack Hayhurst

import sys

def collatz(number):
    '''collatz() takes a single step through the collatz() sequence'''
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

def run_sequence():
    '''runSequence() prompts the user for a given number and runs the collatz sequence on it'''
    try:
        number = int(input("Enter number:"))
    except ValueError:
        print("you must enter an integer")
        sys.exit()
    while number is not 1:
        number = collatz(number)

def main():
    '''main is the main entry point of this file'''
    run_sequence()

if __name__ == "__main__":
    main()
