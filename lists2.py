__author__ = 'patriot'

"""
Problem Statement

Now, lets delve into one of the most basic data types in python, LIST. You are given 'n' numbers. Store them in a list and find the second largest number. Easy enough!

NOTE : Don't use insertion sort

Input Format

First line contains N. Second line contains Array A[] of N integers each separated by a space.

Output Format

Value of the second largest number.
"""

N = int(raw_input())
l = map(int, raw_input().split(" "))
l.sort()
ma = l[len(l)-1]
l.pop()
while (len(l) > 0):
    if (l[len(l)-1] != ma):
        print l[len(l)-1]
        break
    else:
        ma = l[len(l)-1]
        l.pop()