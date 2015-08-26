__author__ = 'patriot'

"""
Task
You have to read a string. change the character at a given index and print the string.

Input Format
First line contains a string, S.
Next line contains an integer i and a character c.

Output Format
Using any of the method explained above. Replace the character at index i with c.

Sample Input
abracadabra
5 k

Sample Output
abrackdabra
"""

S = raw_input()
t = raw_input().split(" ")
S = S[:int(t[0])] + t[1] + S[int(t[0])+1:]
print S