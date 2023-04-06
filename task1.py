#!/usr/bin/env python3

# Task 1
# What is FOR loop
# ---
# You have a positive integer number N as an input. Please write a program in Python 3 that
# calculates the sum in range 1 and N.


import sys


def calc_sum(N: int) -> int:
    assert N > 0
    return N*(N+1)//2


if __name__ == '__main__':
    N = 0
    if len(sys.argv) > 1: N = int(sys.argv[1])
    else: N = int(input('>'))
    print(calc_sum(N))
