__author__ = 'patriot'

"""
Problem Statement
Now we will see how to implement a nested list. There is a classroom of 'n' students and you are given their names and marks in physics. Store them in a nested list and print the name of each student who got the second lowest marks in physics.
NOTE: If there are more than one student getting same marks, make sure you print the names of all students in alphabetical order, in different lines.

Input Format
Integer $N$ followed by alternating sequence of N strings and N numbers.

Output Format
Name of student.

Constraints
    $1 \le N \le 5$
Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output

Berry
Harry
"""

N = int(raw_input())
l = []
for i in range(N):
    p = [raw_input()]
    p.append(float(raw_input()))
    l.append(p)
    p = []
l.sort()
print(l)