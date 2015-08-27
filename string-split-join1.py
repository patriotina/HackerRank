__author__ = 'patriot'

"""
Task
You are given a string. Split the string on " " (space) delimiter and join using a - hiphen.

Input Format
The first line contains a string consisting of words separated by space.

Output Format
Print the formatted string as explained above.

Sample Input

this is a string

Sample Output

this-is-a-string
"""

#S = raw_input()
#l = S.split(" ")
#St = '-'.join(l)
print "-".join(raw_input().split(" "))