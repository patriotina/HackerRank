__author__ = 'patriot'


def patatoi(s):
    res = 0
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            res = res * 10  + (ord(s[i]) - ord('0'))
    return res

print patatoi("12345")