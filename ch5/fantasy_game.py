#!/usr/bin/env python3.5
'''
fantasy_game.py prints the inventory for a fantasy game
'''


# function will not match linter
def displayInventory(inventory):
    '''
    displayInventory prints the player's current inventory
    '''

    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(str(value), str(key))
        item_total += value
        # FILL THIS PART IN
    print("Total number of items: " + str(item_total))


# function will mot match linter
def addToInventory(inventory, addedItems):
    '''
    add to inventory takes a dictionary inventory, and a list of values to add.

    those values are added to the inventory and returned.
    '''

    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory
