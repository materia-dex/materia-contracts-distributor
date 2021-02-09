#!/usr/bin/env python

from sys import argv, exit


def main(argv):
    if len(argv) != 2:
        print('Error: provide a CSV file')
        exit(-1)
    with open(argv[1]) as csv_file:
        print('{', end='')
        print(','.join(f'{address}:"{int(float(amount[1:-1])*10**18)}"' for (address, amount, _) in map(lambda l: l.split(','), csv_file.readlines()[1:])), end='')
        print('}', end='')


main(argv)
