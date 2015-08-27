__author__ = 'patriot'

S1 = raw_input()
S2 = raw_input()
c = 0
for i in range(len(S1) - len(S2) + 1):
    if S1[i:i+len(S2)] == S2:
        c += 1
print c
