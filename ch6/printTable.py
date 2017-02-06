#!/usr/bin/env python3.5
'''
printTable() provides a way to print a right-justified table from a jagged list
'''


def printTable(tableData):
    col_width = []
    longest_col = 0
    for col in tableData:
        col_width.append(len(max(col, key=len)))
        if col_width[-1] > longest_col:
            longest_col = col_width[-1]

    offset = 0
    line = ''
    while offset < longest_col:
        i = 0
        while i < len(tableData):
            if i != 0:
                line += ' '
            if offset < len(tableData[i]):
                # in case there is a table cell missing, do not panic
                line += tableData[i][offset].rjust(col_width[i])
            i += 1
        line += "\n"
        offset += 1
    print(line)
