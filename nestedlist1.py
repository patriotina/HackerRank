__author__ = 'patriot'

"""
Problem Statement
Now we will see how to implement a nested list. There is a classroom of 'n' students
and you are given their names and marks in physics. Store them in a nested list and
print the name of each student who got the second lowest marks in physics.
NOTE: If there are more than one student getting same marks, make sure you print
the names of all students in alphabetical order, in different lines.

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
"""
marksheet = []
for _ in range(0, int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
"""

l = []
for i in range(int(raw_input())):
    l.append([raw_input(), float(raw_input())])
l.sort()
l2 = sorted(l, key=lambda st: st[1])
mi = l2[0][1]
l2.pop(0)
while len(l2) > 0:
    if l2[0][1] != mi:
        print l2[0][0]
        mi2 = l2[0][1]
        l2.pop(0)
        while len(l2) > 0:
            if l2[0][1] == mi2:
                print l2[0][0]
                l2.pop(0)
            else:
                break
        break
    else:
        l2.pop(0)