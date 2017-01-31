#!/usr/bin/env python3
'''
Chapter 4 of Automate the Boring Stuff

The first assignment for this chapter is to write a program - comma_code.py
This program includes the function `comma_code(list)` to process one step of the sequence.
Included is a second way to do this easier with join() - a function not yet introduced.

The second assignment includes a 2 level jagged list inversion with printout.
'''
# ch4 problem - https://automatetheboringstuff.com/chapter4/
# Written by Jack Hayhurst


def comma_code(parts):
    '''comma_code joints the elements in a list with an oxford comma'''
    output = ''
    for word in parts[:-1]:
        output += str(word)
        output += ', '
    output += 'and '
    output += str(parts[-1])
    return output


def picture_grid(data):
    '''picture_grid() takes a list of lists as an input, and inverts and prints the image'''
    xcord, ycord = (0, 0)
    while xcord < len(data[ycord]):
        while ycord < len(data):
            print(data[ycord][xcord], end='')
            ycord += 1
        xcord += 1
        ycord = 0
        print("")


if __name__ == "__main__":
    print('there is no default action defined for this file')
