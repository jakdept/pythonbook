#!/usr/bin/env python3
'''
Chapter 4 of Automate the Boring Stuff

Picture grid includes a 2 level jagged list inversion with printout.
'''
# ch4 problem - https://automatetheboringstuff.com/chapter4/
# Written by Jack Hayhurst



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
